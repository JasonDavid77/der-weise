# install.ps1 -- richtet den Weisen ein (Windows, ohne Adminrechte).
#
# Gefahrlos wiederholbar: jeder Schritt prueft zuerst, was schon da ist.
# Erneut laufen lassen = Reparatur oder Update auf die Plugin-Version.
#
# Aufruf (so startet ihn /weise:einrichten):
#   powershell -NoProfile -ExecutionPolicy Bypass -File "${CLAUDE_PLUGIN_ROOT}/setup/install.ps1"
#
# Optionen:
#   -Werkraum <Ordner>   Ordner der Lernthemen (Standard: werkraum aus config.json,
#                        sonst <WeiseHome>\themen)
#   -WeiseHome <Ordner>  Technik-Ordner (Standard: Umgebungsvariable WEISE_HOME,
#                        sonst %USERPROFILE%\weise)
#   -PythonExe <Pfad>    vorhandenes Python 3.12 nutzen statt zu suchen/installieren
#   -OhnePakete          Umgebung, Pakete und Modell auslassen (nur Dateien kopieren)
#
# config.json wird zusammengefuehrt: vorhandene Felder bleiben erhalten, werkraum
# wird nur gesetzt, wenn er fehlt oder per -Werkraum angegeben ist. Nach Erfolg
# steht die Plugin-Version in <WeiseHome>\version.txt.
#
# Diese Datei ist bewusst reines ASCII (Windows PowerShell 5.1 liest UTF-8 ohne
# BOM sonst falsch).

param(
  [string]$Werkraum = "",
  [string]$WeiseHome = "",
  [string]$PythonExe = "",
  [switch]$OhnePakete
)

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$BundleRoot = Split-Path -Parent $PSScriptRoot
$PyVersion = "3.12.10"

function Schritt([string]$text) { Write-Host ""; Write-Host ("== " + $text) }
function Ok([string]$text) { Write-Host ("   OK: " + $text) }
function Abbruch([string]$text) { Write-Host ("   FEHLER: " + $text); exit 1 }
function Schreibe-Utf8([string]$pfad, [string]$inhalt) {
  [IO.File]::WriteAllText($pfad, $inhalt, (New-Object Text.UTF8Encoding($false)))
}
function Python-Ist-312([string]$exe) {
  if (-not $exe -or -not (Test-Path $exe)) { return $false }
  try {
    $v = & $exe -c "import sys;print('%d.%d' % sys.version_info[:2])" 2>$null
    return ($LASTEXITCODE -eq 0 -and $v -eq "3.12")
  } catch { return $false }
}
function Voller-Pfad([string]$pfad) {
  if (-not $pfad) { return $pfad }
  if (-not [IO.Path]::IsPathRooted($pfad)) { $pfad = Join-Path (Get-Location).Path $pfad }
  return [IO.Path]::GetFullPath($pfad).TrimEnd([char]92)
}

# Technik-Ordner: -WeiseHome, sonst Umgebungsvariable WEISE_HOME, sonst %USERPROFILE%\weise
$HomeAusUmgebung = Voller-Pfad $env:WEISE_HOME
if (-not $WeiseHome) { $WeiseHome = $env:WEISE_HOME }
if (-not $WeiseHome) { $WeiseHome = "$env:USERPROFILE\weise" }
$WeiseHome = Voller-Pfad $WeiseHome
$Werkraum = Voller-Pfad $Werkraum
$StandardHome = [IO.Path]::GetFullPath("$env:USERPROFILE\weise")
# Die Skripte finden den Technik-Ordner nur ueber WEISE_HOME oder den Standard;
# fuer Modell-Download und Selbsttest in diesem Lauf deshalb hier setzen.
$env:WEISE_HOME = $WeiseHome

# Aus dem Internet stammende Dateien freigeben (sonst blockiert Windows sie).
try { Get-ChildItem -Recurse -LiteralPath $BundleRoot | Unblock-File } catch { }

Write-Host "Weise einrichten -- Bundle: $BundleRoot"
Write-Host "Technik-Ordner: $WeiseHome"

