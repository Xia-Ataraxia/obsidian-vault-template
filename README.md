<div align="center">
  <h1>Obsidian Template</h1>
  <p><strong>A home for your notes. A system for your thinking.</strong></p>
  <p>PARA organization, Zettelkasten thinking, and periodic planning — with shared rules for humans and AI agents.</p>
  <p>
    <strong>English</strong> ·
    <a href="README.ko.md">한국어</a>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Obsidian-7C3AED?style=flat&amp;logo=obsidian&amp;logoColor=white" alt="Obsidian" />
    <img src="https://img.shields.io/badge/Markdown-000000?style=flat&amp;logo=markdown&amp;logoColor=white" alt="Markdown" />
    <img src="https://img.shields.io/badge/EN%20%7C%20KO-bilingual-1F6FEB?style=flat" alt="Bilingual English and Korean" />
  </p>
  <p>
    <a href="90.%20Settings/01%20Guideline/01.%20Folders%20and%20Placement.md">Placement</a>
    ·
    <a href="90.%20Settings/01%20Guideline/08.%20Writing%20and%20AI.md">Writing and AI</a>
    ·
    <a href="90.%20Settings/02%20Templates/README.md">Templates</a>
    ·
    <a href="90.%20Settings/01%20Guideline/09.%20Agent%20Skills.md">Agent Skills</a>
    ·
    <a href="90.%20Settings/01%20Guideline/">Guidelines</a>
    ·
    <a href="AGENTS.md">Agent guidelines</a>
  </p>
</div>

## Less organizing. More connecting.

Start with a working structure, not someone else's personal notes. Download the ZIP, open the folder as a **new** vault, and write ordinary Markdown — Git and community plugins are optional until you need them. Give each note one canonical home, connect ideas across projects, and plan from year to day. Humans and agents share the same placement rules.

- **One home per note.** File by what the note is, not who wrote it or which tool captured it.
- **PARA plus Zettelkasten.** Projects and areas stay separate from literature notes and evergreen ideas.
- **A planning chain that matches review.** Folder numbers are labels; the hierarchy is the period chain.
- **Portable on purpose.** Personal notes, credentials, plugin caches, theme binaries, and machine-specific state are not included. Templater, Homepage, Omnisearch, Excalidraw, Outliner, and Linter ship as plugin binaries so they can be enabled after opening the vault and turning off Restricted Mode.

## Features

| Feature | What you get |
| --- | --- |
| Numbered PARA layout | Twelve roots; one canonical path per note |
| Zettelkasten split | Source-derived thinking in Literature Notes; self-contained ideas in Permanent Notes |
| Periodic planning | Templater `auto/` notes for year, quarter, month, week, day, and dashboards |
| Agent-readable rules | Nested `AGENTS.md` at vault root, Work, Literature Notes, Saint, Collections, Inbox Legacy, Settings, and Templates |
| Embedded views | Core Bases tables in period templates; Dashboard Overdue needs Dataview |
| Agent Skills | One vendored `obsidian` skill; works in Claude Code, Codex, and Antigravity |
| Empty placeholders | Home and index folders are yours to fill. `90. Settings/05 Bases` ships example `Video.base` and `Books.base`, and `85. Raw/02 Videos` ships one real video note so `Video.base` renders a card immediately. Root `Home.md` is your first table of contents and opens on startup |

## Capture to work

This is a filing model, not an automatic pipeline. Nothing here moves notes for you. Gemini on the web does not get automatic access to this vault.

**Capture** (`00. Inbox`) → **original** (`85. Raw`) · **interpretation** (`30. Literature Notes`) · **idea** (`40. Permanent Notes`) · **work** (`15. Work`)

Keep captured originals in Raw regardless of collector. Create work under a project or area only when the note has an owner. Read [Folders and Placement](90.%20Settings/01%20Guideline/01.%20Folders%20and%20Placement.md) before filing the first note. For writing with a public AI chat, see [Writing and AI](90.%20Settings/01%20Guideline/08.%20Writing%20and%20AI.md).

## Roots

Twelve roots are shipped. `25. Digital Garden` and `60. Saint` ship empty.

