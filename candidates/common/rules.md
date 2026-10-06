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

This document is the single source for the rules every role shares: write permission, provenance, core metadata, the purpose gate, value serialization, source boundaries, capture and ingest consent, protection of existing records, and approval for changes to an existing vault.

- **Covers**
	- what any writer may change and what proof an existing file requires
	- how provenance, core metadata, and captured values are recorded
	- which outputs require an explicit selection and a stated purpose
- **Other owners**
	- Folder placement and role-specific write scope are in [[01 Role Placement]].
	- Skill procedures, installation, authentication, and runtime operation belong to the adopter's skill repository and infrastructure notes.
- **Single source**
	- [[01 Role Placement]] links to the sections below for metadata and protection instead of restating them.
	- Do not copy a value list from this document into another note; link to the owning section.

```text
Common Rules
├── Permission and Provenance — permission is a separate question from recorded authorship
├── Core Metadata — type · tags · date_created · date_modified, snake_case, quoted YAML
├── Purpose Gate — user_intent_interview before a selected ingest
├── Value Serialization — one JSON/YAML-safe serializer for every captured value
├── Source Boundaries — original · interpretation · purpose · producer
├── Links and Relationships — links to existing notes, never a permission
├── Capture and Ingest — selection and consent, never subscription
├── Records and Runtime Originals — no automatic projection, no silent replacement
├── Existing Vault Changes — additive expectation plus exact allowlist approval
├── Operations and Tools — eleven operation contracts implemented outside this vault
└── Source Grounding — original-source capabilities vs this role's policies
```

## Map

### Permission and Provenance

- **Permission is a separate question from recorded authorship.**
	- `created_by` records who created the note: `user` or `agent`.
	- `authorship` records the authoring character of the body: `user`, `agent`, or `mixed`.
	- Neither field grants, widens, or removes write permission. Write scope stays in [[01 Role Placement]].
- **Preserve a valid creator value.**
	- Keep an existing valid `created_by` through every later edit; it records creation, not the last writer.
	- An approved agent edit of a user-created note keeps `created_by: user` and sets `authorship: mixed`.
	- `mixed` records agent participation in a user-created note. A later edit of that note requires approval again.