# -- 1) Python 3.12 (nur fuer diesen Benutzer) --------------------------------
if (-not $OhnePakete) {
  Schritt "Python 3.12 finden oder fuer diesen Benutzer installieren"
  $Standard = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
  if (-not $PythonExe) { $PythonExe = $Standard }
  $OhnePythonHinweis = "Der Weise laeuft auch ohne Python (Stichwortsuche statt Speicher). Fehlerbilder: /weise:einrichten oder https://github.com/JasonDavid77/der-weise/blob/main/docs/hilfe.md"
  if (-not (Python-Ist-312 $PythonExe)) {
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if ($winget) {
      Write-Host "   Installiere Python $PyVersion ueber winget (Benutzer-Installation) ..."
      Write-Host "   Hinweis: winget nimmt dabei die Nutzungsbedingungen der Paketquelle an."
      # --override: dieselben Installer-Schalter wie beim python.org-Weg (kein PATH, kein Launcher)
      $wingetCode = 1
      try {
        & winget install --id Python.Python.3.12 -e --version $PyVersion --scope user --accept-package-agreements --accept-source-agreements --disable-interactivity --override "/quiet InstallAllUsers=0 PrependPath=0 Include_launcher=0 Include_test=0 Shortcuts=0"
        $wingetCode = $LASTEXITCODE
      } catch { Write-Host "   winget liess sich nicht starten: $($_.Exception.Message)" }
      # winget meldet auch dann Erfolg, wenn ein Schutzprogramm den Installer beendet hat
      # (beobachtet 2026-09-28). Deshalb selbst pruefen. Bei gemeldetem Erfolg ohne Python
      # NICHT den zweiten Weg gehen: der scheitert an derselben Sperre nur ein zweites Mal.
      # Scheitert winget selbst (Fehlercode, z.B. Quelle gesperrt), bleibt python.org der Ersatzweg.
      if ($wingetCode -eq 0 -and -not (Python-Ist-312 $Standard)) {
        Abbruch "winget meldet Erfolg, aber Python fehlt oder startet nicht. Vermutlich stoppt ein Schutzprogramm den Installer. Nichts umgehen. $OhnePythonHinweis"
      }
    }
    if (-not (Python-Ist-312 $Standard)) {
      Write-Host "   winget nicht verfuegbar oder gescheitert -- nutze den offiziellen Installer von python.org ..."
      $url = "https://www.python.org/ftp/python/$PyVersion/python-$PyVersion-amd64.exe"
      $exe = Join-Path $env:TEMP "python-$PyVersion-amd64.exe"
      try { Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $exe }
      catch { Abbruch "Download von python.org gescheitert: $($_.Exception.Message). $OhnePythonHinweis" }
      try { Unblock-File $exe }
      catch { Abbruch "Der geladene Installer ist nicht mehr zugreifbar ($($_.Exception.Message)), vermutlich vom Virenschutz entfernt. Nichts umgehen. $OhnePythonHinweis" }
      try { $p = Start-Process -FilePath $exe -Wait -PassThru -ArgumentList "/quiet","InstallAllUsers=0","PrependPath=0","Include_launcher=0","Include_test=0","Shortcuts=0" }
      catch { Abbruch "Der Python-Installer darf nicht starten ($($_.Exception.Message)). Nichts umgehen. $OhnePythonHinweis" }
      if ($p.ExitCode -ne 0) { Abbruch "Python-Installer endete mit Code $($p.ExitCode). $OhnePythonHinweis" }
    }
    $PythonExe = $Standard
  }
  if (-not (Python-Ist-312 $PythonExe)) { Abbruch "Python 3.12 nicht gefunden unter $PythonExe. $OhnePythonHinweis" }
  Ok ("Python " + (& $PythonExe -c "import sys;print(sys.version.split()[0])") + " unter $PythonExe")
}

# -- 2) Technik-Ordner und Skripte --------------------------------------------
Schritt "Technik-Ordner anlegen und Skripte kopieren"
foreach ($d in @("", "scripts", "speicher", "modelle", "sicherung")) {
  $ziel = Join-Path $WeiseHome $d
  if (-not (Test-Path $ziel)) { New-Item -ItemType Directory -Path $ziel | Out-Null }
}
Copy-Item -Path (Join-Path $BundleRoot "scripts\*") -Destination (Join-Path $WeiseHome "scripts") -Recurse -Force
Copy-Item -Path (Join-Path $BundleRoot "setup\requirements.txt"), (Join-Path $BundleRoot "setup\constraints.txt") -Destination $WeiseHome -Force
Ok "Skripte liegen in $WeiseHome\scripts"
if ($WeiseHome -ne $StandardHome -and $WeiseHome -ne $HomeAusUmgebung) {
  Write-Host "   Hinweis: Technik-Ordner weicht vom Standard ab. Damit der Weise ihn findet, die Umgebungsvariable WEISE_HOME fuer diesen Benutzer auf $WeiseHome setzen."
}