| Root | Role |
| --- | --- |
| `00. Inbox` | Unsorted capture |
| `10. Time` | Daily, weekly, monthly, quarterly, yearly, and dashboards |
| `15. Work` | Projects, areas, archive, and tasks |
| `25. Digital Garden` | Refined publishable notes (ships empty) |
| `30. Literature Notes` | Research, reviews, and meetings derived from a source |
| `40. Permanent Notes` | Ideas and principles that stand on their own |
| `50. AI` | AI-generated or synthesized material with no owning project |
| `60. Saint` | Faith and spiritual practice (ships empty) |
| `70. Collections` | People, prompts, MOCs, music, places, organizations, GitHub, channels, flowers |
| `80. References` | Books, papers, and attachments |
| `85. Raw` | Captured external originals |
| `90. Settings` | Rules, templates, home, indexes, bases, and Excalidraw drawings |

`90. Settings/07 Excalidraw` is the canonical folder for drawings and assets.

## Time

Planning hierarchy: **Year → Quarter → Month → Week → Day**. Folder numbers are not that hierarchy.

Daily titles are `YYYY-MM-DD`. Weekly titles are ISO week year `GGGG-WW` plus `W` (example `2026-37W`). Period wikilinks are navigation only. Creating a daily note can create missing dashboards for yesterday, today, and tomorrow; it does not create week, month, quarter, or year notes.

Task notes use `manual/task.template.md` fields `type`, `done`, `gtd`, `project`, `plan`, and `due` (plus date stamps) so Dashboard queries can match them. Formats, ISO weeks, engine mapping, and those fields: [Folders and Placement](90.%20Settings/01%20Guideline/01.%20Folders%20and%20Placement.md) · [Templates](90.%20Settings/02%20Templates/README.md) **Engine setup**.

## Quick start

### Local independent role candidates

The twelve-root source below is unchanged. `candidates/personal.json` and `candidates/knowledge.json` define separate, privacy-filtered **local candidates**, not a published release or an existing-vault installer. Personal keeps ten responsibility roots with Saint under Work/Area; knowledge keeps seven roots with source-grounded Wiki, Queries and Paper Analyses. Neither requires the other.

Reuse the public assets through the explicit file allowlists, without copying a vault, history or whole `.obsidian` directory:

```sh
mkdir -p .gjc/candidate-builds
python3 scripts/export_candidates.py --role personal --output .gjc/candidate-builds/personal
python3 scripts/export_candidates.py --role knowledge --output .gjc/candidate-builds/knowledge
python3 scripts/test_candidates.py
node scripts/test_source_template.js
```

Each output must be absent, even on rerun. The exporter refuses existing directories and never merges a vault. A post-create failure explicitly retains an incomplete, unverified package; inspect it and retry at a new absent output path, never overwrite it. Its exact canonical `candidate-manifest.json` binds filenames, bytes, folders and selected hidden assets; independent privacy review must name that exact hash. Public source examples/history are excluded, not rewritten. Read each output's `README.md` and role rules for standalone manual use. The template test requires Node.js 22+ and runs in CI.

Synthetic existing-vault preservation inputs live in `candidates/fixtures/preservation.json`. They specify additive expectations; they do not prove real onboarding. The reusable `onboard` implementation and first complete ingest/query slice belong to the separately owned skills work. No runtime installation, Sync, deployment or publication is established here.

### Original twelve-root source

1. **Download ZIP (no Git required)**

   On the GitHub repository page, choose **Code → Download ZIP**. Extract the archive. In Obsidian, choose **Open folder as vault** and select the extracted folder that contains `.obsidian` and the numbered roots.

   Open it as a **new** vault. Do not merge these files into an existing vault.

   Keep the hidden `.obsidian` folder. Show hidden files to check it; if it was omitted, extract the ZIP again with a tool that retains dotfolders. It contains portable settings and the six explicitly shipped community-plugin binaries.

2. **Optional: clone with Git**

   ```sh
   git clone https://github.com/GoBeromsu/Obsidian-template.git
   ```

   Open the cloned folder as a new vault the same way. Copying the directory works the same way.