- **Prove the exact change before editing an existing file.**
	- This applies whenever provenance reads `user`, `mixed`, is missing, or holds a value outside the allowed list.
	- State the exact path, the current content hash or its recorded absence, and the proposed diff before writing.
	- An approved role, folder, or task does not substitute for that per-path proof.
	- Missing or non-conforming provenance is protected rather than repairable; see [[#Missing Provenance Is Protected]].
- **A wikilink or tool name is never a provenance value.**
	- `created_by: [[claude]]` is a conflict to report. It never becomes valid, and it is never silently normalized to `agent`.
	- Leave the file unchanged and record the conflict for review.

### Core Metadata

- **Every note carries the core fields.**
	- `type`, `tags`, `date_created`, `date_modified`, `created_by`, `authorship`.
	- `status` is a workflow field; add it only where progress tracking is meaningful.
- **Record `type` as one lowercase scalar that names the note's actual kind.**
	- Do not import another vault's type list, and do not invent a parallel role taxonomy to classify the same notes twice.
	- Keep `tags` consistent with `type`, lowercase kebab-case, nested with `/`, and never a parent together with its own child tag.
- **Write YAML that parses the same way everywhere.**
	- Property keys are snake_case; do not add a camelCase or spaced variant of an existing key.
	- Quote a wikilink value (`source: "[[Note]]"`), and never write an empty wikilink.
	- Dates are ISO 8601 `YYYY-MM-DD` plain values, not links.
	- YAML indents with two spaces per level; body nested lists indent with one tab per depth.

### Purpose Gate

- **A selected ingest records `user_intent_interview` before its output is written.**
	- Plain text, one or two lines, in the user's own stated terms.
	- It answers why this source was selected and where the result will be reused.
- **Do not supply the purpose yourself.**
	- Do not infer it from the source, restate the source's own summary, or reuse another note's interview text.
	- Reuse a purpose already explicitly supplied for the selected batch; do not ask the same question again.
	- Without a stated purpose there is no ingest: keep the capture and stop.
- **The recorded answer is evidence, not a deliverable contract.**
	- It does not promise a downstream note, task, or schedule, and it does not authorize writing one.

### Value Serialization

- **Serialize every captured value through one scalar serializer that is valid in both JSON and YAML.**
	- Handle double and single quotes, backslashes, newlines, and leading or trailing whitespace.
	- Encode a newline inside a whole quoted scalar as an escape; its parsed value may contain one or two lines of purpose text.
- **Verify the round trip.**
	- Parse the written file and compare the parsed value with the captured value.
	- Placeholder replacement is not serialization; see [[#Placeholder Substitution Is Not a Serializer]].

### Source Boundaries

- **Keep four things distinct in any note that carries a source.**
	- The original text stays verbatim under its own heading.
	- Interpretation, summary, and judgment live in their own sections and never rewrite the original.
	- The stated purpose stays in `user_intent_interview` rather than inside the quoted text.
	- The producer of the captured text is not the author of the note; `created_by` records who wrote the note.
- **Record external provenance in dedicated fields.**
	- `source_url` holds an external URL; `source` holds an in-vault wikilink.
	- Point to a specific location with a real anchor, heading, page, or timestamp. Do not fabricate an anchor that the source does not have.
- **Reference attachments where they already live.**
	- Link or embed the existing file; do not copy, re-download, or rename it to suit a new note.
- **Record incomplete extraction as a gap.**
	- Name what is missing — paywalled body, truncated transcript, failed OCR, unreachable attachment — at the place where it is missing.
	- Do not fill a gap with a paraphrase and do not leave it silently empty.

### Links and Relationships

- **Link only to a note that exists.**
	- Do not create an empty or stub note so that a link resolves, and do not leave a link to a note nobody intends to write.
- **A link is navigation, not permission.**
	- Reaching a note through a link does not authorize editing it; write scope stays in [[01 Role Placement]] and per-file approval in [[#Permission and Provenance]].
- **Keep relationships out of quoted source text.**
	- Add links in the note that interprets a source, never inside the captured original.
	- Link a concept once at its first mention in the body; leave headings, frontmatter, and code spans unlinked.

### Capture and Ingest

- **A selected capture produces candidates only.**
	- Capturing a source creates its original record and nothing else: no analysis, no wiki page, no task, no link injection.
- **A direct ingest does not require a prior capture.**
	- A source the user selects can be ingested in one step; no staging note is required first.
- **Subscription is not ingest consent.**
	- A feed, mailbox, channel, repository, or chat you follow is not a selection. Each ingest needs its own explicit selection.
- **A captured conversation defaults to original backup only.**
	- A messenger or chat export, KakaoTalk included, stays an original record; an explicitly selected ingest is what may produce analysis, tasks, or wiki output.
	- Message history is never summarized, scored, or turned into tasks as a side effect of capture.

### Records and Runtime Originals

- **Do not write a work record automatically.**
	- Write a human record only when the user explicitly requests that record and its destination is resolved; substantive work alone is not a record request.
	- Preserve any existing record rather than generating one at session end.
- **Do not project runtime state into notes.**
	- Session transcripts, daily roundups, tool logs, and queue state are not note content produced as a side effect of an operation.
- **Preserve existing records and runtime originals unchanged.**
	- Existing work records, captured repository originals, roundups, ledgers, recovery records, and runtime state stay byte-identical outside an approved diff.
	- Query existing runtime state read-only when a selected task needs it.
	- Do not create a new backup, mirror, index, or catalog of runtime state.

### Existing Vault Changes

- **Treat an existing vault as additive-only.**
	- Add nothing on top of an occupied path; refuse the destination instead of merging into it.
- **Approve changes per exact allowlist.**
	- Enumerate exact paths, current bytes or recorded absence, hashes, proposed diffs, and the preservation and recovery expectation for each entry.
	- Choosing a role, structure, or template is not approval of an effect on an existing file.
- **Never replace a file tree.**
	- No whole-tree replacement and no repository-wide substitution across `.md`, `.yml`, `.json`, or `.sh`.
	- Keep existing names, links, and attachments intact; a rename is a change requiring its own approval.

### Operations and Tools

- **Eleven operations have contracts, and implementations elsewhere.**
	- `onboard`, `capture`, `inbox`, `ingest`, `query`, `verify`, `audit`, `lint`, `status`, `reindex`, `refresh-context`.
	- Each is independently invocable and reads the rules it needs; there is no dispatcher that routes them.
	- Recording a contract is not an implementation, install, or execution claim; see [[#A Contract Is Not an Implementation]].
- **Select tools per task.**
	- Use the runtime's and the editor's native features directly rather than wrapping them in a bespoke layer.
- **Let selected sources drive growth.**
	- There is no page quota and no target page count, such as a 300-page goal, that an operation should fill.
- **Require no counterpart.**
	- Do not create a paired note in another vault, and do not build an automatic cross-vault search graph.

### Source Grounding

- **Cite the public reference revision.**
	- [cmds-llm-wiki at 863ca437](https://github.com/johnfkoo951/cmds-llm-wiki/tree/863ca43778e639d96a31f71fb388ee000336d0ff) is the reviewed public original for this role's structure vocabulary.
- **Label original-source capability separately from this role's policy.**
	- Original-source capabilities retained by contract are eleven knowledge operations, selected capture, direct ingest, source-grounded Wiki and query, and Standard/Book/Paper workflows. This citation does not prove their installation or operation here.
	- Policy, as set here: the metadata and provenance contract above, snake_case keys, the selection and consent gates, additive existing-vault approval, and the placement rules in [[01 Role Placement]].
- **Keep the citation honest.**
	- A citation is not an audit of that repository and not evidence about its author's practice or private life.
	- Do not adopt a source convention by resemblance; a differing convention there, such as camelCase keys, does not change the policy above.

## Rules

- Check that every note carries the core fields, snake_case keys, quoted wikilink values, and ISO dates.
- Check that a valid `created_by` survived the edit and that an approved edit of a user note reads `authorship: mixed`.
- Check for exact-path approval with a hash and a diff before any existing file is written.
- Report a wikilink or tool name found in a provenance field instead of correcting it.
- Confirm `user_intent_interview` exists as one or two plain-text lines before an ingest writes anything.
- Confirm a captured value survives a parse round trip, not just a template render.
- Confirm original text, interpretation, and stated purpose are separable in the result, and that extraction gaps are named.
- Confirm no record, roundup, or runtime projection was written as a side effect.
- Confirm every touched existing path appears in the approved allowlist and that nothing else changed.
- State operation contracts as contracts; do not report a skill, onboarding, or install as performed.

## Caveats

### Permission Is Not Provenance

A note created by an agent is not therefore editable, and a note marked `mixed` is not therefore shared property. Read write scope from [[01 Role Placement]] and per-file approval from [[#Permission and Provenance]]; treat the metadata as a record of what happened, not as an authorization.

### Missing Provenance Is Protected

A file with no `created_by`, or with a value outside the allowed list, is the most protected case rather than the least. Do not infer an identity from the folder, the filename, the writing style, or an adjacent note, and do not normalize the value to make a check pass. Leave the file unchanged and report it for review with its exact path.

### Placeholder Substitution Is Not a Serializer

A `{{value}}` or `{placeholder}` replacement, a stream-editor pass, or string concatenation can emit a file that parses while the value is already corrupted — a quote closes the field early, a backslash escapes the next character, a newline silently splits the document. Treat a rendered template as unverified until the written file is parsed and the value compared.

### Capture Is Not Ingest

Capturing more sources does not produce knowledge, and an archive of captures is not a backlog that authorizes later synthesis. A capture ends at the original record; the next step starts only from an explicit selection with a stated purpose.

### A Contract Is Not an Implementation

The operations in [[#Operations and Tools]] are named so that their boundaries are stable. Naming them does not install a command, create a skill, or onboard this vault, and no rule in this document executes itself. Report an operation as available only when the runtime actually provides it.

### No Automatic Enforcement

Everything here is normative guidance for writers, including agents. It is not a guard, a hook, or a validator, and it does not run during a write. A separate installed check may exist in the adopter's runtime, but its absence does not relax these rules and its presence does not replace review.
