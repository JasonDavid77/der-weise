# Der Weise: learning on the job

[Deutsch](README.md) | **English**

Der Weise ("the sage") is a learning partner for Claude Code that teaches you a tool or a field while you use it on a real project. It explains every concept from scratch, applies it to your project right away and makes what you learned stick with recall cards. It is meant for people without a technical background, for example lawyers who bring AI tools into their work.

Der Weise works in the Claude desktop app under the "Code" tab or in Claude Code in the terminal, not in the regular chat. It answers in the language you write in; the skill files themselves are in German.

## Quick start

**In the Claude desktop app by clicking:** your profile at the bottom left, then **Settings**, then **Plugins** (in the German interface under "Anweisungen"). Enter the repository `JasonDavid77/claude-plugins` there, then click the plus sign next to Der Weise. Continue with step 3.

**Or by command** (desktop app in the "Code" tab, or the terminal):

1. Add the catalog. Type into the Claude Code input:

   ```
   /plugin marketplace add JasonDavid77/claude-plugins
   ```

2. Install Der Weise:

   ```
   /plugin install weise@jason-lau-christen
   ```

   Both in one step also works: `/plugin install weise --marketplace JasonDavid77/claude-plugins`

3. Start a new session (or type `/reload-plugins`) and set it up:

   ```
   /weise:einrichten
   ```

   Der Weise asks, in conversation, for its name, the form of address (formal "Sie" or informal "du" in German), signs and totems, your name, how you want research done and the folder for your learning topics. If your own agent already has a name, it suggests that one: "Max" becomes "Max der Weise". Then it suggests the first step, for example "New learning topic: …".

## The five skills

| Command | What it does |
|---|---|
| `/weise:einrichten` | Sets up Der Weise in conversation and offers the full search; runs only when you type the command. |
| `/weise:thema` | Creates a new learning topic or updates an existing one, starting with your learning goal. |
| `/weise:lernen` | Runs a learning session: due recall cards first, then the next concept, explained and built right into your project. |
| `/weise:vorschlag` | Turns your improvement idea into a proposal and, after your approval, submits it as a public issue. |
| `/weise:paket` | Imports a knowledge pack as a learning topic or updates it (see below); runs only when you type the command. |

You don't need to remember the commands. Phrases such as "new learning topic: …", "let's keep learning" or "quiz me" are enough.

## Knowledge packs

A knowledge pack is ready-made learning material on one topic, for example the guides of a tool as text. It is a small plugin of its own without commands and holds only data: the texts and a list with one checksum per file. It contains no learning goal, no progress and no recall cards; those are created on your side. If a pack does bring commands, hooks or a server, Der Weise does not import it. Only install packs from catalogs you trust. The pack format is described in [docs/wissenspaket.md](docs/wissenspaket.md).

1. Install the pack like any plugin, from the catalog that lists it.
2. Run `/weise:paket`. Der Weise finds the installed packs, checks every file, asks for your learning goal and creates the topic in your topics folder, in FULL mode also in the store. If a pack is a folder (for example a Git clone), pass the folder: `/weise:paket <folder>`.
3. When a new pack version arrives, run `/weise:paket` again. Der Weise replaces only the pack material in `sources/paket/` and archives the old state. Your learning goal, notes, cards and your own sources stay.

Packs from a private catalog need read access to its repository. Claude Code cannot ask for a password while loading; the sign-in must already be stored in Git (easiest: clone the repository once yourself).

## An example

This is how Der Weise guided us through a real build in Microsoft Power Automate: the lesson first, then the build step in the tool. The conversation below is re-enacted and shortened; topic and content are test data.

> **You:** New learning topic: TEST requests via a form
>
> **Der Weise:** Gladly. The goal first: what should be running at the end?
>
> **You:** Whoever fills in our form should land in a list automatically and get a confirmation email.
>
> **Der Weise:** Then that is our goal. What do you already know about Power Automate, and where are you stuck? After that I will give you a list of research topics to approve.

A few days later, in the middle of the build:

> **You:** Let's keep learning.

