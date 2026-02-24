# 2048 + Keep Ask Why (GitHub Pages)

This repo now also includes a minimal no-UI question machine for GitHub Pages:

- URL: `https://a-bit-thinker.github.io/2048/`
- File: `index.html`
- Behavior: emits simple recurring questions every 200 seconds by default

## Important limitation

GitHub Pages is static hosting. It cannot run `question_machine.py` as a backend process.

So this page runs a browser-side equivalent in JavaScript with the same simple behavior.

## Controls (from browser console)

Open the site, then open browser devtools console:

- `keepAskWhy.status()`
- `keepAskWhy.next()`
- `keepAskWhy.ask("I failed again")`
- `keepAskWhy.askMarkdown("# Loop\\nThis is markdown input")`
- `keepAskWhy.request("POST", "/ask", { markdown: "# Loop\\nThis is markdown input" })`
- `keepAskWhy.setIntervalSec(60)`
- `keepAskWhy.setQuestions(["Why?","What now?"])`
- `keepAskWhy.stop()`
- `keepAskWhy.start()`

## Optional URL parameter

- `?interval=5` to change startup interval
- `?md=...` to send markdown text directly as input on load
- `?md_b64=...` to send base64-encoded markdown text on load

Example:

- `https://a-bit-thinker.github.io/2048/?interval=5`
- `https://a-bit-thinker.github.io/2048/?md=##%20Test%0AHello`