3. **Write Markdown first; install plugins when you need them**

   A plain Markdown lesson works with no community plugins. Install community plugins from **Settings → Community plugins** only when you need them. [Templater](https://github.com/SilentVoid13/Templater) is required when using the `auto/` folder templates or inserting `manual/` templates. Install Dataview if you want the Dashboard Overdue query. IDs in `community-plugins.json` are not installations.

4. **Confirm engine setup (when using templates)**

   Core Daily notes is enabled. Templater folder templates for daily, weekly, monthly, quarterly, and yearly notes ship as `data.json` (not plugin binaries). Follow [Templates](90.%20Settings/02%20Templates/README.md) **Engine setup**. Core Bases is already enabled.

5. **Capture, then file**

   Read [Folders and Placement](90.%20Settings/01%20Guideline/01.%20Folders%20and%20Placement.md) first. Drop unsorted capture into `00. Inbox`. Create work under `15. Work/01 Project` or `15. Work/02 Area` when a note has an owner. Keep system files in `90. Settings`.

These steps are setup instructions, not a claim that periodic creation, Bases views, or theme appearance were end-to-end verified in Obsidian.

## First lesson

One short path after the vault is open. Details: [Writing and AI](90.%20Settings/01%20Guideline/08.%20Writing%20and%20AI.md).

1. Before writing, read [Beginner syntax](90.%20Settings/01%20Guideline/08.%20Writing%20and%20AI.md#beginner-syntax): six Markdown basics and a tiny example.
2. Edit [`Me.md`](Me.md) at the vault root. It is one worksheet with five `##` sections: **Summary Statement** (who you are, what you're doing now), **First Principles** (the values or judgment standards you use), **How I Think** (when and how you use thinking methods — bottom-up, top-down, and first-principles reasoning are optional examples, not prescribed steps or fixed beliefs), **Working Preferences** (how you want AI to collaborate with you), and **나에게 영향을 주는 사람** (names only of the people who influence you — no essays, no names supplied by default). It is the only canonical `Me` note. Use generic facts. Do not put secrets, credentials, or machine paths in it.

   Each section opens with a `> 역할:` line describing what to write. Write your answer underneath it, in your own words. After filling the sections in, set `authorship: mixed` in the frontmatter (keep `created_by: agent`).
3. Share **only sanitized excerpts** with Gemini on the web. Paste text yourself. Gemini does not get automatic access to this vault.
4. Ask Gemini to ask you **exactly three** clarifying questions and wait. Answer them, then request a draft. Review it yourself and save **only accepted** answers into the relevant `Me.md` sections by hand.
5. Build your own Map of Content (MOC) in `70. Collections/03 MoC`: pick existing notes related to what you just wrote in `Me.md` and link each one with a short reason. This is a human-curated table of contents, not a generated index or a project hub.

Treat filled `Me.md` and any linked notes as private. They are **not automatically excluded from Git or sharing**; do not push them to a public repository.

### Three files, three roles

[`Me.md`](Me.md) holds your identity and preferences as a person. [`AGENTS.md`](AGENTS.md) holds this repository's rules. [`CLAUDE.md`](CLAUDE.md) is a simple pointer to those two files; it does not duplicate either one's content. Agents read root `Me.md` first for user context, then the applicable `AGENTS.md` contract. Reading `Me.md` does not grant automatic integration or expanded authorization, and an empty section is unfilled and unknown, not a fact about the adopter.

## Agent guidelines

Read the nearest contract before creating or moving a note. README, `08. Writing and AI`, and `09. Agent Skills` ship as English/Korean pairs; neither language outranks the other. The eleven operational guides are single-language.

| Layer | Role |
| --- | --- |
| [Vault](AGENTS.md) | Twelve-root map and vault-wide conventions |
| [Work](15.%20Work/AGENTS.md) | Project, area, archive, and task contracts |
| [Literature Notes](30.%20Literature%20Notes/AGENTS.md) | Source-derived research, reviews, and meetings |
| [Saint](60.%20Saint/AGENTS.md) | Faith and spiritual-practice notes |
| [Collections](70.%20Collections/AGENTS.md) | People, prompts, MOCs, and other catalog objects |
| [Inbox Legacy](00.%20Inbox/09%20Legacy/AGENTS.md) | Legacy capture under Inbox |
| [Settings](90.%20Settings/AGENTS.md) | Placement SSOT, empty home/index/bases, settings-layer rules |
| [Templates](90.%20Settings/02%20Templates/AGENTS.md) | `auto/` vs `manual/`, title formats, navigation vs creation |

## Guidelines

Operational guides live in [`90. Settings/01 Guideline/`](90.%20Settings/01%20Guideline/). They are single-language. Guideline number `07` is intentionally absent (machine-specific).

| Guide | Role |
| --- | --- |
| [00. Guideline Authoring](90.%20Settings/01%20Guideline/00.%20Guideline%20Authoring.md) | How to write and update guidelines and `AGENTS.md` |
| [01. Folders and Placement](90.%20Settings/01%20Guideline/01.%20Folders%20and%20Placement.md) | Physical folder homes and note placement |
| [02. Properties](90.%20Settings/01%20Guideline/02.%20Properties.md) | Frontmatter, types, and authorship |
| [03. Agent Permissions and Workflows](90.%20Settings/01%20Guideline/03.%20Agent%20Permissions%20and%20Workflows.md) | Zones, authorization, and work records |
| [04. Applications and Integrations](90.%20Settings/01%20Guideline/04.%20Applications%20and%20Integrations.md) | Apps, plugins, Git, and GitHub |
| [05. Writing Style](90.%20Settings/01%20Guideline/05.%20Writing%20Style.md) | Prose and Markdown presentation |
| [06. Knowledge Compile Guideline](90.%20Settings/01%20Guideline/06.%20Knowledge%20Compile%20Guideline.md) | Compiling wiki and terminology from sources |
| [12. DEVONthink Guideline](90.%20Settings/01%20Guideline/12.%20DEVONthink%20Guideline.md) | DEVONthink archive and capture routing |
| [15. Templates](90.%20Settings/01%20Guideline/15.%20Templates.md) | Template categories, routes, and engine |
| [16. MOC](90.%20Settings/01%20Guideline/16.%20MOC.md) | Maps of Content and note relationships |
| [17. Research Evidence](90.%20Settings/01%20Guideline/17.%20Research%20Evidence.md) | Evidence grades for research notes |

<details>
<summary>Plugins, theme, and setup limits</summary>

`.obsidian/community-plugins.json` lists plugin **IDs** only. Plugin IDs and shipped `data.json` are config, not installations. Confirm `.obsidian/plugins/` for binaries (`main.js`, `manifest.json`); do not treat a plugins directory or `data.json` as proof that plugin packages are installed.

`.obsidian/appearance.json` sets `cssTheme` to `Minimal` and enables two shipped snippets under `.obsidian/snippets/`. There is no `.obsidian/themes/` directory. Install [Minimal](https://github.com/kepano/obsidian-minimal) yourself if you want that theme, or change the theme. `obsidian-minimal-settings` is an ID only.

`.obsidian/core-plugins.json` enables core Bases, core Templates, and **Daily notes**. `.obsidian/daily-notes.json` is shipped (folder `10. Time/01 Daily Notes`, format `YYYY-MM-DD`, template empty so Templater applies). Templater folder templates for Daily, Weekly, Monthly, Quarterly, and Yearly are in `.obsidian/plugins/templater-obsidian/data.json`. That file is not plugin binaries. Core Templates is not the engine for `<% %>` files.

Excalidraw drawings belong in `90. Settings/07 Excalidraw`. `.obsidian/plugins/obsidian-excalidraw-plugin/data.json` is path config, not an installation. The `periodic-notes` plugin is not in the ID list and is not used.

</details>

<details>
<summary>Periodic links do not cascade</summary>

Wikilinks in the periodic templates are navigation only. There is no automatic period cascade.

The shipped Daily template can create missing dashboards for yesterday, today, and tomorrow. It does not create weekly, monthly, quarterly, or yearly notes. Task fields for Dashboard queries (`type`, `done`, `gtd`, `project`, `plan`, `due`) are in `manual/task.template.md`. See [Templates](90.%20Settings/02%20Templates/README.md) **Engine setup**.

Core Daily notes is enabled and creates daily files only.

</details>