```
🧙 Der Weise: TEST requests via a form
| WISSEN: thema=test-requests, VOLL (180 Abschnitte) | Modus: NORMAL |
| LERNPFAD                            | DELIVERABLE-SPUR             |
| [x] K1 Trigger                sitzt | [x] Form is ready            |
| [~] K2 Response details  <==  läuft | [~] Flow fetches the answer  |
Form > [Flow] > List > Mail
```

The board keeps the German labels of the skill files: WISSEN (knowledge), VOLL (full mode), Abschnitte (sections), Modus (mode), LERNPFAD (learning path), DELIVERABLE-SPUR (deliverable track), sitzt (solid), läuft (in progress).

> **Der Weise:** 📖 K2, from zero: the trigger only reports *that* someone submitted the form and hands over a number for that response. The answers themselves are fetched by a second step, "Get response details". In everyday terms: the doorbell tells you the mail has arrived; you still have to take the letter out of the box.
>
> ❓ One question before we build: what would end up in the list if we left out this second step?
>
> **You:** Only the number, not the answers.
>
> **Der Weise:** ✅ Exactly. 🛠️ Build step, just one:
> 1. Below the trigger "When a new response is submitted", click **Add an action**.
> 2. Search for `Get response details` and pick the **Microsoft Forms** action.
> 3. **Form Id:** the same form as in the trigger. **Response Id:** from the dynamic content, the trigger's **Response Id**.
> 4. **Save**, then tell me what you see.
>
> *Sources: sources/forms-trigger.md, ui-observed.md (UI map)*

Every tool topic runs like this: the idea from zero, then one question, then a single build step with the real labels. What you learned comes back as a recall card.

## Two modes

Der Weise detects on its own which mode is running. The board shows it in the first line.

- **FULL** (VOLL in German; recommended, Windows): with its own Python environment and a local store that searches by meaning. A German question also finds an English guide. Recall cards are scheduled with a proven method (FSRS). Set up via `/weise:einrichten`, a one-time download of about 1.5 GB.
- **Keyword search** (OHNE PYTHON in German, "without Python"): no installation at all. Der Weise searches your topic files for keywords in German and English, and a simple box rule schedules the reviews. Everything else is the same. This mode applies automatically when Python is missing or blocked.

To switch to FULL later, run `/weise:einrichten` again. Your topics and recall cards are kept.

## Requirements

