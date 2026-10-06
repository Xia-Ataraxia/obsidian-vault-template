// Execute the candidate Templater block with a bounded prompt mock, not an Obsidian runtime claim.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const source = readFileSync(new URL("../candidates/common/source.template.md", import.meta.url), "utf8");
const match = source.match(/^<%\*([\s\S]*?)-%>\n([\s\S]*)$/);
assert.ok(match, "source template has an execution block");
const names = ["sourceTitle", "sourceAuthor", "sourceUrl", "userIntentInterview", "sourceType", "today"];
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const execute = new AsyncFunction("tp", match[1] + `\nreturn {${names.join(",")}};`);

async function run(answers, type = "article") {
  let calls = 0;
  const values = await execute({
    date: { now: () => "2000-01-01" },
    file: { title: "Synthetic source" },
    system: {
      prompt: async () => answers[calls++],
      suggester: async () => type,
    },
  });
  const rendered = match[2].replace(/<%\s*([\s\S]*?)\s*%>/g, (_, expression) =>
    new Function(...names, `return (${expression});`)(...names.map((name) => values[name])),
  );
  return { rendered, values, calls };
}

const intent = 'Synthetic purpose: compare "quoted" values and C:\\synthetic\\file.\nUse only this selected excerpt.';
const url = 'https://example.invalid/synthetic?value="quote"#anchor';
const result = await run([url, 'Synthetic "title" \\ source', 'Synthetic Author', intent]);
for (const [property, expected] of Object.entries({
  title: result.values.sourceTitle,
  author: result.values.sourceAuthor,
  source_url: url,
  user_intent_interview: intent,
})) {
  const scalar = result.rendered.match(new RegExp(`^${property}: (.*)$`, "m"))[1];
  assert.equal(JSON.parse(scalar), expected);
}
assert.ok(result.rendered.startsWith("---\n"));
assert.ok(result.rendered.includes("## Original Content\n\n## Analysis"));
assert.equal(result.calls, 4);
for (const [answers, type] of [
  [[null], "article"], [[""], "article"], [[url], null],
  [[url, "Title", "Author", null], "article"],
  [[url, "Title", "Author", "   "], "article"],
  [[url, "Title", "Author", "one\ntwo\nthree"], "article"],
]) {
  await assert.rejects(() => run(answers, type), /source\.template:/);
}
console.log("source template: whole-scalar quote/backslash/newline roundtrip and six cancellation/empty/line-boundary cases passed; bounded Templater mock, not live app/producer QA");
