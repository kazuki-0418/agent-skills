---
name: deck-guizang-editorial
zh_name: "貴賛編集インク Deck"
en_name: "Guizang Editorial E-Ink Deck"
emoji: "🖋️"
description: "電子雑誌 × 電子インク。版面 10 + パレット 5（インク / 藍磁 / 森の墨 / クラフト紙 / 砂丘）"
category: slides
scenario: marketing
aspect_hint: "16:9 横スライド"
featured: 49
recommended: 1
tags: ["editorial", "e-ink", "magazine", "narrative", "guizang"]
example_id: sample-guizang-editorial
example_name: "貴賛編集インク · 章の扉"
example_format: markdown
example_tagline: "インククラシックパレット + セリフ display"
example_desc: "L02 Act Divider 章の扉 + L03 Big Numbers Grid データグリッド, 紙の印刷感"
example_source_url: "https://github.com/op7418/guizang-ppt-skill"
example_source_label: "op7418/guizang-ppt-skill"
---

【テンプレート: 貴賛編集インク Deck (Editorial × E-Ink)】
【意図】物語、視点、共有、個人のスタイル表現。墨と紙の印刷感。テック感は使わない。Inspired by op7418/guizang-ppt-skill Style A。

【パレット — 5 から 1 つ。hex の変更は禁止、混用は禁止】
- 🖋 **インククラシック Monocle** — ink `#0a0a0b`, paper `#f1efea`, paper-tint `#e8e5de`, ink-tint `#18181a`. 既定 / 汎用ビジネス / テック。
- 🌊 **藍磁 Indigo Porcelain** — ink `#0a1f3d`, paper `#f1f3f5`, paper-tint `#e4e8ec`, ink-tint `#152a4a`. テック / 研究 / データ。
- 🌿 **森の墨 Forest Ink** — ink `#1a2e1f`, paper `#f5f1e8`, paper-tint `#ece7da`, ink-tint `#253d2c`. 自然 / サステナブル / 文化。
- 🍂 **クラフト紙 Kraft Paper** — ink `#2a1e13`, paper `#eedfc7`, paper-tint `#e0d0b6`, ink-tint `#3a2a1d`. ノスタルジー / 人文 / 文学。
- 🌙 **砂丘 Dune** — ink `#1f1a14`, paper `#f0e6d2`, paper-tint `#e3d7bf`, ink-tint `#2d2620`. アート / デザイン / ファッション。

【レイアウト — カセット式の版面プール 10。再利用可; **枚数は【ユーザーの素材】で決める**, 要点をすべて覆う; 短い素材は 6-12 から。長い素材は枚数を増やす (同じ版面を別の章で繰り返してよい)】
- **L01 Hero Cover** — 中央揃えの大きな字 hero typography + kicker + subtitle + lead paragraph + 下部メタデータ row。
- **L02 Act Divider** — kicker + 8.5-10vw の巨大 headline + 引用 1 文; 章の切替では反転色にしてよい (ink ↔ paper)。
- **L03 Big Numbers Grid** — 3×2 データカード (label / 大きな数字 / 注釈)。
- **L04 Quote + Image** — 左 kicker + headline + body + callout; 右 16:10 図 (ベースライン揃え。baseline であり top ではない)。
- **L05 Image Grid** — 3×2 または 3×1 の等高図グリッド (26vh または 22vh); 高さは厳密に揃える。
- **L06 Pipeline / Flow** — 横方向の番号付きステップ群。各ステップ: №X + タイトル + 説明; キーボードで段階送りできる。
- **L07 Hero Question** — 7vw 全画面の問い 1 文。意味で改行。周囲は極簡。
- **L08 Big Quote** — 5.8vw 巨大セリフ引用 + 英語訳 + 署名 + 日付。
- **L09 Before / After** — 1:1 split; 左列 opacity .55 (旧/before); 右列 full brightness (新/after)。
- **L10 Mixed Media** — 8:4 比率; 左に長文 (kicker / headline / body / callout) + 右 3:4 縦図を補助に。

【デザインの要点】
- **禁止**: グラデーション / drop-shadow / 角丸 / 円の装飾 / blur / SVG アイコンライブラリ / emoji 装飾。
- **書体**: Display は `Playfair Display` (英) / `Noto Serif SC` (中); Body は `Inter` / `Noto Sans SC`; 番号 / 数字は italic セリフを時々使ってよい。
- **雑誌感のディテール**: kicker は 11px uppercase letterspacing 0.12em; folio は右下 `01 / 12`; 上部の細い hairline rule + 誌の logo / topic。
- **禁止**: データの捏造、Lorem ipsum、プレースホルダ画像 URL。図はすべて純 CSS / SVG のインラインで描く (色面 + 簡筆)。
- キーボード ← / → で切替; hash 同期; 単ファイル HTML。
