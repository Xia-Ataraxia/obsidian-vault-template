---
aliases:
  - 네이티브 기능 사용
  - Native Usage
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

이 문서는 두 역할 export 가 함께 가져가는 Obsidian native 기능과 번들 asset 의 사용 범위를 정한다. 어떤 기능이 설정으로 켜져 있고, 무엇이 binary 로 실제 들어 있고, 무엇을 채택자가 직접 확인해야 하는지 구분하는 것이 목적이다.

- **다루는 것**
	- core plugin 으로 켜 둔 기능, 번들 plugin binary, 역할별 route 와 template, Excalidraw 정본 경로
- **다루지 않는 것**
	- 필드·속성·편집 권한은 [[00 Common Rules]] 가 담당한다.
	- root 목록과 폴더 생성은 [[01 Role Placement]] 가 담당한다.
	- 이 문서는 그 두 계약을 요약하거나 역할별 사본으로 다시 적지 않는다.

```text
Native Usage
├── Two Exports — personal 10 roots / knowledge 7 roots, 각각 단독 동작
├── Native Capabilities — core-plugins.json 의 설정값과 실행 확인의 구분
├── Plugin Binaries — 번들 6개 binary 와 설정 ID 목록의 차이
├── Personal Routes — Time·Daily·Dashboard 자동 경로
├── Manual Templates — 모달 insert 와 Bases 속성 쌍
└── Excalidraw & Snippets — 정본 경로와 수동 활성화
```

## Map

### Two Exports

- 두 export 는 각각 단독으로 열리는 별개의 vault 다.
	- personal export 는 10개 root 로 열린다.
	- knowledge export 는 7개 root 로 열린다.
	- 한쪽을 쓰기 위해 다른 쪽을 설치하거나 참조할 필요가 없다.
- personal export 의 구조 차이는 두 가지다.
	- `60. Saint` root 는 두지 않고, 같은 내용은 `15. Work/02 Area/Saint` 에 둔다.
	- `50. AI` root 는 포함하지 않는다.
- knowledge export 에는 `10. Time` 이 없다.
	- period note route 와 dashboard 자동 생성을 두지 않는다.
	- daily note 는 `00. Inbox` 로 떨어진다.
- 두 export 사이에 wikilink, embed, 공유 파일로 의존을 만들지 않는다.
	- 같은 파일을 쓸 때도 각 export 가 자기 사본을 가진다.

### Native Capabilities

| 기능군 | core plugin | 두 export 공통 |
|---|---|---|
| 탐색 | `file-explorer`, `switcher`, `global-search`, `bookmarks`, `tag-pane` | 켜 둠 |
| 관계 | `backlink`, `outgoing-link`, `graph`, `page-preview` | 켜 둠 |
| 구조 | `outline`, `footnotes`, `note-composer`, `word-count` | 켜 둠 |
| 데이터 | `properties`, `bases`, `canvas` | 켜 둠 |
| 실행 | `command-palette`, `slash-command`, `workspaces`, `webviewer` | 켜 둠 |
| 복구 | `file-recovery` | 켜 둠 |
| 주기 | `daily-notes`, `templates` | 켜 둠 |
| 미사용 | `sync`, `publish`, `slides`, `audio-recorder`, `random-note`, `zk-prefixer`, `markdown-importer`, `editor-status` | 원본과 같이 꺼 둠 |

- `core-plugins.json` 은 두 역할에 같은 파일로 들어간다.
	- Canvas, Bases, search, backlink, graph, properties, file recovery, editor 기능을 역할 축소를 이유로 끄지 않는다.
	- `sync` 와 `publish` 는 원본과 같이 꺼진 상태다. Obsidian Sync 나 Publish 를 쓴다고 전제하지 않는다.
- `true` 는 **설정값** 이고 실행 확인이 아니다.
	- 해당 기능이 채택자의 Obsidian 버전에서 실제로 뜨는지는 앱을 열어 확인한다.
	- `bases`, `webviewer`, `slash-command` 처럼 뒤에 추가된 항목은 구버전에서 무시된다.
	- 이 문서는 파일에서 읽은 설정값만 기록한다. 앱에서 end-to-end 로 실행했다고 주장하지 않는다.

### Plugin Binaries

