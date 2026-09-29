---
name: frame-liquid-bg-hero
zh_name: "流体背景 Hero フレーム"
en_name: "Liquid Background Hero"
emoji: "🌊"
description: "WebGL 風の流体ディスプレースメント背景 + 上に名言。動画オープニング / landing hero / ポスター向け"
category: poster
scenario: video
aspect_hint: "1920×1080 (16:9) または 1080×1920 (9:16)"
featured: 39
tags: ["liquid", "fluid", "background", "hero", "html-in-canvas", "vfx"]
example_id: sample-frame-liquid-bg-hero
example_name: "流体背景 Hero · 名言"
example_format: markdown
example_tagline: "Aurora Violet 流体"
example_desc: "多層 radial-gradient の呼吸背景 + difference 文字"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · vfx-liquid-background"
---

【テンプレート: 流体背景 Hero】
【意図】動画オープニングフレーム、SaaS landing 上部 hero、ポスター下地に使える。WebGL の流体感を、CSS / canvas のフォールバックで描き、単ファイルをダブルクリックで開けるようにする。Inspired by hyperframes vfx-liquid-background。

【キャンバス】1920×1080 (横) または 1080×1920 (縦)、どちらか。背景は全面。

【流体背景 — 実装 3 種, ユーザーの好みで選ぶ】
1. **CSS 多層 radial-gradient のずれた呼吸** (最も安定, 既定の推奨):
   - 大きな楕円 `radial-gradient(...)` を 3-5 個、色はパレットから。
   - 各楕円に `@keyframes` の平行移動 + scale + hue-rotate、周期 8-14s、ずらす; 画面全体に `mix-blend-mode: screen` または `overlay`。
   - 最前面に `backdrop-filter: blur(80px)` 1 層で端をさらにぼかす。
2. **Canvas + simple perlin noise** (中級):
   - inline JS 80 行、`requestAnimationFrame` で metaballs または simplex noise field を描く。
   - 性能が許すとき有効。`prefers-reduced-motion` では静的スクリーンショットに落とす。
3. **WebGL fragment shader** (上級, 慎重に):
   - jsdelivr CDN で `regl` を引くか inline plain WebGL。
   - shader は domain-warp noise; quad 1 つ、uniform `u_time` 1 つ。

【最前面の文字レイヤー】
- 中央または左下: 巨大な名言 1 句 (5-7vw, セリフまたは太い sans), フォント: `Source Serif Pro` / `Inter Tight` / `Manrope Black`。
- 文字色は paper white `#fafaf8` または ink、背景の明暗による; `mix-blend-mode: difference` でどの流体色でも読めるようにする。
- サブタイトル (小さな sans, opacity 0.7) 1 行。
- 下部は任意で CTA chip または hairline + メタデータ row。

【カラー — 4 から 1 つ, 虹は使わない】
- 🌅 **Solar Peach** — `#ffb18a` + `#f78b4c` + `#d97757`, 暖かい橙と桃。
- 🌊 **Ocean Aqua** — `#5ac8fa` + `#0a84ff` + `#1e3a8a`, 海の青。
- 🌌 **Aurora Violet** — `#a78bfa` + `#7c5cff` + `#1e1b4b`, オーロラ紫。
- 🌿 **Forest Mint** — `#86efac` + `#34d399` + `#065f46`, 苔の森。

【デザインの要点】
- 禁止: 多色の虹 (>4 色相)、PowerPoint グラデーション、ネオン蛍光の重ね。
- フォント: 中国語は `Noto Serif SC` (display) / `Noto Sans SC` (サブタイトル)。
- 外部画像は禁止; すべて CSS + SVG + 任意 canvas。
- ユーザー提供の名言 / タイトルを使う; 入力がデータなら ≤ 18 字の名言 1 句に抽出。
- 単ファイル HTML, `prefers-reduced-motion` でモーションを切れる。
