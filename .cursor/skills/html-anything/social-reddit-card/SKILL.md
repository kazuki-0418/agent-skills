---
name: social-reddit-card
zh_name: "Reddit 投稿カード"
en_name: "Reddit Post Card"
emoji: "🔺"
description: "本物に近い Reddit 投稿カード + 上下投票 + コメント数。動画オーバーレイ / ストーリー共有向け"
category: card
scenario: marketing
aspect_hint: "1280×720 または 800×600"
featured: 42
tags: ["reddit", "social", "card", "overlay", "story"]
example_id: sample-social-reddit-card
example_name: "Reddit 投稿 · r/programming"
example_format: markdown
example_tagline: "Reddit dark mode + vote rail"
example_desc: "AITA 風ストーリー 1 本 + 12.3k upvotes + 1.2k comments"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · reddit-post"
---

【テンプレート: Reddit 投稿カード】
【意図】物語 / 質問 / ネタを Reddit 投稿カードにする。動画オーバーレイ、SNS ストーリー共有向け。Inspired by hyperframes reddit-post。

【キャンバス】1280×720 (動画オーバーレイ) または 800×600 (単カード共有); 背景は透明または暗い `#0b1416`。

【カード構造】
- 外枠: 角丸 16px, bg 白 `#ffffff` (light) または `#1a1a1b` (dark, 動画 overlay 推奨), border 1px `#edeff1` / `#343536`。
- 左側 **vote rail** (40-56px 幅):
  - 上矢印 ▲ (16px, `#878a8c`, hover で橙 `#ff4500`)。
  - 票数 (Inter, 17px, weight 700, 中央揃え, 色: 0 は灰 / 正は橙 / 負は青); 大きな数字は `12.3k` 形式。
  - 下矢印 ▼ (hover で青 `#7193ff`)。
- 本体:
  - 上部 meta row: サブレディットアイコン (CSS 円 + 1文字) + `r/subreddit` (太) + `· Posted by u/username · 3h` (小さな灰色文字)。
  - **タイトル** (Inter / IBM Plex Sans, 22-28px, weight 500, dark text)。
  - 内容: 16px body または引用ブロックまたは図 1 枚 (CSS グラデーションプレースホルダ)。
  - 下部 action row: 💬 `1.2k Comments` · 🏆 Awards · ⤴️ Share · ⋯ icon。
- 上部右上 Reddit Snoo logo (インライン SVG, 橙 `#ff4500`)。

【フォント】
- 主: `IBM Plex Sans` → fallback `Inter`, weight 400/500/700。
- 数字: 同じ主フォント。
- 日本語: `Noto Sans SC`。

【デザインの要点】
- Light mode: bg `#fff`, text `#1c1c1c`, secondary `#7c7c7c`。
- Dark mode (推奨): bg `#1a1a1b`, text `#d7dadc`, secondary `#818384`, border `#343536`。
- 票数の色: 正 = `#ff4500`, 負 = `#7193ff`, 0 = `#878a8c`。
- タイトルのクリック域に控えめな背景 hover を足してよい。
- 外部画像 URL は禁止; 画像プレースホルダは CSS グラデーション + 説明。
- ユーザーが渡した内容を使う; 妥当な subreddit / username / 票数を自動生成。
- 単ファイル HTML; icon はインライン SVG (上下矢印、コメント泡、トロフィー)。
