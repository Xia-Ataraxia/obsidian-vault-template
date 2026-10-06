<%*
/*
 * 공용 source note insert. 사람이 Templater 모달에서 실행한다.
 * Shared source-note insert, run by a human from the Templater modal.
 *
 * 이 블록은 Templater 실행 블록이며, 자료를 가져오거나 렌더링하지 않는다.
 * 묻는 값은 프런트매터로만 들어가고, 본문 원문은 사용자가 직접 붙여넣는다.
 * 취소하거나 필수 값을 비우면 노트를 만들지 않고 중단한다.
 */
const today = tp.date.now("YYYY-MM-DD");

const reject = (reason) => {
	throw new Error("source.template: " + reason);
};

const askScalar = async (label, initial, multiline) => {
	const answer = await tp.system.prompt(label, initial, false, multiline);
	if (answer === null) {
		reject(label + " 입력을 취소했습니다. 노트를 만들지 않습니다.");
	}
	return answer.trim();
};

const sourceUrl = await askScalar("Source URL", "", false);
if (sourceUrl === "") {
	reject("source_url 은 필수입니다. 빈 값으로는 노트를 만들지 않습니다.");
}

const sourceTypes = ["article", "book", "paper", "video", "repo"];
const sourceType = await tp.system.suggester(sourceTypes, sourceTypes, false, "Source type");
if (sourceType === null) {
	reject("source type 선택을 취소했습니다. 노트를 만들지 않습니다.");
}

const sourceTitle = await askScalar("Source title", tp.file.title, false);
const sourceAuthor = await askScalar("Source author or speaker", "", false);

const intentAnswer = await tp.system.prompt("왜 이 자료를 읽는가 (1-2줄)", "", false, true);
if (intentAnswer === null) {
	reject("user_intent_interview 입력을 취소했습니다. 노트를 만들지 않습니다.");
}
const intentLines = intentAnswer
	.split("\n")
	.map((line) => line.trim())
	.filter((line) => line !== "");
if (intentLines.length === 0) {
	reject("user_intent_interview 는 필수입니다. 빈 값으로는 노트를 만들지 않습니다.");
}
if (intentLines.length > 2) {
	reject("user_intent_interview 는 1-2줄까지만 받습니다. 줄 수를 줄여 다시 실행하세요.");
}
const userIntentInterview = intentLines.join("\n");
-%>
---
aliases: []
title: <% JSON.stringify(sourceTitle) %>
author: <% JSON.stringify(sourceAuthor) %>
source_url: <% JSON.stringify(sourceUrl) %>
user_intent_interview: <% JSON.stringify(userIntentInterview) %>
status: todo
type: <% sourceType %>
tags:
  - reference/<% sourceType %>
created_by: user
authorship: user
date_created: <% today %>
date_modified: <% today %>
---
<!--
Serialization / 직렬화
`title`, `author`, `source_url`, `user_intent_interview` 는 JSON.stringify 로 스칼라 전체를 직렬화한다. 따옴표를 손으로 덧붙이지 않는다. 따옴표·백슬래시·줄바꿈이 섞여도 YAML double-quoted scalar 로 안전하게 들어가고, 줄바꿈은 이스케이프되어 한 줄로 유지된다.
JSON.stringify writes the whole scalar including its own quotes. Never wrap the output in extra quotes; quotes, backslashes, and newlines stay escaped inside one line.

Identity / 식별
`type` 과 `tags` 의 값은 고정 목록에서 고른 값이므로 그대로 쓴다. 필드 규칙은 `00 Common Rules`, 저장 위치는 `01 Role Placement` 를 따른다. 이 insert 는 파일을 옮기지 않는다.

Provenance / 작성 주체
`created_by: user` 와 `authorship: user` 는 사람이 이 모달을 직접 실행했을 때만 맞는 값이다. 사람이 아닌 생산자는 자기 실행에 맞는 값을 쓴다. 모델 이름이나 `[[claude]]` 같은 wikilink 를 작성 주체 필드에 넣지 않는다. 허용값은 `00 Common Rules`, 현재 agent 식별 경계는 루트 `AGENTS.md` 를 따른다. `author` 는 실제 원출처 저자를 기록한다.

Body / 본문
`## Original Content` 는 사용자가 원문을 직접 붙여넣는 빈 영역이다. 비어 있는 상태가 기본이며, 수집에 실패했다는 뜻도 수집했다는 증거도 아니다. 이 템플릿은 `source_url` 을 열지 않고 가져오지도 않는다.
`## Analysis` 에는 읽은 사람의 해석만 쓴다. 원문과 해석을 같은 섹션에 섞지 않는다.
치환은 Templater 실행 블록과 `tp.*` 만 쓴다. Obsidian core Templates 의 중괄호 치환자나 Web Clipper 변수 문법은 이 파일에서 쓰지 않는다.
-->

## Original Content

## Analysis
