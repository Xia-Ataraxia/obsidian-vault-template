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

This document owns physical placement and write scope for the personal role: which roots exist, what each one is responsible for, and where an agent may create a new file. Metadata, provenance, and existing-file protection stay in [[00 Common Rules]].

- **Covers**
	- the ten roots, their responsibility boundaries, and the folders that carry a distinction
	- which of those folders accept a new agent-written file
- **Other owners**
	- Provenance, core fields, serialization, capture and ingest consent, and existing-file approval are in [[00 Common Rules]].
	- Source-derived wiki pages, queries, and per-paper analyses are a knowledge-role responsibility and are not recreated here.

```text
Personal Vault
├── 00. Inbox/            — unsorted capture · 01 Chat · runtime record folders · 08 Unlisted · 09 Legacy
├── 10. Time/             — 01 Daily Notes · 02 Weekly · 03 Monthly · 04 Yearly · 05 Quarterly · 06 Dashboard
├── 15. Work/
│   ├── 01 Project/<Name>/   — work with an end condition: hub · dated logs · supporting notes
│   ├── 02 Area/<Name>/      — ongoing responsibility, same shape as a project
│   │   └── Saint/           — faith practice: 01 Sermon · 02 QT · 03 Pray · 04 Bible · 05 Worship
│   ├── 03 Archive/<Year>/   — inactive items kept for reference
│   └── 04 Tasks/            — tasks with no owning project or area
├── 25. Digital Garden/   — published refinement of a thought note
├── 30. Literature Notes/ — 01 Researches · 02 Reviews · 03 Meetings
├── 40. Permanent Notes/  — refined evergreen insight
├── 70. Collections/      — entity and directory notes: people · prompts · maps · places · organizations · channels
├── 80. References/       — curated bibliography, images, and attachments
├── 85. Raw/              — captured source originals, by source type
└── 90. Settings/         — guidelines, templates, home, index, bases
```

## Map

### Root Structure

- **The personal role has exactly these ten roots: Inbox, Time, Work, Digital Garden, Literature Notes, Permanent Notes, Collections, References, Raw, Settings.**
	- A fresh personal vault creates no top-level AI root and no top-level faith root; faith practice is an area of work, not a separate taxonomy.
	- Place a note in the most specific valid folder, and keep notes out of a parent that has leaves — the Inbox is the exception.
	- A machine-readable declaration of this structure is a projection of this document, not a second owner of it.