# -- 3) Werkraum und config.json ----------------------------------------------
Schritt "Werkraum (Ordner der Lernthemen) festlegen"
$ConfigPfad = Join-Path $WeiseHome "config.json"
# Zusammenfuehren: vorhandene Felder (Profil aus /weise:einrichten) bleiben erhalten.
$Config = New-Object PSObject
$ConfigGeaendert = $false
if (Test-Path -LiteralPath $ConfigPfad) {
  # ReadAllText erkennt und entfernt ein BOM am Anfang
  $roh = [IO.File]::ReadAllText($ConfigPfad, [Text.Encoding]::UTF8)
  if ($roh.Trim()) {
    try { $Config = $roh | ConvertFrom-Json }
    catch { Abbruch "config.json ist kein gueltiges JSON ($ConfigPfad). Nichts geaendert; Datei pruefen oder /weise:einrichten." }
    if ($Config -isnot [System.Management.Automation.PSCustomObject]) {
      Abbruch "config.json enthaelt kein JSON-Objekt ($ConfigPfad). Nichts geaendert; Datei pruefen oder /weise:einrichten."
    }
  } else { $ConfigGeaendert = $true }
} else { $ConfigGeaendert = $true }
$Eingetragen = ""
if ($Config.PSObject.Properties["werkraum"]) { $Eingetragen = [string]$Config.werkraum }
if (-not $Werkraum) {
  $Werkraum = $Eingetragen
  if (-not $Werkraum) { $Werkraum = Join-Path $WeiseHome "themen" }
}
if ($Werkraum -cne $Eingetragen) {
  $Config | Add-Member -NotePropertyName "werkraum" -NotePropertyValue $Werkraum -Force
  $ConfigGeaendert = $true
}
# Umgebungsvariablen im eingetragenen Pfad (z.B. %USERPROFILE%) aufloesen, wie die Skripte es tun
$WerkraumOrdner = [Environment]::ExpandEnvironmentVariables($Werkraum)
if (-not (Test-Path -LiteralPath $WerkraumOrdner)) { New-Item -ItemType Directory -Path $WerkraumOrdner | Out-Null }
if ($ConfigGeaendert) { Schreibe-Utf8 $ConfigPfad ($Config | ConvertTo-Json -Depth 20) }
foreach ($f in @("werkzeug-register.md", "_themen.md")) {
  $ziel = Join-Path $WerkraumOrdner $f
  if (-not (Test-Path -LiteralPath $ziel)) { Copy-Item (Join-Path $BundleRoot "setup\$f") $ziel }
}
Ok "Werkraum: $Werkraum (in $ConfigPfad eingetragen)"

# -- 4) Python-Umgebung und Pakete --------------------------------------------
$VenvPy = Join-Path $WeiseHome "venv\Scripts\python.exe"
if (-not $OhnePakete) {
  Schritt "Python-Umgebung anlegen und Pakete installieren (einmalig rund 1 GB Download)"
  # Windows begrenzt Pfade auf 260 Zeichen (ohne "Long Paths"). Die laengste
  # Paketdatei braucht rund 140 Zeichen unterhalb von site-packages.
  $SitePackages = Join-Path $WeiseHome "venv\Lib\site-packages\"
  $LongPaths = (Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -ErrorAction SilentlyContinue).LongPathsEnabled
  if ($LongPaths -ne 1 -and ($SitePackages.Length + 140) -gt 259) {
    Abbruch "Der Technik-Ordner liegt zu tief ($($SitePackages.Length) Zeichen bis site-packages). Kuerzeren Technik-Ordner waehlen: Umgebungsvariable WEISE_HOME fuer diesen Benutzer z.B. auf C:\weise setzen, neue Sitzung, dann /weise:einrichten."
  }
  if (-not (Test-Path $VenvPy)) {
    & $PythonExe -m venv (Join-Path $WeiseHome "venv")
    if ($LASTEXITCODE -ne 0) { Abbruch "venv konnte nicht angelegt werden" }
  }
  & $VenvPy -m pip install --disable-pip-version-check -r (Join-Path $WeiseHome "requirements.txt") -c (Join-Path $WeiseHome "constraints.txt")
  if ($LASTEXITCODE -ne 0) { Abbruch "Paket-Installation gescheitert (Meldung oben). Fehlerbilder: /weise:einrichten oder https://github.com/JasonDavid77/der-weise/blob/main/docs/hilfe.md" }
  Ok "Pakete installiert"

  # -- 5) Sprachmodell ---------------------------------------------------------
  Schritt "Sprachmodell einmalig laden (rund 0,5 GB)"
  & $VenvPy (Join-Path $WeiseHome "scripts\download-model.py")
  if ($LASTEXITCODE -ne 0) { Abbruch "Modell-Download gescheitert. Fehlerbilder: /weise:einrichten oder https://github.com/JasonDavid77/der-weise/blob/main/docs/hilfe.md" }
}

# -- 6) Selbsttest ------------------------------------------------------------
if (-not $OhnePakete) {
  Schritt "Selbsttest"
  & $VenvPy (Join-Path $WeiseHome "scripts\self-check.py")
  if ($LASTEXITCODE -ne 0) { Abbruch "Selbsttest nicht bestanden (Ausgabe oben)" }
}

# -- 7) Version der Technik ---------------------------------------------------
# Die Skills vergleichen version.txt mit der Plugin-Version (Technik aktuell?).
Schritt "Version der Technik festhalten"
$Version = "unbekannt"
try {
  $Manifest = [IO.File]::ReadAllText((Join-Path $BundleRoot ".claude-plugin\plugin.json"), [Text.Encoding]::UTF8) | ConvertFrom-Json
  if ($Manifest.version) { $Version = [string]$Manifest.version }
} catch { }
Schreibe-Utf8 (Join-Path $WeiseHome "version.txt") $Version
Ok "Version $Version in $WeiseHome\version.txt"

Write-Host ""
Write-Host "Fertig. Der Weise ist eingerichtet."
