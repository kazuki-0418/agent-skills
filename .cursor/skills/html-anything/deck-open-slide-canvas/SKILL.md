---
name: deck-open-slide-canvas
zh_name: "1920 キャンバス自由 Deck"
en_name: "Open-Slide 1920 Canvas Deck"
emoji: "🎨"
description: "1920×1080 キャンバスに固定。React コンポーネント単位で自由配置。テンプレートに縛られない"
category: slides
scenario: design
aspect_hint: "1920×1080 (16:9)"
featured: 35
recommended: 9
tags: ["canvas", "open-slide", "freeform", "1920", "react"]
example_id: sample-deck-open-slide-canvas
example_name: "1920 自由キャンバス · Sea Indigo"
example_format: markdown
example_tagline: "1920×1080 に固定 + 自由な組み合わせ"
example_desc: "Sea Indigo パレット + 1 ページ大文字 question + 角の標"
example_source_url: "https://github.com/1weiho/open-slide"
example_source_label: "1weiho/open-slide"
---

【テンプレート: 1920 キャンバス自由 Deck】
【意図】テンプレートに縛られたくない場面 (個人ポートフォリオ、変わった講演、アート / デザイン授業の deck)。固定 1920×1080 キャンバス + かなり強いタイプ / 配色の拘束を渡し、agent が React コンポーネントを書くように中身に合わせて各ページを自由に置く。Inspired by 1weiho/open-slide。

【必須の技術仕様】
- キャンバス: 各ページは厳密に `width: 1920px; height: 1080px;`。`transform: scale(...)` でビューポートに合わせる (既定 `scale(0.7)` 中央)。
- **overflow は絶対禁止**: 各ページの中身は 1920×1080 に fit させる。スクロールバーは出さない。
- 字サイズ type scale (px): `2xs:18 · xs:22 · sm:28 · md:36 · lg:48 · xl:64 · 2xl:88 · 3xl:120 · 4xl:160 · 5xl:220`。
- 余白 padding: 96 / 128 / 160 の 3 段から 1 つ。
- 各ページに `<section class="slide" data-slide-id="<n>">`。

【パレット — deck ごとに 1 セット。最後まで変えない】
- 🌫 **Ash & Lime** — bg `#f1efea`, ink `#161616`, accent `#c5e803`。
- 🌌 **Sea Indigo** — bg `#0a0e1a`, ink `#f5f5f7`, accent `#5ac8fa`。
- 🧉 **Mate Mocha** — bg `#1a1411`, ink `#f5e9d6`, accent `#d97757`。
- 🌸 **Pearl Rose** — bg `#fdf6f3`, ink `#1a1015`, accent `#ff5d8f`。

【レイアウトの自由度 — ここが核】
- テンプレートは強制しない。各ページは**中身の性質**でレイアウトを選ぶ: cover / question / quote / image-text / 3 列 / 5 列 / リスト / データカード / 全面図。
- ただし各ページは**規則 1 つを守る**: 視覚の重心 (visual hierarchy) は 1 つだけ — 名言 1 文、数字 1 つ、図 1 枚。「何もかも強調」はしない。
- 対等な文章を 2 段詰め込まない; 本当に並列なら 3 列の等ウェイトグリッドにする。

【書体】
- 欧文: `Inter Tight` (display) + `Inter` (body); または `Source Serif Pro` (editorial 調のとき)。
- 中国語: `Noto Sans SC` (sans 調) または `Noto Serif SC` (editorial 調); sans + serif を混ぜない。
- mono: `JetBrains Mono` をデータ / タイムスタンプに。

【デザインの要点】
- emoji 装飾は禁止 (本文中のものは可); 多色の虹は禁止; accent は 1 色だけ。
- SVG icon に lucide / feather などの汎用ライブラリを当てない (inline SVG を自分で書く)。
- キーボード ← / → 切替 + hash 同期を付ける; 角の標は固定: 右下 `№N/M`, 左下 deck title。
- ユーザーの実内容を使う; lorem ipsum は禁止。
- 単ファイル HTML; Tailwind CDN; 画像の外リンクは使わない。
