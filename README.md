# Design & Gestalt

Course materials for **Design & Gestalt** — Smart Interactive Media, 1st semester, TH Rosenheim.

Published site: https://cyberhirsch.github.io/DesignGestalt/

## Contents

- `index.html` — course hub, schedule, and links to everything below
- `checklists.html` — the homework checklist: what to hand in each week and what to check first, as tick lists (14 weeks, 76 hand-ins and 64 checks)
- `briefs.html` — the full homework brief for every week. Generated: edit the homework
  document, then run `python scripts/build_briefs.py` (needs the `markdown` package)
- `slides/` — the finished decks as single HTML files, with teaching-only images left out, and a
  credits page per deck (`week-01.html`, `week-01-credits.html`)
- `tools/`
  - `gestalt.html` — interactive demos of nine Gestalt principles (Week 1)
  - `contrast.html` — WCAG AA/AAA checker with colour-blindness simulation (Week 7)
  - `style-lottery.html` — assigns each student a design style to present (62 movements)
  - `type-lottery.html` — the same for FontShop's 100 Best Fonts

The hub also links out to four practice games by Method of Action — The Bézier Game,
Color, KernType and Shape Type — each tied to the week it supports.

Slide decks are added per week as they are finished.

## Notes

The lotteries and the checklists keep their state in the browser's local storage, so
progress survives a reload but lives only on the device it was entered on. Nothing is
submitted or shared from these pages.
