---
name: frame-data-chart-nyt
zh_name: "NYT 風データチャートフレーム"
en_name: "NYT-Style Data Chart Frame"
emoji: "📈"
description: "NYT-newsroom 組版 + ずらして見せるアニメーション + 編集品質のチャート（折れ線/棒/レンジ帯）"
category: video
scenario: video
aspect_hint: "1920×1080 (16:9)"
featured: 46
tags: ["data", "chart", "nyt", "editorial", "frame"]
example_id: sample-frame-data-chart-nyt
example_name: "NYT 風折れ線図 · 世界のユーザー数"
example_format: markdown
example_tagline: "編集品質のチャート + ずらして見せる"
example_desc: "8 年の週次アクティブユーザー折れ線 + NYT red accent + 注釈 mono"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · data-chart"
---

【テンプレート: NYT 風データチャートフレーム】
【意図】データ (CSV / JSON / 結論 1 文) を『ニューヨーク・タイムズ』コラム感の単フレーム / アニメーションチャートにする。動画クリップやツイートカード向け。Inspired by hyperframes data-chart。

【キャンバス】1920×1080, 暖白地 `#f7f5ee` または墨黒地 `#0e0e0e` のどちらか; 文字色は背景の反対。

【レイアウト】
- **上部 kicker** (11px uppercase letterspace 0.14em, 色 = accent 赤 `#a91d1d` または mint `#5fb38a`): データ出典 + カテゴリ, 例 "GLOBAL · WEEKLY ACTIVE USERS · 2018–2026"。
- **大きなタイトル** (Cheltenham / Playfair / Source Serif Pro, 5.6vw, italic のサブタイトルは任意): 結論 1 文。**結論はユーザーのデータから抽出する**。図の説明ではない。
- **チャート領域** (キャンバスの 55-65%):
  - 折れ線: 線 1-2 本, 主線 ink 実線 2.5px, 次線 dashed 1.5px; データ点は 6px の塗り円; 要点の横に `2024 · 412M` 黒 mono 小字。
  - 棒: すべて ink 単色、または accent のハイライト棒 1 本; 棒の上に大きな数字; 棒の下のカテゴリは斜体 (Cheltenham italic)。
  - レンジ帯 (range band): 薄い灰の塗り `#e6e2d2` 包絡 + 中線 ink。
- **下部 source + footnote** (10px mono, opacity 0.6): "Source: ユーザーデータ · Chart by html-anything"。
- **ずらして見せるアニメーション**: タイトル fade-in (0s), kicker (200ms), 折れ線 stroke-dashoffset 1.2s ease-out (400ms), データラベルは 100ms 間隔で順に。`prefers-reduced-motion` でオフ可。

【デザインの要点】
- **絶対に**: chart.js / d3 ライブラリは使わない (jsdelivr CDN 導入は除く); 手書き SVG を推奨、inline は 80 行以内。
- フォント: タイトル `Source Serif Pro` または `Cheltenham` (無ければ `Playfair Display`); body `IBM Plex Sans` または `Inter`; データラベル `IBM Plex Mono`。
- 主色 1 つ (ink) + accent 1 つ (NYT red `#a91d1d` / 編集 mint `#5fb38a` / 暖橙 `#d97757` から 1 つ)。
- Y 軸目盛りは hairline + tick 3-4 だけ, ラベルは軸の外側の mono 字。
- 全画面の grid 線、影、3D 立体棒は禁止。emoji は禁止。
- ユーザー提供のデータを使う。入力がテキストの結論なら、妥当な座標を自動で見積もる (ただし "schematic" と注記); CSV/JSON ならそのまま描く。
- 単ファイル HTML; データ点横の注釈形式: `<text class="annot">2024 · 412M</text>`。