- **Claude Code:** the Claude desktop app with the "Code" tab, or Claude Code in the terminal.
- **Git:** Claude Code loads the catalog via Git. Check in PowerShell with `git --version`. If Git is missing, install it from [git-scm.com](https://git-scm.com) or ask your IT. You don't need a GitHub account for this.
- **Additionally for FULL:** Windows (64-bit), about 2.5 GB of free space, internet once for a download of about 1.5 GB, and 10 to 30 minutes. No admin rights needed.

**Limits:** Der Weise is tested on Windows. On macOS and Linux only keyword search is intended, and it is not tested there yet. There is currently no way to install without Git.

## What Der Weise does on your computer

- **Your data stays local** in one folder: `%USERPROFILE%\weise` (can be changed with the environment variable `WEISE_HOME`). It holds your learning topics (`themen\`, or the folder you choose during setup), your profile (`config.json`), backups and drafts of your proposals; with FULL also the Python environment, the store and the language model. Der Weise writes nothing into the plugin folder, because Claude Code replaces it on every update.
- **Downloads happen once and only with your consent** (FULL): Python 3.12 from python.org (via winget, if available), about 95 Python packages in pinned versions from pypi.org and a language model (paraphrase-multilingual-MiniLM-L12-v2, about 0.5 GB) from huggingface.co. After that, search runs offline.
- **Telemetry is off:** the packages send no usage data.
- **No hooks, no MCP server, no background service.** Der Weise runs only when you call it, by command or with a phrase like "let's keep learning".
- **It changes Claude settings only after asking:** `/weise:einrichten` offers to add the folder `%USERPROFILE%\weise` (and your topics folder, if it lives elsewhere) as an additional working directory in `%USERPROFILE%\.claude\settings.json`, so Der Weise can read there without prompts. You see the change first. If it finds older copies of Der Weise under `%USERPROFILE%\.claude\skills`, it moves them to the backup folder after you agree. Nothing is deleted.
- **Web search only if you choose it:** with the setting "websuche" Der Weise searches the web itself, and only after you have approved the topic list. With "werkzeug" it writes research prompts for your own research tool and only searches itself if you explicitly ask it to. The prompts are numbered (R1, R2, …) and stored as files in the topic's `auftraege` folder; Der Weise opens that folder in your file manager and keeps an overview. You put each result under the same number into the `eingang` folder. At the start of the next session Der Weise works it into the topic's synthesis.
- **Knowledge packs are only read:** `/weise:paket` reads the list of your installed plugins (`%USERPROFILE%\.claude\plugins\installed_plugins.json`, or else the plugin folder) and the folders of the knowledge packs, checks the files with PowerShell and copies them into your topics folder. On "new learning topic", `/weise:thema` looks in the same places for a matching installed pack. Der Weise writes nothing into plugin folders.
- **Proposals only after your approval:** `/weise:vorschlag` removes names, paths and confidential details, shows you the final text and asks how to submit it. If the GitHub command line `gh` is signed in on your computer, Der Weise can send the proposal directly after your approval; it first names the account the issue will appear under, and for that it asks github.com once for the account name. Otherwise it opens the prefilled form in your browser and you click submit yourself. You can also just save it. Der Weise never sets up an account or a sign-in. Issues on GitHub are public.
- **The conversation itself** is processed by Claude like in any Claude Code session, including the files Der Weise reads for it. So keep confidential content out of your learning topics: no case files, client or customer data. Der Weise works with learning material, guides and invented practice cases.

## Updates

By default, Claude Code does not update third-party catalogs on its own. To turn this on once for this catalog: type `/plugin`, choose "Marketplaces", then `jason-lau-christen`, then "Enable auto-update". New versions then arrive when Claude Code starts.

Manually: type `/plugin`, pick Der Weise under "Installed", choose "Update now", then start a new session. In the desktop app you also find your plugins via the plus sign (+) under "Plugins".

If, after an update, the installed technology is older than the plugin, Der Weise says so in one sentence. Then run `/weise:einrichten` once.

Changes are listed in the [CHANGELOG](CHANGELOG.md) (German).

## Uninstall

```
/plugin uninstall weise@jason-lau-christen
/plugin marketplace remove jason-lau-christen
```

Knowledge packs are plugins of their own and stay installed. Remove them with `/plugin uninstall <pack>@<catalog>`; imported topics stay in your topics folder.

**Your data is kept.** Topics, profile and technology live in `%USERPROFILE%\weise` (or in the topics folder you chose), and Claude Code deletes nothing there. To remove everything:

1. Back up your learning topics if you want to keep them.
2. Delete the folder `%USERPROFILE%\weise` (and your own topics folder, if you chose one).
3. FULL only: remove Python 3.12 in Windows Settings under "Apps", if setup installed it and you don't use it otherwise.
4. If you agreed to this during setup: remove the entries of Der Weise under `additionalDirectories` in `%USERPROFILE%\.claude\settings.json`.

## Help and proposals

- **If something is stuck:** [docs/hilfe.md](docs/hilfe.md) (German) lists the known problems. `/weise:einrichten` shows your profile and checks the technology at any time.
- **Proposals and bugs:** with `/weise:vorschlag` or directly as an [issue](https://github.com/JasonDavid77/der-weise/issues). Submitting an issue needs a free GitHub account. Der Weise also saves every proposal under `%USERPROFILE%\weise\vorschlaege\`; it stays there, with its status (saved, opened in the browser, or submitted with link).
- **No GitHub account:** send the saved file via [LinkedIn](https://www.linkedin.com/in/jason-lau-christen-81bbb3240).
- **Contributing:** please open an issue before sending a pull request.
- **Security issues:** please don't report them as issues; follow [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE), Copyright (c) 2026 Jason Lau-Christen.
