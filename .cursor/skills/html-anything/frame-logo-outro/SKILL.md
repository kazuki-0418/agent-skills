---
name: frame-logo-outro
zh_name: "ブランド Logo アウトロフレーム"
en_name: "Logo Outro Frame"
emoji: "🎬"
description: "Logo をブロック組み立てで入場 + glow bloom + tagline の開示。動画エンディング / ブランドクローズ向け"
category: video
scenario: video
aspect_hint: "1920×1080 (16:9)"
featured: 40
recommended: 8
tags: ["logo", "outro", "branding", "end-card", "frame"]
example_id: sample-frame-logo-outro
example_name: "ブランド Logo アウトロ · HTML Anything"
example_format: markdown
example_tagline: "Midnight Indigo + glow bloom"
example_desc: "Logo 組み立て + ブランド名 + tagline + CTA。動画エンディング用"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · logo-outro"
---

【テンプレート: Logo アウトロフレーム (Logo Outro)】
【意図】動画末尾のブランド reveal フレーム —— logo をブロック組み立て + glow bloom + tagline 浮上 + CTA。Inspired by hyperframes logo-outro。

【キャンバス】1920×1080, 黒 `#08090c` またはブランドの暗い背景; 微妙な vignette `radial-gradient(...)` で中心を明るく。

【レイアウト】
- **中心 Logo**: CSS / インライン SVG で描く; 幾何ブロック 4-8 個 (円 / 四角 / 三角 / hairline) で構成。
  - 入場アニメーション: 各ブロックが画面外からスライドイン (±100px で方向が違う) + scale 1.4→1.0 + opacity 0→1, 80ms ずらす; 総時間 1.2s。
  - 入場完了後、logo 全体に glow bloom: `filter: drop-shadow(0 0 24px <accent>40)`; 同時に shimmer `mask-image` が logo を横に一掃 (500ms)。
- **ブランド名**: logo の下 6-8% 位置, 大きな字 (Inter Tight / SF Pro Display, 48-72px, weight 700, letter-spacing -0.02em), 入場: typewriter or fade-up after logo bloom (1.4s 開始)。
- **Tagline**: ブランド名の下 1 行 (24-28px, weight 400, opacity 0.7), fade in (1.8s)。
- **下部 CTA + メタデータ**: 2 行の下部 row, 例 `htmlanything.dev · @htmlanything · 2026`, 11px uppercase letter-spacing 0.16em, 色 opacity 0.4, hairline 区切り。

【カラー — 4 から 1 つ, 混ぜない】
- 🌌 **Midnight Indigo** — bg `#08090c`, accent `#7c5cff` (ネオン紫青 glow)。
- 🌅 **Solar Amber** — bg `#0e0a08`, accent `#ffb547` (暖琥珀)。
- 🌿 **Forest Mint** — bg `#0a1410`, accent `#5fb38a` (ミント緑)。
- ⚪ **Bone & Ink** — bg `#f1efea`, accent `#0a0a0b` (neon なし, editorial 寄り, glow は影に変える)。

【デザインの要点】
- **絶対に**: 外部リンクの logo 画像は使わない; logo は純 CSS / インライン SVG の幾何で描く。
- 入場アニメーションは `@keyframes` + `animation-delay`; `prefers-reduced-motion` でオフ可。
- フォント: 欧文 `Inter Tight` / `SF Pro Display` / `Manrope`; 中国語 `Noto Sans SC` weight 700。
- ユーザー提供のブランド名 + tagline を使う; 無ければ fallback "HTML Anything" / "Anything → beautiful HTML"。
- 単ファイル HTML; アニメーション完了後は freeze (loop しない。動画末尾フレーム)。
- 上部は任意で 5px ribbon (accent 色) を足してブランド識別を上げる。
