---
name: ad-copy
description: "Research what is actually winning in a niche with vidIQ, then write the ad copy or short-form video script from that evidence — Meta primary text, headlines, TikTok/Reels UGC scripts, hooks, and beat-by-beat shooting plans. Use this skill whenever the user asks to write, rewrite, or brainstorm ads, ad hooks, captions, primary text, UGC scripts, video ad scripts, talking head scripts, ad angles, ad variations, or scroll-stopping hooks — and equally when they ask what hook, format, or length is working in a niche, want competitor or market research for short-form content, ask why a video is not performing, push back on a script, or want a content plan for TikTok/Instagram Reels. Also trigger for 'write me an ad', 'UGC 台本', 'この動画の脚本を書き換えて', 'フックを考えて', 'バズってる型を調べて', 'ADHD hook ad', 'in-feed VSL script'. Research and script are one pass, not two skills. Every deliverable is scored by a separate agent (ad-copy-auditor) before it reaches the user. Does NOT handle compliance or legal review, landing pages, emails, or long-form VSLs."
---

> Created by **Rob Palmer** — direct-response copywriter ($523M+ tracked).
> Source & updates: https://github.com/robpalmer99/claude-code-copywriting-skills
> Free under CC-BY-4.0. Attribution requested when redistributed.
>
> Extended locally with a vidIQ market-research stage (Step 2) so scripts are grounded in
> measured outlier data rather than general principles alone.

# Ad Copy & Short-Form Script Skill

This skill writes high-converting ad copy and short-form video scripts — Meta primary text,
headlines, descriptions, TikTok/Reels UGC scripts, and beat-by-beat shooting plans. It draws
on proven direct response frameworks from Schwartz, Halbert, Makepeace, Georgi, Sultanic and
others, and on what vidIQ shows is *currently* outperforming in the specific niche, language,
and month you are writing into.

The ad's ONLY job is to get the click. Not close the sale. Not educate fully. Get the click.

**The four stages are one pass:** classify the brief → research the market → write → have a
separate agent score it. Skipping the research stage is how you end up producing copy that is
textbook-correct and still wrong for the market. Skipping the scoring stage is how a draft that
quietly ignores this skill's own instructions reaches the user. Both fail silently, which is
what makes them expensive.

---

# Step 1: Classify the Ad Brief

Before writing a single word, determine these four things. Ask the user if unclear.

## Funnel Position

| Position | What They Know | Ad Approach |
|----------|---------------|-------------|
| **Cold traffic** | Nothing about you | Lead with problem/curiosity, longer education |
| **Warm/engaged** | Seen you before | More direct, mechanism-focused |
| **Retargeting** | Visited your page | Objection-handling, social proof, urgency |

## Awareness Level (Schwartz)

Eugene Schwartz's 5 Levels of Awareness determine everything — your headline, your copy length, your angle, and where the ad sends people:

| Level | Lead With | Ad Length | Send To |
|-------|-----------|-----------|---------|
| **Unaware** | Identity/emotion, not the problem | Long, educational | Advertorial |
| **Problem-Aware** | Name the pain vividly, tease mechanism | Medium-long | VSL or advertorial |
| **Solution-Aware** | Differentiate your mechanism | Medium | VSL or long PDP |
| **Product-Aware** | Overcome objections, add proof | Short-medium | PDP |
| **Most-Aware** | Lead with the deal | Short | Checkout or offer page |

The less aware they are, the longer your copy needs to be.

## Strategy: Sell the Click vs. Sell the Solution

This is the most important strategic decision for any Meta ad:

**Sell the Click** — Short caption, curiosity-driven image/video, minimal info revealed. The ad's job is ONLY to generate the click. The advertorial or VSL does the selling. Best for: unaware/problem-aware audiences, products that need explanation, high-ticket offers.

**Sell the Solution** — Longer video with education, visual demos, proof. The ad itself does much of the selling. The landing page just needs to close. Best for: solution-aware+ audiences, simple products, visual products, lower price points.

**Critical rule:** If you show the product in the ad, the viewer becomes product-aware. Never send a product-aware viewer to a blind VSL — send them to a PDP or offer page instead.

**Real-world example:** Many 8-figure brands run BOTH strategies simultaneously. Static ads with product images sell the solution and send to PDPs. Curiosity video ads sell the click and send to advertorials or VSLs. Different awareness levels, different funnels, same brand.

## Ad Format

- **Static image + primary text** — Caption does the work, image stops the scroll
- **Short UGC / talking head** (15-60s) — First-person, phone-filmed feel
- **ADHD super hook ad** (3-7min) — Rapid-fire hooks, never stops hooking
- **Story-style video** (60-120s) — Personal narrative arc