- binary 로 함께 가는 community plugin 은 6개다.
	- Templater, Homepage, Omnisearch, Excalidraw, Outliner, Linter.
	- 각 plugin 의 `main.js`, `manifest.json`, `styles.css` 만 복사한다.
	- plugin 폴더를 통째로 복사하지 않는다. cache, 로그, 로컬 상태 파일은 가져가지 않는다.
- `data.json` 은 설정이며 plugin 설치가 아니다.
	- Templater, Homepage, Excalidraw 의 `data.json` 은 역할별로 안전한 최소 키만 쓴다.
	- 계정·네트워크·호스트 경로·API 토큰·workspace 상태·hotkey 는 어느 역할에도 넣지 않는다.
- `community-plugins.json` 의 ID 목록은 설치 증거가 아니다.
	- 목록에는 binary 가 없는 ID 도 있다. 그 plugin 은 채택자가 직접 설치할 때까지 로드되지 않는다.
	- Dataview 가 그 예다. Caveats 의 Overdue 항목을 본다.

### Personal Routes

| route | 설정 위치 | 값 |
|---|---|---|
| daily note 폴더 | `.obsidian/daily-notes.json` | `10. Time/01 Daily Notes` |
| daily note 파일명 | `.obsidian/daily-notes.json` | `YYYY-MM-DD` |
| template 루트 | Templater `data.json` | `90. Settings/02 Templates` |
| folder template | Templater `data.json` | Daily · Weekly · Monthly · Quarterly · Yearly |

- Dashboard 는 folder template 이 아니다.
	- Daily 템플릿이 모든 템플릿 실행 후 hook 에서 어제·오늘·내일 dashboard 를 없을 때만 만든다.
	- `10. Time/06 Dashboard` 에 folder template 을 추가하면 같은 파일이 두 번 처리된다.
- knowledge export 의 Templater 는 자동 적용을 쓰지 않는다.
	- `trigger_on_file_creation_mode` 는 `none`, `folder_templates` 는 빈 목록이다.
	- `auto/` 템플릿 6개는 knowledge export 에 포함하지 않는다.
- knowledge 의 daily note 는 capability 만 남긴다.
	- 폴더는 `00. Inbox`, 파일명은 `YYYY-MM-DD` 다.
	- Time root 를 되살리거나 period note 를 자동 생성하지 않는다.

### Manual Templates

| template | personal | knowledge | 비고 |
|---|---|---|---|
| `manual/note.template.md` | 포함 | 포함 | 범용 insert |
| `manual/source.template.md` | 포함 | 포함 | 공용 source insert |
| `manual/book.template.md` | 포함 | 포함 | `80. References/01 Book` |
| `manual/guideline.template.md` | 포함 | 포함 | 가이드 작성 frame |
| `manual/task.template.md` | 포함 | 제외 | `15. Work` 의존 |
| `manual/project.template.md` | 포함 | 제외 | `15. Work` 의존 |
| `manual/log.template.md` | 포함 | 제외 | project hub 쌍 |
| `manual/video.template.md` | 포함 | 제외 | `85. Raw/02 Videos` 의존 |

- insert 는 Templater 모달에서 사람이 실행한다.
	- 템플릿은 파일이나 폴더를 만들지 않는다. Daily 템플릿의 dashboard hook 만 예외다.
	- `source.template.md` 는 묻는 값을 프런트매터에만 쓰고, 원문은 사용자가 직접 붙여넣는다.
- Bases 와 속성 이름은 한 쌍으로 유지한다.
	- `Books.base` 는 `author`, `status`, `total_page`, `cover_url` 을 읽는다. 두 역할에 포함한다.
	- `Video.base` 는 `author`, `date_published`, `image` 를 읽는다. personal 에만 포함한다.
	- 속성 이름을 바꾸면 view 가 조용히 빈다. 이름을 바꾸기 전에 두 쪽을 함께 확인한다.
- knowledge 에서 제외한 template 은 경로 의존 때문이다.
	- `video.template.md` 는 본문 주석이 `85. Raw/02 Videos` 를 가리키고 knowledge 에는 그 root 가 없다.
	- 제외한 template 을 경로만 바꿔 되살리지 않는다. 필요하면 담당 문서에서 route 를 먼저 정한다.

### Excalidraw & Snippets

