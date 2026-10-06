---
date_created: 2026-10-03
date_modified: 2026-10-03
status: done
tags:
  - guideline
type: guide

created_by: agent
authorship: agent
---

## Overview

This document owns physical placement and write scope for the knowledge role: which roots exist, what each layer is responsible for, and where a new file may be created. Metadata, provenance, the purpose gate, and existing-file protection stay in [[00 Common Rules]].

- **Covers**
	- the seven roots, the exact wiki children, and the source-type leaves under raw sources
	- which folders accept a new agent-written file, and how local search is scoped
- **Other owners**
	- Provenance, core fields, serialization, capture and ingest consent, and existing-file approval are in [[00 Common Rules]].
	- Personal daily records, personal work, and personal relationship notes belong to the personal role and are not recreated here.

```text
Knowledge Vault
├── 00. Inbox/            — capture awaiting a selected route
├── 10. Raw Sources/      — selected source originals, append-only
│   └── 01 Articles · 02 Videos · 03 Books · 04 Papers · 05 Repositories
│       · 06 Conversations · 07 Mail · 08 KakaoTalk · 09 Clippings
├── 20. Wiki/             — source-derived pages
│   ├── 01 Concepts/      — definitions and reusable concepts
│   ├── 02 Entities/      — source-grounded objects: people, organizations, tools, works
│   ├── 03 Guides/        — procedures compiled from sources
│   ├── 04 Maps/          — entry maps over this vault's own pages
│   ├── 05 Questions/     — open questions and their evidence state
│   └── 06 Personas/      — evidence-backed models of how a documented person reasons
├── 30. Queries/          — synthesized answers to a recorded question
├── 40. Paper Analyses/   — one hub plus detail notes per paper
├── 80. References/       — curated bibliography and attachments
└── 90. Settings/         — guidelines, templates, index
```

## Map

### Root Structure

- **The knowledge role has exactly these seven roots: Inbox, Raw Sources, Wiki, Queries, Paper Analyses, References, Settings.**
	- The layering is source original → derived page → recorded answer, with per-paper analysis as its own responsibility.
	- A machine-readable declaration of this structure is a projection of this document, not a second owner of it.
- **`20. Wiki` has exactly six children: `01 Concepts`, `02 Entities`, `03 Guides`, `04 Maps`, `05 Questions`, `06 Personas`.**
	- Do not add a seventh child, and do not create a subfolder inside one of them; each child stays flat.
	- Changes to that fresh default require an explicit structure change; folder count is not a note or analysis quota.
	- A page that fits none of the six is not a wiki page yet; keep it in `00. Inbox` until its kind is decided.
- **The source-type leaves under `10. Raw Sources` are the proposed set, not a closed list.**
	- Proposed: `01 Articles`, `02 Videos`, `03 Books`, `04 Papers`, `05 Repositories`, `06 Conversations`, `07 Mail`, `08 KakaoTalk`, `09 Clippings`.
	- A capture whose source type has no leaf stays in `00. Inbox` until a leaf is approved; do not invent a leaf to file it.

### Scope of the Vault

- **This vault serves every activity that compiles knowledge from sources, not research alone.**
	- Writing, teaching, software development, consulting, faith study, and community work all produce source-derived pages here.
	- A sermon's cited commentary, a client engagement's reference material, and a paper are the same kind of input and get the same treatment.
- **The subject matter does not change the layering.**
	- A captured original stays an original, a derived page stays derived, and the purpose recorded at ingest stays with the note.

### Raw Sources