---

# Step 2: Research What Is Actually Winning (vidIQ)

Direct response principles tell you what tends to work. They cannot tell you what is working
in *this* niche, in *this* language, this month — and that gap is where most short-form scripts
die. A hook that is textbook-perfect can still open on the wrong kind of image for the niche;
a length that "everyone knows" is right can be half what the actual winners run.

vidIQ answers those questions with measured data: posts that beat their own creator's median
by a large multiple, with their hook text, opening visual, audio mix, cut rhythm, and duration
attached. Use it, then write from it.

## When to research

Research when the answer would change what you write:

- **Short-form video or UGC scripts** — always. Format conventions vary enormously by niche and
  language, and they are exactly what the data covers.
- **A market or language you have not validated yet** — always. Assumptions imported from
  English-language advice are the most common failure mode.
- **The user is pushing back on a draft**, or asking why something underperformed. Guessing at
  the cause in conversation is slower and less convincing than measuring it.
- **A stated spec smells like folklore** — a length rule, a "hooks must X" claim, a benchmark
  with no source attached. Check it.

Skip it for micro-edits (tighten this headline, give me three subject lines), when the user
has already supplied research, or when they explicitly want a fast draft. Say that you skipped
it and why, so nobody mistakes an unresearched draft for a researched one.

**Research does not always mean spending vidIQ credits.** This user maintains a local corpus of
collected, transcribed reels; for a niche it already covers, that *is* the search half of the
research. It does not cover the visual half — whisper hears, it does not watch. Step 0 of the
pass below says how to reach it and where it stops.

## The pass

Read `references/vidiq-research.md` before your first call — it has the exact parameters,
query templates, credit costs, and the failure modes that are easy to walk into. The shape:

0. **Check the local corpus first — it is free, and for a niche it already covers it is deeper
   than a fresh vidIQ pass.** This user collects Instagram reels into
   `~/Desktop/dev/ig-research/` and transcribes them locally (see the `/ig-sync` command).
   The findings live in the vault at
   `10_projects/kivori/marketing/2026-08-20-instagram-reel-analysis.md`, the full transcripts
   in the NotebookLM notebook *Instagram バズ分析 (ig-sorter)*
   (`523dcc55-2b15-49e9-8694-73dd674cf36d`), and the raw data in
   `~/Desktop/dev/ig-research/transcribed_data.json`.

   Ask the notebook with `nlm notebook query <notebook-id> "<question>"` — it answers from the
   transcripts and returns the cited posts in full. Read `transcribed_data.json` directly when
   you need to **count** something rather than ask about it; every entry carries `play_count`,
   `like_count`, `comment_count`, the caption, and the transcript **with timestamps**.

   **What the corpus replaces, and what it does not.** Be precise about this — the two halves
   of "second-by-second structure" come from different places:

   | | Corpus (free) | `watch_shortform_content` (10 cr) |
   |---|---|---|
   | What is **said**, and when | ✅ timestamped transcript | ✅ |
   | What is **on screen**, and when | ❌ **not captured** | ✅ scene-by-scene walkthrough |

   So the corpus replaces **step 2** (the searches — it already holds outliers with their hooks,
   view counts, captions, and durations). It does **not** replace step 3. Whisper hears; it does
   not watch. When the brief turns on visual grammar — the opening shot, what the hands do, when
   the screen recording cuts in — you still need either a watch, or to open the mp4 yourself
   (they are all in `~/Desktop/dev/ig-research/videos/`, named by shortcode, which is free).

   **When the corpus covers the niche and language, skip step 2 and decide step 3 on its merits.**
   Report that you used the corpus and how many posts it held, so nobody mistakes it for an
   unresearched draft. Fall through to the full vidIQ pass when the brief is a niche or language
   the corpus does not cover, or when the corpus is stale relative to the question.

   Two caveats carried over from how it is built: posts whose audio is music only are excluded
   (roughly a third of what gets collected — the on-screen text is the content and it is not
   captured), and play counts that came from vidIQ are rounded displays, not exact figures.
   Both are flagged in the analysis note.

1. **Check credits** with `vidiq_balance` (free). A standard pass is 3 searches + 2 watches =
   35 credits. If the balance is tight, tell the user the cost and let them pick the depth.
2. **Search from three angles** — the pain, the format, the adjacent category — with
   `vidiq_instagram_tiktok_outlier_search`. Where they disagree is usually the finding.
3. **Watch the top one or two** with `vidiq_watch_shortform_content` for second-by-second
   structure. Search metadata gives you *what* winners do; only the watch gives you the order,
   the timing, and how the CTA is built.
