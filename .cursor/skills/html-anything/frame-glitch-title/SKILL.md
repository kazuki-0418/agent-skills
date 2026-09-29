---
name: frame-glitch-title
zh_name: "グリッチアートタイトルフレーム"
en_name: "Glitch Title Frame"
emoji: "⚡"
description: "デジタルグリッチ / 色収差オフセット / データ破損タイトル。動画トランジション / cyberpunk hero 向け"
category: video
scenario: video
aspect_hint: "1920×1080 (16:9)"
featured: 37
recommended: 6
tags: ["glitch", "cyberpunk", "title", "transition", "vfx", "frame"]
example_id: sample-frame-glitch-title
example_name: "グリッチタイトル · SIGNAL_LOST"
example_format: markdown
example_tagline: "cyan / magenta 色収差 + CRT スキャンライン"
example_desc: "巨大タイトル + データ破損のゴースト + 角の ASCII ノイズ chunks"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · glitch"
---

【テンプレート: グリッチアートタイトルフレーム (Glitch Title)】
【意図】単フレーム hero / 動画トランジション / cyberpunk スタイルのタイトル。Inspired by hyperframes glitch。

【キャンバス】1920×1080, 背景 `#070708` ほぼ黒または CRT 暗灰 `#0d0e10`; 56px グリッド (透明 5%) + scanlines 横線 (透明 8%, 2px 間隔)。

【メインタイトル】
- 中央揃え, 6-9vw, weight 800/900, フォント `Space Grotesk Bold` / `Inter Tight Black` / `JetBrains Mono Bold`。
- 色: メイン層 `#f5f5f7`; 後ろにゴースト 2 層:
  - cyan `#00f0ff` translate(`-3px`, `1px`)。
  - magenta `#ff2bd6` translate(`3px`, `-1px`)。
- 全体に clip-path スライス 5-8 段, 各段 `@keyframes` でランダム translateX -10px → 10px, 持続 80-160ms, ずらして再生, "data corruption" 色収差を出す。
- 1.5s ごとに「大グリッチ」 — タイトル全体を horizontal smear 1 frame。`filter: url(#displacementFilter)` または単純な CSS 平行移動。

【追加レイヤー】
- 上部 1 行 caption (uppercase mono, 11px, opacity 0.6): `>> SIGNAL_LOST · CH-04 · 14:32:08`。
- タイトル下にサブタイトル 1 行 (24-28px, mono, opacity 0.7), たまに ` ̶▒̶` 文字に置換 (偽の文字化け)。
- 角にランダムで `█▓▒░` ASCII ノイズ chunks。
- 下部 timecode (mono, opacity 0.4)。
- 画面全体に noise grain 層 `background-image: url("data:image/svg+xml,...turbulence...")`, opacity 6%, mix-blend-mode overlay。

【SVG フィルター (任意)】
- `<filter id="rgbShift">` を定義し `feColorMatrix` + `feOffset` + `feMerge` で R/G/B 3 チャネルをずらす; 全体 `filter: url(#rgbShift)` をグリッチ瞬間に適用。

【デザインの要点】
- 色は次だけ: 黒 / 白 / cyan / magenta / amber 警告色を少し; 虹全体は禁止。
- フォント: 欧文 `Space Grotesk` または `JetBrains Mono` Bold; 中国語 `Noto Sans Mono CJK SC` または `Noto Sans SC` Bold。
- lorem ipsum は禁止; ユーザーのタイトル + サブタイトルを使う。
- モーションは `@keyframes`。`prefers-reduced-motion` でオフ可 (静的 chromatic split に戻す)。
- 単ファイル HTML。
