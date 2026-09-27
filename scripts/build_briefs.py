"""Build briefs.html from the Design & Gestalt homework document.

    python scripts/build_briefs.py ["path/to/Design & Gestalt Homework Assignments.md"]

The homework document is the source. Edit it, then run this script;
never edit briefs.html by hand. Needs the `markdown` package.
"""
import re
import sys
from pathlib import Path

import markdown

DEFAULT_SOURCE = Path(r"D:\Google Drive\THRO\Lectures\S1_Design & Gestalt"
                      r"\Design & Gestalt Homework Assignments.md")
ROOT = Path(__file__).resolve().parent.parent

TEMPLATE = """<!doctype html>
<!-- Generated from the homework document by scripts/build_briefs.py. Edit the document, not this file. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Homework Briefs</title>
<meta name="description" content="The full homework brief for every week — Design &amp; Gestalt, Smart Interactive Media.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Archivo:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">

<style>
  :root {
    --ground: #EDEEF1;
    --surface: #FFFFFF;
    --ink: #14161B;
    --ink-2: #565D6C;
    --ink-3: #878E9E;
    --rule: #D3D7E0;
    --accent: #2439D4;
    --accent-ink: #FFFFFF;

    --display: "Syne", "Archivo", system-ui, sans-serif;
    --body: "Archivo", system-ui, -apple-system, sans-serif;
    --mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
  }

  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --ground: #0D0F14;
      --surface: #161A23;
      --ink: #EDEFF4;
      --ink-2: #A4ACBB;
      --ink-3: #6C7488;
      --rule: #2A303C;
      --accent: #6B7FFF;
      --accent-ink: #0D0F14;
    }
  }

  :root[data-theme="dark"] {
    --ground: #0D0F14;
    --surface: #161A23;
    --ink: #EDEFF4;
    --ink-2: #A4ACBB;
    --ink-3: #6C7488;
    --rule: #2A303C;
    --accent: #6B7FFF;
    --accent-ink: #0D0F14;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    background: var(--ground);
    color: var(--ink);
    font-family: var(--body);
    line-height: 1.55;
  }

  .wrap { max-width: 820px; margin: 0 auto; padding: 0 24px 90px; }

  /* ---------- masthead ---------- */
  header { padding: 52px 0 26px; }

  .back {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-3);
    text-decoration: none;
    display: inline-block;
    margin-bottom: 22px;
  }
  .back:hover { color: var(--accent); }

  h1 {
    font-family: var(--display);
    font-weight: 800;
    font-size: clamp(32px, 6vw, 56px);
    letter-spacing: -0.035em;
    line-height: 1;
    margin: 0 0 16px;
  }

  .standfirst { font-size: 16px; color: var(--ink-2); max-width: 62ch; margin: 0; text-wrap: pretty; }

  /* ---------- sticky nav ---------- */
  .nav {
    position: sticky;
    top: 0;
    z-index: 5;
    background: var(--ground);
    border-bottom: 1px solid var(--rule);
    padding: 12px 0;
    margin-bottom: 10px;
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
  }
  .nav a {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--ink-2);
    text-decoration: none;
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 4px 7px;
    min-width: 28px;
    text-align: center;
  }
  .nav a:hover { border-color: var(--accent); color: var(--accent); }

  /* ---------- the document ---------- */
  .doc { font-size: 15.5px; }
  .doc h2 {
    font-family: var(--display);
    font-weight: 700;
    font-size: 26px;
    letter-spacing: -0.02em;
    line-height: 1.15;
    margin: 12px 0 6px;
    scroll-margin-top: 100px;
  }
  .doc h3 {
    font-family: var(--display);
    font-weight: 700;
    font-size: 19px;
    letter-spacing: -0.01em;
    margin: 30px 0 8px;
    scroll-margin-top: 100px;
  }
  .doc h2 + h3 {
    font-family: var(--body);
    font-weight: 500;
    font-size: 16px;
    letter-spacing: 0;
    color: var(--ink-2);
    margin: 0 0 12px;
  }
  .doc p { margin: 0 0 12px; text-wrap: pretty; }
  .doc ul, .doc ol { padding-left: 24px; margin: 6px 0 12px; }
  .doc li { margin: 5px 0; }
  .doc li > ul, .doc li > ol { margin: 4px 0; }
  .doc blockquote {
    margin: 16px 0;
    padding: 12px 16px;
    border-left: 3px solid var(--accent);
    background: var(--surface);
    border-radius: 2px;
  }
  .doc blockquote p:last-child { margin-bottom: 0; }
  .doc code {
    font-family: var(--mono);
    font-size: 13px;
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 2px;
    padding: 0 4px;
  }
  .doc hr { border: 0; border-top: 1px solid var(--rule); margin: 44px 0 34px; }
  .doc a { color: var(--accent); overflow-wrap: anywhere; }

  .to-list {
    display: inline-block;
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--accent);
    text-decoration: none;
    border: 1px solid var(--accent);
    border-radius: 2px;
    padding: 6px 10px;
    margin: 2px 0 14px;
  }
  .doc a.to-list { overflow-wrap: normal; }
  .to-list:hover { background: var(--accent); color: var(--accent-ink); }

  :focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
</style>
</head>
<body>
<div class="wrap">

  <header>
    <a class="back" href="index.html">&larr; Design &amp; Gestalt</a>
    <h1>Homework briefs</h1>
    <p class="standfirst">
      The full brief for every week: what to study first, the task step by step, and what to
      hand in. The <a href="checklists.html">homework checklist</a> is the short version for ticking off.
    </p>
  </header>

  <nav class="nav">
%(nav)s
  </nav>

  <article class="doc">
%(body)s
  </article>

</div>
</body>
</html>
"""


def build(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    text = re.sub(r"\A# [^\n]*\n", "", text)  # the page carries its own title
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])

    weeks = [int(n) for n in re.findall(r"<h2>Week (\d+) — ", body)]
    body = re.sub(r"<h2>Week (\d+) — ", lambda m: f'<h2 id="week-{m[1]}">Week {m[1]} — ', body)
    # after each week's subtitle, a link to its checklist
    body = re.sub(
        r'(<h2 id="week-(\d+)">.*?</h2>\s*<h3>.*?</h3>)',
        lambda m: m[1] + f'\n<a class="to-list" href="checklists.html#week-{m[2]}">Checklist for this week</a>',
        body, flags=re.S)
    body = body.replace("<h3>Party fact sheet</h3>", '<h3 id="party-fact-sheet">Party fact sheet</h3>')

    nav = "\n".join(f'    <a href="#week-{n}">{n:02d}</a>' for n in weeks)
    nav += '\n    <a href="#party-fact-sheet">Party fact sheet</a>'
    indented = "\n".join("    " + line if line else line for line in body.splitlines())
    return TEMPLATE % {"nav": nav, "body": indented}


if __name__ == "__main__":
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    out = ROOT / "briefs.html"
    out.write_text(build(source), encoding="utf-8", newline="\n")
    print(f"wrote {out}")