4. **Extract the template and the diff** — what the market does versus what the brief does.

## Things that will burn you

**The search defaults to English captions.** Working a non-English market without setting
`descriptionLanguage` returns English results, and every conclusion drawn from them will be
about the wrong market while looking entirely plausible. Set it explicitly on every call —
including `["en"]` when English really is the target, so the choice is on the record.

**Two outliers is the floor for calling something a pattern**, and count independence, not
handles. Accounts with rhyming names or identical visual grammar are usually one team running
one playbook; that is closer to one data point than two. Report thin evidence as thin — "two
videos, same operator" is more useful than "the market shows".

**Measure duration in-niche rather than importing a benchmark.** Every result carries its
length. Collect them and compare against whatever the brief assumed. General short-form
guidance is drawn from broad English datasets and is regularly wrong by a factor of three for
a specific niche and language.

**Read the opening visual, not just the hook text.** In product-led niches the winners
routinely do *not* show the product in the first three seconds — the text carries the hook
while the visual is something human and physical. If the brief opens on the product, that is a
concrete note worth making.

## Before you carry a pattern across: explain the mechanism

A shared feature across winners is not yet a reason. Before recommending that the user copy
anything you observed, write one sentence: **"this works because ___"** — and then check
whether that *because* exists in their situation. If you cannot write the sentence, you found
a correlation, not a finding, and recommending it is guesswork dressed as data.

This failure has a specific shape worth recognising. Five outliers all opened on a hand
holding a phone, and the obvious conclusion was "put a phone in the opening shot." The
mechanism, once actually checked, was that all five were phone-tips videos — **the phone was
the subject of the content, not a hook device.** For a product with a different subject, the
pattern transferred nothing. What *did* transfer, from the same data, was one level up:
motion already underway at frame one, curiosity carried by the text rather than the image, and
a look that reads as someone's real desk. Same evidence, opposite conclusions, depending on
whether you copied the surface or the function.

Two habits prevent it:

- **Check the sample for genre lock-in.** If every example comes from one content genre, what
  you found is that genre's convention. Say so, and ask whether the convention has a reason
  that survives outside it.
- **Raise the abstraction one notch and re-test.** "Holds a phone" is a surface. "The subject
  of the video is present in frame one" is a mechanism — and it may or may not apply. The
  abstracted version is usually the one worth carrying.

A high outlier multiple makes this harder, not easier: a 66x on a 233-follower account is
compelling evidence that *something* in that video worked, and it is tempting to attribute it
to whatever you happened to notice.

## Reporting it

Lead with what contradicts the user's current assumptions. That is the part they could not
have reached by thinking harder, and it is worth more than a confirmation.

Be precise about *which* part was wrong. "Your hook is validated — three of the top performers
use that exact phrasing; what is not working is that you open on the product" is a far more
useful sentence than a verdict on the whole piece. A user whose framing was right and whose
fix was wrong needs to hear both halves.

Then convert findings into a diff table (current → market → change) and write the script from
the extracted template. Where a finding overturns something durable — a spec, a recorded
benchmark, a decision log — correct it at the source, not only in chat.

---

# Step 3: Write the Ad

## Meta Ad Specs (Quick Reference)

Read `references/meta-ad-specs.md` for full specs. Key numbers:

- **Primary text**: First 125 characters show before "See more" — this is everything
- **Headline**: 27 characters optimal for mobile display (40 max)
- **Description**: 27 characters visible, often hidden on mobile entirely

---

## Writing Meta Primary Text

### The Three Fields

**Primary Text (above the creative)** — The main sell. First 125 characters are your headline equivalent.

Structure for "See more" expansion:
```
[Hook — first 125 chars. Must create an open loop or pattern interrupt]
                                               ← "See more" break
[Expand: agitate the problem, tease the mechanism, drop proof]
[CTA: tell them what to do next]
```

The "See more" click is a micro-conversion. Make expanding irresistible.

**Headline (below the creative)** — Benefit-driven, specific. NOT a label — a second hook.

Weak: "Learn More" | "Check This Out" | "Click Here"
Strong: "The 7-Second Morning Fix" | "Why Diets Fail After 40" | "23 Lbs in 8 Weeks"

**Description (below the headline)** — Secondary benefit or risk reversal. Often hidden on mobile, so don't put critical info here. Use for friction reduction: "Free shipping" | "No credit card needed" | "2-minute read"

### The WHY / WHAT / HOW Structure

Use this fill-in-the-blank formula (from Alen Sultanic) to structure any ad:

**WHY (The Problem)** — Open with curiosity or a contrarian hook. State the problem. Agitate.