- 두 역할 모두 `90. Settings/07 Excalidraw` 를 Excalidraw 정본 경로로 쓴다.
	- library, script, CJK font 경로도 그 아래에 둔다.
	- JavaScript 파일 허용과 onload script 는 꺼 둔다.
- CSS snippet 두 개는 파일만 복사된다.
	- `appearance.json` 은 포함하지 않는다. `cssTheme` 가 가리키는 Minimal theme binary 를 함께 보내지 않기 때문이다.
	- 그래서 `fix-nested-bullets` 와 `mermaid-wide` 는 Appearance 설정에서 직접 켠다.
	- snippet 이 꺼져 있어도 노트 내용은 바뀌지 않는다. 중첩 bullet 과 Mermaid 폭의 표시만 기본값으로 보인다.

## Rules

- 설정 파일이나 template 을 고치기 전에 [[00 Common Rules]] 와 [[01 Role Placement]] 를 읽는다.
- binary 가 없는 plugin 기능을 전제로 노트·template·Bases view 를 만들지 않는다.
- `core-plugins.json` 에서 Canvas, Bases, search, backlink, graph, properties, file recovery, editor 항목을 끄지 않는다.
- Excalidraw 그림과 plugin asset 은 `90. Settings/07 Excalidraw` 아래에만 둔다.
- knowledge export 에 `10. Time` route 나 period folder template 을 추가하지 않는다.
- 두 export 사이에 파일 공유·링크·복사로 의존을 만들지 않는다.
- 필드·속성·권한 규칙은 이 문서에 다시 적지 않고 [[00 Common Rules]] 로 연결한다.
- 설정값을 근거로 기능이 동작한다고 쓰지 않는다. 확인한 범위를 그대로 적는다.

## Caveats

### 설정값과 앱 확인은 다르다

`core-plugins.json`, `community-plugins.json`, 각 `data.json` 은 모두 파일에서 읽은 설정이다. 이 문서의 모든 "켜 둠" 표기는 그 설정값을 뜻한다.

- 실제 동작 확인은 채택자가 앱에서 한다.
	- plugin 을 켜고, 명령을 실행하고, view 가 뜨는지 본다.
	- 버전이 낮으면 설정에 있는 기능이 조용히 무시된다.
- 이 패키지를 적용했다는 사실이 실행 확인을 대체하지 않는다.

### Dataview Overdue 블록은 선택이다

- `auto/Dashboard.template.md` 의 `## Overdue` 는 `dataview` 코드 블록이다.
	- Dataview binary 는 이 패키지에 없다. `community-plugins.json` 에 ID 가 있어도 설치 증거가 아니다.
	- 설치하지 않으면 그 블록은 쿼리 결과 없이 코드 블록 그대로 보인다. 다른 섹션은 영향받지 않는다.
	- 설치는 채택자 선택이다. 설치하지 않은 상태를 오류로 보지 않는다.
- Dataview 가 있다고 전제한 블록을 새로 만들지 않는다.
	- Dashboard 의 Tasks 와 Timeline 은 core Bases 의 `base` 블록이다. Dataview 와 무관하다.

### onboard 와 ingest 는 아직 구현되지 않았다

- 이 패키지는 정적 asset 과 설정 후보다.
	- 실행되는 onboard, ingest, query 동작은 들어 있지 않다.
	- skill 과 onboard 구현은 별도 스킬 작성 정본의 책임이다.
- 이 문서는 그 동작을 설명하거나 보장하지 않는다.
	- `source.template.md` 도 사람이 실행하는 insert 이며 자료 수집 구현이 아니다.

### 런타임·계정 설정은 포함하지 않는다

- Obsidian Sync, Publish, 서비스 계정, 네트워크 설정, 호스트 경로, hotkey, workspace 상태는 어느 역할에도 넣지 않는다.
- Homepage 는 `autoCreate: false` 로 둔다.
	- 대상은 두 역할 모두 `90. Settings/03 Home/Home.md` 다.
	- 그 파일과 폴더는 [[01 Role Placement]] 의 manifest 가 제공한다.
	- 경로를 바꾸면 시작 시 Notice 만 뜨고 다른 기능은 영향받지 않는다.
- 이 문서는 설치·인증·동기화 절차를 다루지 않는다.