- **`10. Raw Sources` holds the original of a source the user selected, placed in the leaf for its type.**
	- The capture is the verbatim original with its provenance fields; see [[00 Common Rules#Source Boundaries]].
- **Growth is append-only: new captures, never rewrites.**
	- Do not edit, reformat, retitle, translate, summarize in place, or inject links into a captured body.
	- A better extraction of the same source is a new capture that records what the earlier one missed; see [[#Raw Sources Are Append-Only]].

### Wiki

- **`20. Wiki` is the source-derived layer, not an agent-authorship zone.**
	- A page belongs here because its content derives from captured sources, whoever wrote it; see [[#The Wiki Axis Is Source, Not Author]].
	- Who wrote it is recorded in provenance per [[00 Common Rules#Permission and Provenance]].
- **`01 Concepts` holds definitions and reusable concepts together.**
	- There is no separate terminology folder; a term's definition and the concept page are the same note.
- **`02 Entities` holds source-grounded objects: people, organizations, tools, works, and places as documented by sources.**
	- An entity page records what sources state about the object, with citations. It is not a relationship record, and it does not replace the personal role's people notes.
- **`03 Guides` holds procedures compiled from sources, with each step traceable to the source that supports it.**
- **`04 Maps` holds entry points over this vault's own pages.**
	- Build a map from pages that exist here; do not copy or mirror a personal map, and do not generate a map that links mostly to pages that do not exist.
- **`05 Questions` holds open questions with their current evidence state.**
	- A question records what is known, what is missing, and which sources bear on it. It is not a task, a plan, or an assignment; see [[#Questions Are Not Tasks]].
- **`06 Personas` holds an evidence-backed model of how a documented person reasons.**
	- Every claim cites a source that person actually produced. A persona is not a runtime profile, an agent personality, or a configuration; see [[#Personas Are Not Runtime Profiles]].

### Queries and Paper Analyses

- **`30. Queries` holds a synthesized answer to a recorded question.**
	- Keep the question, the answer, and the pages or sources the answer rests on in the same note.
	- A substantial answer may be saved and gaps or conflicts may lead to authorized Wiki strengthening. Enumerate the actual target diff and preserve original-source anchors; the answer is not new independent evidence.
- **`40. Paper Analyses` holds one folder per paper: a hub note plus its detail notes.**
	- The hub carries the paper's provenance, the purpose recorded at ingest, and the use context — who it is for and where the result gets reused.
	- Detail notes carry the per-section analysis and stay linked to the hub.
	- A concept that is reusable beyond the paper belongs in `20. Wiki/01 Concepts` and is linked from the hub, not duplicated into it.
	- Personal reading, meaning and decisions stay personal. A source analysis can contain the user's purpose, research question and use context without becoming a personal Literature Note; do not force mixed notes apart.

### Write Scope

- **A new agent-written file is allowed in `00. Inbox`, `10. Raw Sources`, `20. Wiki`, `30. Queries`, and `40. Paper Analyses`, for an authorized knowledge output the user selected.**
	- Selection and the stated purpose come first; see [[00 Common Rules#Capture and Ingest]] and [[00 Common Rules#Purpose Gate]].
	- Zone permission covers a new file only.
- **`80. References` and `90. Settings` require user approval for each file.**
	- Curated bibliography, attachments, guidelines, templates, and index notes stay under the user's control.
- **Editing anything that already exists is governed by [[00 Common Rules#Existing Vault Changes]], in every root, including the writable ones.**

### Local Search

- **Search this vault's own layers: wiki pages, recorded queries, and paper analyses, with selected raw originals as supporting evidence.**
	- Start from derived pages, and open a raw original when a claim needs its exact wording.
- **Do not mix corpora automatically.**
	- Another vault, another account's data, or an external index is not part of this search scope; see [[#No Automatic Corpus Mixing]].
	- No counterpart is required or created; follow [[00 Common Rules#Operations and Tools]].
- **Mention another vault's note only through an explicitly authorized real link.**
	- The user names the target, the target note actually exists, and the link resolves to that exact note.
	- Do not infer a counterpart path, and do not leave a link to a note that was never created.

## Rules

- Check that a new note landed in one of the seven roots and that `20. Wiki` still has exactly its six children.
- Check that a capture sits in a declared source leaf, or stayed in `00. Inbox` because no leaf applies.
- Check that no captured original was modified and that a re-extraction was added as a new capture.
- Check that a wiki page was placed by what its content derives from, with provenance recorded separately.
- Check that a persona claim cites that person's own documented output, and that a question note contains no assigned work.
- Check that a paper hub records provenance, the stated purpose, and the use context, and that reusable concepts live in the concepts folder.
- Check that `80. References` and `90. Settings` files exist only because the user approved them.
- Check that a search answer cites only this vault's pages and its selected raw originals, with any cross-vault link explicitly authorized and resolvable.

## Caveats

### The Wiki Axis Is Source, Not Author

A page is a wiki page because it derives from captured sources, and a note is personal because it carries personal meaning. Authorship is a separate record. A page the user wrote by hand from three captured articles still belongs in `20. Wiki`; a decision an agent drafted about the user's own work does not belong here at all. Deciding placement from who typed it produces a vault where the layers no longer mean anything.

### Raw Sources Are Append-Only

A captured original is the evidence that every derived page rests on, so editing it invalidates the pages that cite it. Improving an extraction, fixing an encoding problem, or adding a missing transcript is a new capture that records what the earlier one lacked, with both kept. If the earlier capture is wrong in a way that matters, say so in the new capture rather than silently replacing the old text.

### Questions Are Not Tasks

A question note tracks the state of knowledge: what sources say, where they disagree, and what evidence is missing. It is not a work item, it carries no owner or due date, and answering it is not a commitment. Keep planning and task tracking in the role that owns personal work, and let a question note change only when the evidence changes.

### Personas Are Not Runtime Profiles

A persona page models how a documented person reasons, and every claim traces to something that person produced. It is not an agent personality, a system prompt fragment, a user profile, or a runtime configuration, and it must never be inferred from private interaction history, speculation about motive, or an impression formed while working. Without citable output from that person, there is no persona page.

### No Automatic Corpus Mixing

This vault answers from what it contains. Pulling in another vault, a personal archive, a mailbox, or an external index because it might help produces answers that cannot be checked and leaks content across boundaries the user set deliberately. Widen the corpus only when the user names the source for that request, and say which corpus an answer came from.

### Standing Alone Without a Personal Vault

Capture, derivation, querying, and paper analysis are complete inside these seven roots. No page, link, or folder here depends on a personal vault existing, and nothing waits for one to be created. If a personal vault is also in use, the link between them is optional, explicit, and per note.