> "Why do _____ matter more than _____ after ___?"
> "[Deep identifier — something that resonates with their identity]"
> "Experts are calling it the '_____'. But it's not a _____ at all..."
> "It hits from all sides: _____ stress. _____ stress. _____ stress. It's NOT aging, it's not normal and it's not permanent."

**WHAT (The Mechanism)** — Pivot to the mechanism. Tease the solution without revealing it.

> "Fortunately, there is another way. One that focuses on _____ rather than _____."
> "Using this approach, [proof: thousands of people / specific number] are [specific result]."

**HOW (The Product/CTA)** — Reveal just enough to make the click inevitable.

> "Click below to discover how [mechanism] works for [their specific situation]."

---

## Hook Writing

The hook is the single biggest lever in ad performance. Test more hooks than anything else.

### Hook Types

| Type | Example | When to Use |
|------|---------|-------------|
| **Curiosity** | "There's a reason your doctor won't tell you about this..." | Cold traffic, unaware |
| **Contrarian** | "Everything you've been told about _____ is wrong." | Problem-aware, skeptical |
| **Social proof** | "Over 47,000 women have tried this 30-second trick..." | Solution-aware+ |
| **Story** | "Last March I was 40lbs overweight and my doctor said..." | Cold, emotional markets |
| **Demographic callout** | "Attention men over 50 who..." | Cold, specific targeting |
| **Result** | "I lost 23 lbs in 8 weeks without giving up pizza." | Warm/retargeting |
| **Pattern interrupt** | "Stop scrolling. This actually matters." | Cold, saturated markets |
| **Fascinating fact** | "Your liver processes 500+ chemicals before breakfast." | Unaware, education-first |

### Hook Shapes for Fact-Led Video

The types above are psychological angles. When the video's raw material is a *fact* — a
statistic, a piece of history, an origin story, a discovery — the hook is better chosen by
the shape of the fact itself. These eight cover most of that space:

| Shape | What it does | Example frame |
|---|---|---|
| **Top-three / ranking** | Promises a bounded, complete list | 「三大◯◯の、実はもう一つ」 |
| **Unexpected number one** | Subverts an assumed leader | 「意外な日本一」 |
| **Alias / nickname** | Names a thing the viewer half-knows | 「◯◯が『△△』と呼ばれた理由」 |
| **Head-to-head** | Two known things, one winner | 「AとB、実際どちらが」 |
| **Origin story** | Where something started, against expectation | 「発祥は◯◯ではなかった」 |
| **Number gap** | Two numbers whose distance is the story | 「1年で3人 → 4万人」 |
| **Correcting a misbelief** | Names what the viewer currently believes, then breaks it | 「◯◯は間違いだった」 |
| **Unexpected connection** | Two unrelated things that turn out linked | 「◯◯と△△が繋がっていた」 |

Pick by asking what makes the fact surprising, not by picking a favourite shape and hunting
for a fact to fit it. A ranking hook on a fact whose interest is really a number gap will feel
generic, because the surprise and the frame are pointing in different directions.

*(Carried over from the retired RoamLore video-planning prompt P020, which derived these from
its own performance data. They apply to any discovery/trivia-style video, not only that
project.)*

### Hook Rules

- First 3 seconds of video / first line of text must arrest attention
- Use fragmented, open-ended curiosity — NOT complete fascinations that close the loop
- Be specific: "47,312 women" not "thousands of women"
- Deploy tangible curiosity: hint at what they'll discover without revealing it
- Tell them what it's NOT to intensify what it IS: "It's not a diet... not a pill... not exercise..."
- A single winning hook can run for months. Test constantly.

### The Curiosity Toolbox

**Open Loops** — Create an information gap that can only be closed by clicking. Tease without resolving.

