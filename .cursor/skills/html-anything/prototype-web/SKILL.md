---
name: prototype-web
zh_name: "Web プロダクトプロトタイプ"
en_name: "Web Prototype"
emoji: "🛠️"
description: "クリックできる機能的な Web プロトタイプ。ナビ、ヒーロー、機能、CTA を含む"
category: prototype
scenario: design
aspect_hint: "1440×900 デスクトップ"
tags: ["prototype", "landing", "プロトタイプ"]
example_id: sample-prototype-inkstack
example_name: "Web プロトタイプ · SaaS Landing"
example_format: markdown
example_tagline: "クリックできる SaaS ランディング一式"
example_desc: "Hero / Features / How / Voices / Pricing / Footer を一度に"
---

【テンプレート: Web プロダクトプロトタイプ】
- 完成した製品 landing page を出す。
- Sections: Top Nav (logo + ナビ + CTA ボタン) → Hero (大タイトル + サブタイトル + 双 CTA + 可視化プレースホルダ) → Features (特性カード 3-6) → How it works (ステップ) → Social proof (logo wall / 評価) → Pricing (任意) → Footer。
- 現代 SaaS のデザイン傾向: 大サイズ、柔らかいグラデーション、glassmorphism カード、スクロールで入る入場アニメーション (pure CSS でよい)。
- レスポンシブ: モバイルは 1カラム, デスクトップは複数カラム; 少なくとも `md:` ブレークポイントを処理。
- インタラクション: nav スクロールで色が変わる; 特性カード hover で浮く; FAQ はアコーディオン (`<details>`)。
- 高忠実度プロトタイプ。"明日リリースできる" と感じさせる。