- **An existing vault keeps every root it already has.**
	- Retention is the default, including roots this role would not create fresh.
	- Reorganizing existing content into this layout is a live migration and needs its own separately approved exact manifest; see [[#Fresh Structure Is Not a Migration Plan]].

### Work and Saint

- **`15. Work` holds the active responsibilities: projects, areas, archive, and loose tasks.**
	- A project has an end condition; an area does not. Both use one semantic folder per item with a hub note, dated logs, and supporting notes.
	- Archive moves an inactive item under its year; it is reference storage, not a backlog.
- **Faith practice lives as the `Saint` area item and keeps its five leaves: `01 Sermon`, `02 QT`, `03 Pray`, `04 Bible`, `05 Worship`.**
	- Keep the leaves as they are; do not flatten, rename, merge, or renumber them to match another folder's shape.
	- This area is user-only for new files; see [[#Saint Stays Personal]].

### Responsibility, Not Format

- **A folder is chosen by whose meaning the note carries, not by the file's shape.**
	- `30. Literature Notes` holds the user's own thinking about an external source: a research note, a review, or a meeting record.
	- A per-paper structured analysis of a source is a knowledge-role responsibility, so the boundary is responsibility rather than format.
	- `40. Permanent Notes` holds the refined insight that no longer depends on the source; `25. Digital Garden` holds the published version of such a note, which is a separate note rather than a copy.
- **A note that mixes personal judgment with source notes stays one note.**
	- Do not split, move, or duplicate it to satisfy a cleaner taxonomy; see [[#Mixed Notes Are Not Split]].

### Collections, People, and Personas

- **`70. Collections` holds entity and directory notes, and `80. References` holds curated bibliography and attachments.**
	- A people note records a real relationship: who they are, shared history, and the notes that link back to them.
	- A map note is the user's own navigation over personal notes; it is not generated from a source corpus.
- **An entity record and a persona model are different artifacts.**
	- A persona — an evidence-backed model of how a documented person reasons, built from cited sources — is a knowledge-role artifact and does not replace or extend a personal people note.
	- Do not convert a people note into a persona, and do not store a persona as a people note.

### Agent Write Scope

- **A new agent-written file is allowed only in these places.**
	- `00. Inbox` — any subfolder, including the runtime record folders when a record is warranted under [[00 Common Rules#Records and Runtime Originals]].
	- `15. Work` — projects, areas, archive, and tasks, except the `Saint` area item.
	- `10. Time/01 Daily Notes` — only with an agent identifier suffix in the filename, so the user's dated note is never the target; see [[#Daily Notes Need an Agent Suffix]].
	- `85. Raw` — a captured original for a source the user selected, placed in the leaf for that source type.
- **Every other root is user-only for new files, absent an explicit request.**
	- This includes the remaining `10. Time` folders, `25. Digital Garden`, `30. Literature Notes`, `40. Permanent Notes`, `70. Collections`, `80. References`, and all of `90. Settings`.
	- An explicit request authorizes that named file only, and the result records provenance honestly per [[00 Common Rules#Permission and Provenance]].
- **Editing anything that already exists is governed by [[00 Common Rules#Existing Vault Changes]], in every root, including the writable ones.**
	- Zone permission covers new files; it never covers an existing file.
- **A captured original in `85. Raw` is immutable once captured.**
	- Do not rewrite, reformat, retitle, translate, or inject links into the captured body. Interpretation belongs in the note that interprets it.
- **No write happens as a side effect of a session.**
	- Do not open a daily note, a log, or a record just because work occurred; follow [[00 Common Rules#Records and Runtime Originals]].

### Standing Alone

- **Every responsibility here works without a knowledge vault.**
	- Capture, time, work, collections, references, literature notes, and permanent notes are complete on their own.
	- A selected local reference or a source original captured for personal use lives here; needing one does not require a second vault, an export, or a sync.
- **No counterpart note is created anywhere.**
	- Follow [[00 Common Rules#Operations and Tools]]: no paired notes, no automatic cross-vault graph, and no link to a vault that was not explicitly authorized.

## Rules

- Check that a new note landed in the most specific valid folder among the ten roots, and that no new root was introduced.
- Check that `Saint` kept its five leaves and received no agent-written file.
- Check that an agent-written daily note carries an agent suffix and did not touch the user's dated note.
- Check that a `85. Raw` capture is the unmodified original of a source the user selected.
- Check that a note outside the agent write scope exists only because the user asked for that exact file.
- Check that an existing file was changed only with the approval described in [[00 Common Rules#Existing Vault Changes]].
- Check that a mixed personal note was neither split nor moved to tidy the taxonomy.
- Check that no record or dated note was created merely because a session ran.

## Caveats

### Saint Stays Personal

Faith practice sits inside `15. Work/02 Area/Saint` because it is an ongoing personal responsibility, not because it is a work deliverable. The surrounding area folders accept agent-written files; this one does not. Reflection, prayer, and study notes are written by the user, and an agent contributes only to a file the user names explicitly.

### Fresh Structure Is Not a Migration Plan

A fresh vault built on these ten roots says nothing about where an existing vault's content should move. An existing AI root, faith root, or any other legacy folder is retained as it is. A move, merge, or rename of existing content requires its own approval with exact paths, current hashes, and the proposed result, as described in [[00 Common Rules#Existing Vault Changes]] — selecting this role does not approve it, and neither does a structure check that reports the difference.

### Daily Notes Need an Agent Suffix

The user's dated note is a personal record, and a second writer in the same file destroys that record silently. An agent writing in `10. Time/01 Daily Notes` keeps the date and appends an agent identifier to the filename, so the two files sit side by side and neither overwrites the other. Without a usable identifier, write nothing there and report the gap.

### Mixed Notes Are Not Split

A literature note that carries both source notes and the user's own conclusion is doing exactly what it should. Splitting it into a source part and a thinking part destroys the connection that made it worth writing. Keep it in place, and separate the sections inside the note per [[00 Common Rules#Source Boundaries]].

### Agent Participation Does Not Transfer Ownership

Personal decisions, prose, meaning, and work stay personal no matter how much of the drafting an agent did. A note marked as having mixed authorship is still a user-created note: it keeps the user's creator value, it keeps requiring approval for the next edit, and it never becomes an agent-owned working file.
