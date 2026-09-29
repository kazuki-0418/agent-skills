---
name: frame-light-leak-cinema
zh_name: "フィルムライトリーク映画フレーム"
en_name: "Light-Leak Cinematic Frame"
emoji: "🎞️"
description: "フィルムのライトリーク + 粒状ノイズ + 16:9 letterbox + セリフ大文字。映画的な開き / 章カード"
category: video
scenario: video
aspect_hint: "2.39:1 letterbox (1920×800) または 16:9 (1920×1080)"
featured: 36
tags: ["cinema", "film", "light-leak", "grain", "letterbox", "frame"]
example_id: sample-frame-light-leak-cinema
example_name: "フィルムライトリーク · REEL 03"
example_format: markdown
example_tagline: "暖橙ライトリーク + 35mm 粒状"
example_desc: "2.39:1 letterbox + セリフ斜体の大きな字 + フィルムのパーフォレーション"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · light-leak"
---

【テンプレート: フィルムライトリーク映画フレーム】
【意図】ドキュメンタリー / 個人短編 / 動画の章カード用の開き単フレーム —— 暖橙ライトリーク + 35mm 粒状 + セリフの大きな字、古典フィルムの質感。Inspired by hyperframes light-leak。

【キャンバス】
- **2.39:1 letterbox** (推奨): 1920×800, 上下黒帯 各 140px (`#000`)。
- または 16:9: 1920×1080, letterbox なし。

【背景】
- 下層: 深い暖色 (深い赤茶 `#1a0d08` / 深緑 `#0a1410` / 青紫 `#0d0e1a`) または場面描写 (CSS gradient で空 / 室内 / 屋外を模す)。
- **フィルムライトリーク (Light Leak)**: 大きな `radial-gradient(ellipse at top right, #ffb547 0%, transparent 50%)` を 2-3 + 下部 `linear-gradient(to top, #d97757 0%, transparent 30%)` 1 つ; 色は暖橙 / 桃 / ローズ / 暗い黄, **冷たい青は使わない**。
- **35mm Grain**: 全画面に SVG turbulence noise レイヤー, opacity 14%, `mix-blend-mode: overlay`; `background-image: url("data:image/svg+xml,...feTurbulence...")` でも可。
- 任意: `feDisplacementMap` 1 本でフィルムの揺れを模す (慎重に)。

【文字】
- 中央または左下: 大きなセリフ (Source Serif Pro / Playfair Display / EB Garamond) 5-8vw, weight 500 italic; 色は暖白 `#f5e9d6` または cream。
- サブタイトル (24-28px) 1 行, opacity 0.7, 同じセリフ。
- 角 caption (uppercase letterspace 0.18em, 10-11px, mono, opacity 0.5): "REEL 03 · CH I · 1985"。
- 下部 timecode + 撮影地 + 日付 (mono, opacity 0.4)。

【任意の追加】
- 「フィルム傷」: 1-2px の縦白線を数本, opacity 0.2, 不規則な間隔 (`box-shadow` の多重 inset または複数 `<div>`)。
- 「フィルムのパーフォレーション」: letterbox 黒帯の中に等間隔の小さな白四角 (CSS repeating-linear-gradient)。
- 入場モーション: 画面全体が underexposed (brightness 0.3) → normal、800ms 内; ライトリーク位置は 12s 周期でゆっくり漂う。

【デザインの要点】
- 色相は 4 つまで (深い背景 + 暖色ライトリーク 2 + 文字 cream)。
- 禁止: 青紫ライトリーク (フィルム質感に反する)、emoji、ネオン色、幾何 dashboard 装飾。
- 中国語: `Noto Serif SC` italic は無い → `Noto Serif SC` regular + 字間を広げる。
- ユーザー提供のタイトルを使う; 「年 / 章 / 場所」メタデータは妥当に見積もる (ただし出典はユーザーの素材)。
- 単ファイル HTML, `prefers-reduced-motion` でモーションを切る。