> "I tested 47 headlines. One pattern beat everything else by 3x." (Which pattern?)
> "The formula has three parts. The first is obvious. The third is counterintuitive. But the second? That's where the magic happens." (What's the second?)

**Tangible Curiosity** — Make curiosity concrete and specific, not vague.

Weak: "Discover the secret to weight loss"
Strong: "Discover the 7-second morning trick that targets the fat cells your body forgot about"

**Bucket Brigades** — Transition phrases that maintain momentum and pull forward:
- "But here's the thing..."
- "Here's what I discovered..."
- "This is where it gets interesting..."
- "Wait, it gets better..."
- "And that's not even the best part..."
- "Now here's what nobody tells you..."
- "Which brings me to the real secret..."

Use 2-3 per ad. Every paragraph ending with a bridge gets tiresome.

---

## Intrigue Intensifiers

These techniques make any ad more compelling:

**Tell them what it's NOT:**
> "It's not a diet... not a supplement... not exercise... not willpower..."
> "It's not what your doctor told you. It's not what the internet says."

**Tell them where it's NOT:**
> "You can't find it in any store, any pharmacy, any website..."
> "It's not available in any health food store — and for good reason."

**Drop specific hints:**
> "It's 150 million years old"
> "It's smaller than a nickel"
> "Harvard announced it only last week"
> "It grows only above 12,000 feet in the Andes"

**Authority anchors:**
> "Experts call it..."
> "A study from [institution] proved..."
> "Researchers found..."
> "Over 100 medical reports now show..."
> "3 out of 4 scientists now say..."

## Making the Mechanism Appealing

The mechanism is what makes your solution different from everything else they've tried. The strongest mechanisms are:

- **Credible**: Backed by the most authoritative source possible
- **Exotic/rare**: Hard to find, expensive to produce, newly discovered
- **Small and specific**: "7-second trick" beats "20-minute routine"
- **Simple, fast, easy**: Low perceived effort to get the result
- **Expert-backed**: Someone credible behind the scenes
- **Celebrity-associated**: Known figures connected to it

---

## Proof and Credibility in Ads

Every claim needs support. In short-form ads, proof must be compressed:

- **Specific numbers**: "47,312 customers" not "thousands of customers"
- **Named results**: "Sarah lost 23 lbs" not "our customers love it"
- **Timeframes**: "in 8 weeks" not "fast results"
- **Authority mentions**: Publications, institutions, studies
- **Visual proof**: Before/after, screenshots, product demos
- **Social proof**: User count, review ratings, waitlist numbers

---

## The Teaching Pattern (For Educational Ads)

When selling the solution through education, use this structure to help the prospect understand the problem — so they assume you have the solution:

1. **When things are normal, it's like this** (describe the baseline)
2. **Due to [UNAVOIDABLE FACTOR], the process breaks down** (explain the disruption)
3. **This causes your current symptoms/problems** (connect to their reality)
4. **If unaddressed, it gets worse, plus [other bad things] can happen** (raise stakes)

The prospect thinks: "They clearly understand the problem. They must have the solution." Then your CTA becomes: "Here's what to do about it."

---

## The So What? Chain

For every feature, ask "so what?" until you hit something emotional or financial:

> **Feature:** Fast database
> "So what?" → Queries load in milliseconds
> "So what?" → Users don't bounce, revenue doesn't leak
> "So what?" → You stop waking up stressed about churn

The bottom of the chain is where the ad copy lives. Not "saves 4 hours" but "close your laptop at 5pm instead of 9pm."

Three levels deep. Then write from there.

---

# Writing UGC / Video Ad Scripts

## Format A: Short UGC / Talking Head (15-60 seconds)

The goal: look and sound like a real person filmed this on their phone. NOT a scripted ad.

**Structure:**
```
[HOOK — 0-3s] Pattern interrupt, curiosity question, or bold claim
  [VISUAL: talking to camera, casual setting]

[PROBLEM — 3-10s] Name the pain specifically, make them nod
  [VISUAL: frustrated expression, relatable scenario]

[MECHANISM — 10-25s] Tease the discovery/solution, explain just enough
  [VISUAL: showing product casually, or demonstrating]

[RESULT — 25-40s] Specific transformation, before/after
  [VISUAL: showing results, genuine excitement]

[CTA — 40-60s] Natural close, not salesy
  [VISUAL: direct to camera, genuine recommendation]
```

**Voice rules:**
- First person, conversational — sounds like a real person sharing what worked for them
- Include verbal fillers sparingly ("honestly," "like," "I mean") for authenticity
- Specific details: names, dates, numbers, places — not vague claims
- The CTA should feel like a recommendation to a friend, not a pitch
- Include `[VISUAL DIRECTION]` notes for what should be on screen

## Format B: ADHD Super Hook Ad (3-7 minutes)

In-feed VSLs designed for cold traffic. They never stop hooking.

**Structure:**
```
[RAPID-FIRE HOOKS — 0-30s]
  3-5 different hooks back-to-back, each one an open loop
  Different speakers/angles, fast cuts
  DO NOT close any loops yet

[EDUCATIONAL/MECHANISM — 30s-3min]
  Teaching section: explain WHY the problem exists
  Use the teaching pattern above
  Tease the mechanism throughout — constant "but here's the thing..."
  Pattern interrupts every 30-45 seconds

[PROOF MONTAGE — 3min-5min]
  Testimonial clips with specific results
  Before/after visuals
  Authority mentions (studies, experts, publications)

[CTA — final 30-60s]
  Simple, direct, low-friction
  "Click the link below" or "Tap learn more"
```

**Critical rules:**
- NEVER mention the product by name — sell the click to a VSL/advertorial
- Constant hooks and pattern interrupts throughout — the moment it gets boring, they scroll
- Use fragmented hooks (not complete fascinations that resolve curiosity)
- Multiple speakers/perspectives create variety and social proof simultaneously
- Contrarian claims keep attention: challenge what they think they know

## Format C: Story-Style Video (60-120 seconds)

Personal narrative arc. Most effective for emotional markets.

**Structure:**
```
[HOOK — 0-5s] Start in the middle of the struggle
  "Six months ago, I couldn't even look at myself in the mirror."

[STRUGGLE — 5-20s] Failed attempts, relatable frustration
  "I tried everything — diets, trainers, supplements. Nothing worked."

[DISCOVERY — 20-40s] The turning point, how they found the solution
  "Then my sister sent me this weird article about..."

[TRANSFORMATION — 40-60s] Specific results with numbers and timelines
  "In 8 weeks, I dropped 23 lbs. My husband noticed in the first 2 weeks."

[CTA — 60-90s] Natural recommendation, not a pitch
  "I just wanted to share what actually worked for me. Link's below."
```

## Format D: Research-Grounded Shooting Sheet

When Step 2 produced a template and the user has to actually shoot something, the script alone
is not the deliverable — the shooting sheet is. A script says what the video says; a shooting
sheet says what to point a camera at, and that is the part that stalls projects for weeks.

Write it so someone can execute without a follow-up question:

```markdown
# [Video name] — shooting sheet
**Length**: [from the measured in-niche distribution, not a general rule]
**Who shoots what**: [what needs a real camera vs. what gets assembled in post]

## Setup
| Item | Spec | Why |
[Framing, background, lighting, device state — each tied to the outlier it came from]

## Cut sheet
| # | Action | What is on screen | Seconds |
[Beat by beat, grouped into takes that can be shot in one go]

## Audio
[Narration verbatim, marked already-recorded vs. still-needed. Music and SFX direction.]

## What this resolves
[Map each complaint the user raised to the beat that fixes it]
```

Two things make this land:

**Cite the evidence inline.** "Phone on a desk stand, off-camera hand taps the screen — this is
what the 1.1M-view example does" carries the instruction *and* the reason, so whoever is
shooting can improvise correctly when reality differs from the plan.

**Flag what only they can do.** Real-device footage, their own voice, an account they own — name
those explicitly and separate them from what you will assemble afterwards. A sheet that quietly
assumes the user will produce something they cannot is worse than one that says so up front.

---

# Advertorial Awareness (What Your Ad Feeds Into)

Since many Meta ads send traffic to advertorials, understand the four advertorial types your ad might connect to:

1. **Story-Based** — Personal transformation narrative ("I couldn't move until I tried this 2-inch patch"). Makes it personal, real, and lets the reader live it.
2. **Listicle** — "5 reasons homeowners are switching to..." or "We tested the top 5 and found..."
3. **Editorial/Consumer** — Looks like a news article or editorial review.
4. **eCom Disruptor** — "Small watch company is disrupting the billion dollar industry." Underdog story.

**Match your ad to the advertorial:** If the advertorial is story-based, your ad hook should tease the story. If it's a listicle, your ad can tease the #1 finding. The ad and advertorial should feel like one continuous experience.

---

# Testing & Variation Strategy

## Always Output Variations

Every ad request should produce **3-5 variations** for testing. Label each with its angle:

```
## Variation 1: Curiosity Hook
[Primary Text]
[Headline]
[Description]

## Variation 2: Contrarian Hook
[Primary Text]
[Headline]
[Description]

## Variation 3: Social Proof Hook
...
```

## Testing Hierarchy (In Order of Impact)

1. **Hooks** — THE BIGGEST LEVER. Test 5-10 different hooks with the same ad body
2. **Images/thumbnails** — Different visuals with identical copy
3. **Caption length** — Short click-sellers vs. long story-sellers
4. **Video length** — 2 min vs. 7 min versions of same content
5. **Copy angle** — Different emotional approaches, same creative

## Testing Pattern of Winning Brands

- Control creative runs continuously for months
- New hooks tested constantly (same video body, different openings)
- When a hook wins, it becomes the new control
- Multiple ad sets running simultaneously with different hook/creative combinations
- Very rarely do people buy the first time. Frequency + multiple touchpoints = conversion.

---

# Shareability Principles (STEPPS Framework)

When an ad gets shared organically, your reach multiplies for free. Six principles drive sharing:

1. **Social Currency** — People share what makes them look smart or in-the-know. Use insider language, "secret" positioning, remarkable statistics.
2. **Triggers** — Tie your product to daily rituals ("Every morning when you..."). Frequent mental triggers = frequent sharing.
3. **Emotion** — High-arousal emotions drive sharing: awe, excitement, anger, anxiety. Low-arousal (sadness, contentment) kills sharing.
4. **Public** — Design messages that advertise themselves. Testimonials with real names. "Share your results" CTAs.
5. **Practical Value** — People share useful information. Tips, how-tos, frameworks are inherently shareable.
6. **Stories** — People retell stories, not facts. Embed your message inside a narrative people want to share. Your product must be integral to the story.

---

# Voice & Anti-Patterns

## The Tingle Factor

From Clayton Makepeace: feel your way through ad copy, don't think your way through it. Every sales message is a chain, link by link, to the click. The chain breaks when: the tingle drops (reader gets bored), something feels unbelievable, or clarity is lost.

Read your ad aloud. When the tingle dips at any passage, that's where you rewrite.

## Power Words (Use Liberally)

Amazing, Astonishing, Breakthrough, Discover, Easy, Effortless, First Time Ever, Free, Guaranteed, How To, Hurry, Immediate, Instant, Introducing, Last Chance, Limited, Miracle, New, Now, Proven, Quick, Revolutionary, Secret, Shocking, Simple, Special, Surprising, Truth, Unique, Win, YOU

## Words and Phrases to Ban

**AI tells:** delve, dive into, comprehensive, robust, cutting-edge, utilize, leverage, crucial, vital, essential, unlock, unleash, supercharge, game-changer, revolutionary (when used generically), landscape, navigate, streamline

**Ad cliches:** "click the link in my bio," "you won't believe," "game-changer," "take your X to the next level," "in today's fast-paced world," "are you ready to"

**Wimpy hedging (Makepeace):** can, could, should, might, may, ought to — tell them what it WILL do

**Structural tells:** Every sentence the same length. Every bullet starting the same way. Perfect grammar that sounds written, not spoken. Overly organized with too many headings.

## The UGC Authenticity Test

Before delivering a UGC script, ask: would a real person actually say this out loud, on camera, to their phone? If it sounds like a copywriter wrote it, rewrite it. UGC scripts should feel slightly imperfect — that's what makes them believable.

## Readability

Aim for Flesch-Kincaid Grade 6 or lower. Short sentences. Simple words. If a 12-year-old wouldn't understand it, simplify.

## The Final Check

Before delivering ad copy, verify:

1. Does the first line stop the scroll? Would YOU stop scrolling for this?
2. Is every claim backed by a specific number or proof point?
3. Does it sound like someone talking, or someone "writing copy"?
4. Are there open loops pulling them to click?
5. Is it about THEM (their transformation) or about YOU (your product)?
6. Does the rhythm alternate? (Punchy moments, then breathing room)
7. Would a real person actually say this out loud?
8. Is the CTA benefit-driven, not command-driven?

If any answer is no, rewrite that part.

When Step 2 ran, add two more:

9. Does every structural choice — opening visual, length, audio, cut rhythm, CTA shape — trace
   to something measured, or did some of it come from habit?
10. Did you say plainly where the data contradicted the brief? A pass that only confirms what
    the user already believed either got lucky or did not look hard enough.

## 縦型の短い動画には、さらに4つ

**どれも「音を出して最後まで見てもらえる前提」を捨てるための項目。**

11. **ミュートテスト** — **最初のコマを音なしで見て、何の話で何が困るのかが伝わるか。**
    伝わらないならフックは壊れている。多くの人が音を切ってスクロールしているので、
    音に依存したフックは半分の人にとって存在しない
12. **最初のコマに4〜8語のテキスト** — 1コマ目から置く。**フェードインさせない**
    （1秒かけて出ると、判断の瞬間には間に合わない）
13. **全編に字幕** — 社会動画の85%は音なしで見られる。字幕は視聴時間を押し上げる
14. **セーフゾーン** — 文字と大事なものは**画面の中央80%**に。外側はアプリのボタンや
    説明文に隠れる

⚠️ **音は「あるといい」ではない。**音ありを前提に設計したほうが**コンバージョンが28%高い**
という測定がある。無音の動画を作らない。

（出典: NotebookLM `89f1a888` RoamLore: Remotion × UGC / 46 ソース。2026-08-08 照会。
**このノートには RoamLore 固有の制約も混ざっている**（写真ちょうど3枚・尺6秒など）。
それは Remotion 実装の話なので、他プロジェクトに持ち込まないこと）

---

# Step 4: 採点役に出す（別のエージェント）— **渡す前に毎回**

## 🔴 例外なしの規則

**書いた → 採点役に出す → 結果と一緒に Kazuki へ。この順番に例外はありません。**

「まだ材料が揃っていないから」「どうせ落ちるから」「早く見せたいから」は、
**すべて飛ばす理由になりません。**材料が足りないなら、**成果物を出さずに
「何が足りないか」だけを報告する。**本文を見せた時点で、Kazuki はそれを検品済みだと受け取ります。

⚠️ **周回を節約する工夫が、検品を飛ばす言い訳になっていないかを毎回見る。**
2026-08-08 に姉妹スキル（`buzzy-video-prompt`）で実際に起きた: 「無駄な周回を避けろ」という
注意書きを「採点を飛ばして出してよい」と読み替え、**未検品の成果物を Kazuki に見せた。**

上の Final Check は**自分で自分を採点している。**それでは通らないことが実際に起きた。
書いた本人には、自分の書いたものの穴が見えない。

## 4-1. 作業記録を取りながら書く

Step 2 以降、**ツールを実行するたびにその場で記録する。**あとから思い出して書かない。

| 記録すること | 例 |
|---|---|
| vidIQ の検索 | 検索語 / `descriptionLanguage` の値 / 返ってきた件数 / 使った動画の ID |
| NotebookLM の照会 | notebook の id と名前 / 投げた質問文 / ソース数 |
| コマンド | 実行したコマンドそのままと、出力 |
| **成果物に書いた数字すべて** | 秒数・値段・件数・画面に出す表示（`00:22` など）。**どこから取ったか** |

⚠️ **主張の裏づけでない数字も記録する。**画面に出す小道具の数字（タイマーの値など）は
主張ではないので捏造には当たらないが、**記録に1行あれば疑う余地がゼロになる。**
「この数字はどこから来たのか」を後から誰も辿れない状態を作らない。

**この記録に無いことを「調べた結果」「ソースによれば」と書かない。**
自分の判断で書いたなら、**同じ段落の中で**「これは私の判断で、根拠はない」と書く。
段落を分けて後ろに置くと、読み手は前半を出典つきだと受け取る。

⚠️ **内容が正しそうなときほど危ない。**照会せずに書いたことが後で当たっていると、
指摘されなければ誰も気づかない。**間違っていれば見つかる嘘より、当たってしまう嘘のほうが危ない。**

## 4-2. 採点役を起動する

Agent tool で `ad-copy-auditor` を起動し、次の 4 つを渡す。

| # | 渡すもの |
|---|---|
| 1 | Kazuki の依頼の原文 |
| 2 | 成果物の全文 |
| 3 | **4-1 の作業記録** |
| 4 | 何周目か。2 周目以降は前回落ちた項目番号 |

**3 が無ければ「判定不能」で返ってくる。**採点役は会話を見られないので、
作業記録が唯一の根拠になる。

- **合格** → Kazuki に成果物と採点結果を出す
- **要修正** → 落ちた項目を直して、**もう一度採点役に出す**（同じ採点役を続けて使う）
- **3 周やって通らない** → **止める。**「何周目でどの項目が落ち続けたか」を Kazuki に報告する。
  通っていないものを通ったことにしない

## 4-3. 指摘の受け取り方

⚠️ **落ちた項目番号を「解釈」して範囲を狭めないこと。**
名指しされた 1 か所だけ直して、同じ前提に立つ他の箇所を残さない。

指摘を受けたら、直す前に**「この指摘はどの前提を否定したのか」を一文で書く。**
たとえば「A1 の夜道はわからない」は「A1 を机にする」ではなく
「実写の場所は机に統一する」だった。前提のレベルで受け取ると範囲が正しく出る。
直したあと**同じ語で全文を検索して、残っていないことを確かめてから「直した」と言う。**
波及先が別のファイル（Linear / vault / 生成済みの素材）に及ぶことも見る。

---

# Reference Files

- `references/meta-ad-specs.md` — Character limits, placements, video specs. Read when writing
  for a specific Meta placement.
- `references/vidiq-research.md` — The full Step 2 procedure: exact tool parameters, query
  templates, credit costs, pattern-validity rules. Read before your first vidIQ call.
- `references/dr-principles.md` — Schwartz, Hopkins, Ogilvy, Halbert, Caples, Sugarman,
  Collier, Makepeace in one page. Background reading, not needed for a routine pass.

# 採点役

- `~/.claude/agents/ad-copy-auditor.md` — Step 4 で起動する採点役。
  採点項目（甲・乙・丙）の全文はここにある。**このスキルを直したら、採点役の項目も
  同じ回に見直す。**片方だけ新しくなると、採点が古い基準で通ってしまう。
