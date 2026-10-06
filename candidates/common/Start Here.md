---
type: guide
created_by: agent
authorship: agent
tags:
  - guideline
date_created: 2026-10-03
date_modified: 2026-10-03
status: todo
---
# Independent Role Candidate

이 폴더는 개인정보를 제외한 **로컬 정적 역할 후보**입니다. 루트 선언은 `90. Settings/04 Index/folder-structure.json`, 현재 역할의 책임과 배치는 [[01 Role Placement]]에서 확인합니다. 상대 볼트 없이 이 폴더만 Obsidian으로 열어 기본 Markdown, 로컬 탐색, Canvas와 Bases를 사용할 수 있습니다.

## Fresh Vault

1. 후보 manifest의 해시와 독립 privacy 검토의 해시가 같은지 확인합니다.
2. 비어 있는 새 볼트 용도로만 이 독립 폴더를 선택합니다.
3. [[Me]]의 빈 맥락을 자신의 비공개 설치본에서 채웁니다.
4. [[00 Common Rules]]와 [[02 Native Usage]]를 읽고 필요한 기능만 직접 사용합니다.

Templater와 기타 플러그인의 바이너리는 공개 upstream 자산을 명시적으로 선택한 것입니다. 설정 및 파일 존재는 실제 앱 실행 검증이나 안전성 인증이 아닙니다. 신뢰할 수 있는 플러그인만 활성화합니다. Sync는 구성하지 않습니다.

## Existing Vault

기존 볼트에 이 폴더 전체를 병합하거나 복사해 덮어쓰지 않습니다. 기존 노트, 혼합 저작, 원문, 첨부, 설정, 보고서, Git 이력과 기계 복구 기록을 그대로 보존해야 합니다. `90. Settings/04 Index/onboard-expectations.json`은 이를 검증할 **명시적 synthetic fixture와 예상 보호 목록**이지 실행 결과가 아닙니다.

실제 재사용 가능한 `onboard`와 첫 자료 ingest/query 구현은 별도 스킬 소유 작업에서 완성합니다. 그 구현은 이 후보 해시를 입력으로 받고, 새 볼트와 기존 볼트를 구분해 기존 볼트의 exact allowlist/diff/hash 승인만 적용해야 합니다. 이 후보에는 초기화기, 호환 라우터, 런타임 스킬 설치본이 없습니다.

## Privacy and Verification

`candidate-manifest.json`은 모든 내보낸 파일의 이름·바이트 해시·크기와 폴더를 결정적으로 나열합니다. 원본 저장소의 공개 예제 노트, 개인 내용, `.git` 이력, 숨김 런타임 상태, 전체 `.obsidian` 복제는 내보내지 않습니다. `.obsidian`의 명시적 안전 설정과 공개 플러그인 자산만 포함합니다.

정적 패키지 검증은 실제 스킬 로드, source-to-query 행동, 기존 볼트 onboarding 성공, host Sync 또는 공개 배포 승인을 대신하지 않습니다. 기본 검색·백링크·그래프는 현재 볼트 안에서만 동작합니다.
