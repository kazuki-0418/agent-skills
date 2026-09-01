---
name: copy-review
description: >-
  Run sales and landing-page copy through all four Rob Palmer copy skills in
  one pass — direct-response-copy, landing-page-copy, copychief, and
  compliance-checker — then have a separate copy-auditor score the result.
  Use when writing, rewriting, punching up, or reviewing landing pages, VSLs,
  emails, headlines, CTAs, Meta ads, waitlist pages, or Canpitch LP copy.
  Also trigger for コピー, レビュー, LP直して, 見出し, CTA, セールスコピー, copychief,
  compliance, bridge page, lander.
---

# Copy Review (4-lens pass)

Do not run these skills one at a time as four separate conversations.
One piece of copy goes through **all applicable lenses**, then a **separate
auditor** scores it. Same pattern as `ad-copy` → `ad-copy-auditor`.

## Roles

| Role | What it is | What it does |
|---|---|---|
| **You (maker)** | This conversation | Classify, write/rewrite, apply the four skills |
| **copy-auditor** | Subagent | Scores. Does not rewrite. Call it before Kazuki sees the copy |

Do not self-score and ship. The maker is biased toward "good enough."

## Skill files (read, do not rely on memory)

Search in this order (same file via symlink after local setup):

1. `.cursor/skills/<name>/SKILL.md` in this repo (`kazuki-0418/agent-skills`)
2. `~/.cursor/skills/<name>/SKILL.md`
3. `~/.claude/skills/<name>/SKILL.md`

| name | role |
|---|---|
| `direct-response-copy` | how to write |
| `landing-page-copy` | short landers / bridge pages |
| `copychief` | review structure and verdict |
| `compliance-checker` | platform policy |
| `compliance-checker/references/trigger-words.md` | substitutions |

Read the ones that apply **before** writing or rewriting. The auditor will
read them again on its own.

## Which lenses apply

Classify first (copychief Step 1 + Schwartz awareness). Then:

| Piece | DR | LP lander | Copychief | Compliance |
|---|---|---|---|---|
| Product LP (Canpitch `/`) | always | only the headline/CTA/sequence bits; skip "don't mention the product" | always | organic site: still flag fake proof, income claims, scare tactics. Meta ad rules = N/A unless this copy will be advertised |
| Bridge / pre-sell lander | always | **full skill** (3 paragraphs, no price, tease mechanism) | always | if paid traffic: full Meta/Google pass |
| Meta / TikTok / Google ad | always | skip (that's `ad-copy`) | always | **strict** |
| Email / VSL / TSL | always | skip | always | by platform |
| Headline / CTA only | always | if it sits on a lander | always | if it will run as an ad |

`landing-page-copy` is a **bridge page** skill (300–800 words, does not sell
the product). Canpitch's site LP **is** a product page. Do not force the
"never mention the product" rule onto it. Still steal: mechanism, awareness
match, CTA as benefit, 2–3 headline variations.

## Maker workflow

```
Task progress:
- [ ] 1. Classify (type, funnel, awareness, mechanism, destination, platform)
- [ ] 2. Read the applicable SKILL.md files
- [ ] 3. Write or rewrite using those skills
- [ ] 4. Launch copy-auditor with the packet below
- [ ] 5. 合格 → show Kazuki the copy + score
- [ ] 6. 要修正 → fix named items, relaunch auditor
- [ ] 7. 3 fails → stop and report which items keep failing
```

## Auditor packet

Launch `copy-auditor` via the Task tool (`subagent_type: copy-auditor` if
listed; otherwise a generalPurpose agent whose prompt is the auditor file
at `~/.cursor/agents/copy-auditor.md`).

Pass all of:

| # | Content |
|---|---|
| 1 | Kazuki's original request |
| 2 | Full copy (every headline, body block, CTA) |
| 3 | **Classification** — type / funnel / awareness / mechanism / destination / platform |
| 4 | **Which lenses apply** and why any were marked N/A |
| 5 | **Work log** — which skill files you Read, any numbers/proof and where they came from |
| 6 | Round number. On round 2+, the item IDs that failed last time |

No work log → auditor returns 判定不能. Do not invent one after the fact.

## Output to Kazuki (only after 合格)

1. The copy
2. Classification (one short block)
3. Auditor verdict table
4. If you wrote a lander from scratch: 2–3 variations as the LP skill requires,
   each scored, winner marked

## Do not

- Review with only copychief, or only compliance, then stop
- "Mentally apply" a skill you did not Read this turn
- Invent testimonials, user counts, or time-to-result
- Soften a 否 so the copy can ship
