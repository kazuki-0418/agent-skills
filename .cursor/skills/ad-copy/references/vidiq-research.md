# vidIQ Research Playbook

The full procedure for finding out what is actually winning in a niche before you write.
SKILL.md covers when to research and the headline rules; this file has the mechanics.

## Contents

1. [Credit budget](#credit-budget)
2. [The three search angles](#the-three-search-angles)
3. [Writing the search call](#writing-the-search-call)
4. [The language trap](#the-language-trap)
5. [Reading the results](#reading-the-results)
6. [Deciding what counts as a pattern](#deciding-what-counts-as-a-pattern)
7. [Watching top performers](#watching-top-performers)
8. [Measuring length in-niche](#measuring-length-in-niche)
9. [Turning findings into a spec](#turning-findings-into-a-spec)
10. [Tool reference](#tool-reference)

---

## Credit budget

vidIQ charges per call, so plan the spend before you start. Check the balance first with
`vidiq_balance` (free) — if it is low, tell the user what a full pass costs and let them
decide the depth rather than silently running out halfway.

| Call | Cost | What you get |
|---|---|---|
| `vidiq_balance` | 0 | Remaining credits |
| `vidiq_instagram_tiktok_outlier_search` | 5 | ~6 outliers per platform with hook text, format, pacing, audio mix |
| `vidiq_watch_shortform_content` | 10 | Second-by-second breakdown of one video |
| `vidiq_ig_accounts_from_outliers` | 10 | Creator/competitor accounts in a niche |
| `vidiq_ig_profile_reels` | 5 | Up to 12 reels from one handle |
| `vidiq_job_poll` | 0 | Retrieves async results |

A solid default pass is **3 searches + 2 watches = 35 credits**. That is enough to find
patterns and understand structure. Go deeper only when the first pass leaves a real
question open.

---

## The three search angles

One search gives you one slice of a market and it is easy to mistake that slice for the
whole thing. Run at least three, because each answers a different question:

| Angle | Question it answers | Example query |
|---|---|---|
| **The pain** | What content wins on this *topic*, in any format? | "交流会で会った人の名前が思い出せない悩み" |
| **The format** | What wins in the *format* you plan to shoot? | "スマホアプリの画面録画だけで使い方を見せる紹介動画" |
| **The adjacent category** | Who is already selling something similar, and how? | "AIが自動でメモを整理してくれるアプリの紹介" |

The pain angle and the format angle frequently disagree — and that disagreement is the
most useful thing you will learn. If talking heads dominate the topic but screen recordings
dominate the format, a screen-recording video about that topic is competing on two fronts
at once. Say so.

Add a fourth angle when the brief has a distinctive hook type ("secret", "unpopular
opinion", "POV"), using `embeddingType: "hook"` to search on the first three seconds
rather than the whole premise.

---

## Writing the search call

```
vidiq_instagram_tiktok_outlier_search({
  query: "<full content premise in the target market's own language>",
  audienceQuery: "Culture/Region: Japan/Japanese; Global: false; Demographics: working professionals 25-40, networking, remembering people;",
  descriptionLanguage: ["ja"],
  resultsPerPlatform: 6
})
```

- **`query`** — write it in the language the target audience speaks, as a complete premise,
  not keywords. The search is embedding-based, so "会った人の名前が思い出せない悩み" retrieves
  far better than "人脈 アプリ".
- **`embeddingType`** — `concept` (default) for the whole premise, `hook` for the first
  three seconds, `format` for a subject-free production template. Use `format` when you
  want "how do people shoot this" independent of topic.
- **`audienceQuery`** — the schema is strict: `Culture/Region: ...; Global: <true|false>; Demographics: ...;`
  Getting it wrong silently degrades relevance rather than erroring.
- **`resultsPerPlatform`** — 6 is a good default. More costs the same but takes longer to read.

## The language trap

**The search defaults to English captions.** If you are working a non-English market and
forget `descriptionLanguage`, you get English-language results and every conclusion you
draw will be about the wrong market — while looking perfectly plausible. This is the single
easiest way to produce confidently wrong research.

Set `descriptionLanguage` to the target market's code on every call: `["ja"]`, `["es"]`,
`["pt"]`, and so on. If the user's market is genuinely global English, set `["en"]`
explicitly so the choice is on the record rather than inherited from a default.

---

## Reading the results

Each result carries more than a view count. The fields that change what you write:

| Field | Why it matters |
|---|---|
| `hook_0_3s.text` | The literal words that stopped the scroll. Collect these verbatim — they are the highest-signal thing in the response |
| `hook_0_3s.visual` | What was on screen during those words. Often *not* the product |
| `outlier multiple` (e.g. 106.7x) | How far above that creator's own median. A 100x on a small account beats a 2x on a big one — it isolates the content from the audience |
| `audio.audio_mix` | Voice only / Voice + Music / Music only. Cheap to copy, frequently decisive |
| `execution.pacing` + `visual_changes` | Cut rhythm. "Fast / High" vs "Moderate / Low" is a production decision you can act on today |
| `format.template` | The reusable shape (talking head, split screen, screen recording, listicle) |
| `effort.time` + `effort.barrier` | Whether the winning format is even reachable for this user |
| `durationSeconds` | Feeds the length distribution — see below |

Read `hook_0_3s.visual` and `hook_0_3s.text` together. The most common finding in
product-led niches is that **the winners do not show the product in the first three
seconds** — the text carries the hook while the visual is something human and physical.
If the brief opens on the product, that is a concrete, defensible note.

---

## Deciding what counts as a pattern

Two outliers from a platform is the floor before calling something a pattern. Below that
you are describing one video.

Beyond counting, check independence:

- **Shared operators.** Handles that rhyme (`hiromu_noimosai`, `nanoka_noimosai`) or share a
  posting cadence and visual grammar are usually one team running a playbook. Two accounts
  from one operator is closer to one data point than two. Say so rather than quietly
  inflating the count.
- **Sponsored posts.** A `#pr` post proves a brand paid for reach, not that the format won
  organically. Still useful as category evidence; weaker as format evidence.
- **Follower skew.** A 17x on a 420K-follower account and a 55x on a 73-follower account are
  different claims. The small-account outlier is stronger evidence that the *content* did the
  work.

When evidence is thin, write it as thin. "Two videos, same operator" is a more useful
sentence than "the market shows".

---

## Watching top performers

Search metadata tells you *what* the winners do. It does not tell you the order, the
timing, or how the CTA is built. For that, spend 10 credits on
`vidiq_watch_shortform_content` for the top one or two — ideally one that matches your
planned format and one that is simply the biggest outlier.

Pass a `prompt` asking for what you actually need to copy:

> Break down the exact structure: second-by-second beats, where the hook lands, when the
> product first appears, how the problem is framed before the solution, music/voiceover mix,
> cut frequency, and how the CTA works. I want a reusable template.

The call is asynchronous — it returns an `mcpJobId`, and you poll `vidiq_job_poll` (free)
until `status` is `completed`. Fire both watches in the same turn so they run in parallel,
then poll both.

What tends to come back that you could not have guessed: two-tier CTAs (share first, follow
second), text overlay position chosen to dodge platform UI, caption update cadence tied to
narration, and whether the creator ends on their own profile grid as social proof.

---

## Measuring length in-niche

General short-form advice ("7-15 seconds", "under 30 seconds") comes from broad,
mostly-English datasets and is often flatly wrong for a specific niche and language. You
already have the real numbers: every search result carries a duration.

Collect the durations of the outliers you found and report the actual distribution against
whatever length the brief assumed. When they disagree, the measured distribution wins,
because it is drawn from the exact niche, language, and month the user is posting into.

This one check has overturned a stated spec more than once. Do it every time — it costs
nothing beyond reading the numbers you already paid for.

---

## Turning findings into a spec

Research that ends in observations is only half-delivered. Convert it into a diff against
what the user currently has:

```markdown
| # | Current | Market | Change |
|---|---|---|---|
| 1 | Opens on the app screen | 3 outliers open on an unrelated physical action | Move the product past 0-3s |
| 2 | Silent | Nearly all winners run music from 0s + tap SFX | Add a music bed |
```

Then the script itself, beat by beat with timings, grounded in the template you extracted.

**Surface contradictions with the user's own assumptions explicitly.** If the data
contradicts a spec they wrote, a benchmark they recorded, or an instruction they just gave
you, that is the highest-value output of the whole pass — it is the thing they could not
have gotten by thinking harder. Lead with it, cite the numbers, and separate "your framing
of the problem was right" from "your proposed fix was not". Both can be true at once, and
saying so is more useful than a verdict.

Where a finding contradicts something durable — a spec file, a recorded benchmark, a
decision log — write the correction into that source, not only into the chat reply.

---

## Tool reference

| Tool | Use for |
|---|---|
| `vidiq_balance` | Check credits before planning depth (free) |
| `vidiq_instagram_tiktok_outlier_search` | The core call. Outliers across IG + TikTok |
| `vidiq_watch_shortform_content` | Second-by-second structure of one video (async) |
| `vidiq_job_poll` | Retrieve async watch results (free) |
| `vidiq_ig_accounts_from_outliers` | Find competitor/creator accounts in a niche |
| `vidiq_ig_profile_reels` | A specific creator's recent reels (max 12, no pagination) |
| `vidiq_keyword_research`, `vidiq_outliers`, `vidiq_youtube_search` | YouTube-side equivalents when the brief is YouTube |

These are MCP tools and are frequently deferred — load them with ToolSearch before calling,
batching every tool you expect to need into one `select:` query rather than one at a time.

If vidIQ is unavailable or the user has no credits, say so plainly and write from the
frameworks in SKILL.md instead. Research-grounded copy is better than unresearched copy,
but unresearched copy clearly labelled as such is better than a stall.
