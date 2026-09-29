---
name: ppt-keynote
zh_name: "Keynote 風 PPT"
en_name: "Keynote-style Slides"
emoji: "🎬"
description: "Apple Keynote 級のスライド。1 画面 1 カード。キーボード左右で切替"
category: slides
scenario: marketing
aspect_hint: "16:9 (1280×720)"
featured: 19
tags: ["slides", "deck", "presentation", "スライド", "プレゼン"]
example_id: sample-ppt-html-anything
example_name: "Keynote PPT · 製品紹介"
example_format: markdown
example_tagline: "スライド 7 枚で製品を言い切る"
example_desc: "Apple Keynote 風の製品紹介, ←/→ で切替"
---

【テンプレート: Keynote 風 PPT】
- 各スライドは `<section class="slide">`。全体幅 1280 高さ 720, 中央揃え, 背景グラデーション。
- 1 ページの中身は極簡: 大タイトル + 支持テキスト 1-3 行; またはデータ図 1 枚; または名言 1 つ。
- サイズ: タイトル `text-7xl font-semibold tracking-tight`, サブタイトル `text-2xl text-neutral-500`。
- 1 ページ目はカバー (テーマ + 登壇者 / 日付), 最後は "Thanks." または行動喚起。
- 上部右上の小さなインジケータ: 現在ページ / 総ページ数。
- JavaScript で ArrowLeft / ArrowRight / スペースキー切替; hash (#/3) も同期。
- ページ間は fade-in アニメーション。
- 余白を保つ。データカードは grid で揃える。色は抑える。
