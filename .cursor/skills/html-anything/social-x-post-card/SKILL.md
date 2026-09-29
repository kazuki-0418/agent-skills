---
name: social-x-post-card
zh_name: "X (Twitter) 投稿カード"
en_name: "X / Twitter Post Card"
emoji: "𝕏"
description: "本物に近い X 投稿カード + エンゲージメント (likes/reposts/views)。動画オーバーレイや図カード共有向け"
category: card
scenario: marketing
aspect_hint: "1280×720 または 1080×1080"
featured: 44
tags: ["twitter", "x", "social", "card", "overlay"]
example_id: sample-social-x-post-card
example_name: "X 投稿カード · AlchainHust 名言"
example_format: markdown
example_tagline: "X dark mode + エンゲージメント"
example_desc: "名言ツイート 1 本 + 12.3K likes / 1.2K reposts + 青いチェック"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · x-post"
---

【テンプレート: X (Twitter) 投稿カード】
【意図】ツイート内容 (またはユーザーの名言) を本物に近い X 投稿カードにする。動画オーバーレイ、X への図投稿、知識の蓄積向け。Inspired by hyperframes x-post。

【キャンバス】1280×720 または 1080×1080, 暗い背景 `#0f1419` または明るい背景 `#ffffff` (X のテーマに合わせる); カードは中央揃え, 影は柔らかい。

【カード構造】
- 外枠: 角丸 16px, 1px border `#2f3336` (dark) / `#eff3f4` (light), 内側余白 16px。
- 上部 row: アバター (48×48 円, CSS gradient プレースホルダ) + ユーザー名 + handle `@username` + verified 青いチェック + 時刻 (mono, 12px, 灰)。
- 本文: 17-22px, ウェイト 400; リンクは X 青 `#1d9bf0`; hashtag 同色; mention 同色; 段落間の空き 0.6em。
- 任意: 引用カード (小さなカードを内包, 灰背景, 角丸 12px)。
- 任意: 図 1 枚 (CSS グラデーション + 説明プレースホルダ, 外部画像 URL は使わない), 比率 16:9, 角丸 12px。
- エンゲージメント row: icon 4 + 数字 (返信 / リポスト / 引用 / いいね), icon は inline SVG (X 公式スタイル), 灰色, hover で色が変わる。
- 上部右上 X logo 単線 SVG。
- 閲覧数 row: 👁️ + 数字 (小さな文字)。

【フォント】
- 欧文: `Chirp` (X のフォント) → fallback `Inter` または `Segoe UI`。
- 日本語: `Noto Sans SC` / `PingFang SC`。
- 数字: 同じ主フォント。mono は使わない。

【デザインの要点】
- 配色 light: bg `#fff`, text `#0f1419`, secondary `#536471`, border `#eff3f4`, accent `#1d9bf0`。
- 配色 dark (推奨, 動画オーバーレイ用): bg `#000`, text `#e7e9ea`, secondary `#71767b`, border `#2f3336`, accent `#1d9bf0`。
- 数字の形式: 1.2K / 4.5M (生の 1234 は使わない)。
- 内容はユーザー入力から。ツイートを捏造しない。
- ユーザー入力がデータなら → 「名言」ツイート 1 文に自動要約 (≤ 280 文字)。
- 単ファイル HTML; icon はインライン SVG; 外部画像 URL は使わない。
- 任意: カードの背後に控えめな放射ハイライト `radial-gradient(...)` で動画オーバーレイの可読性を上げる。
