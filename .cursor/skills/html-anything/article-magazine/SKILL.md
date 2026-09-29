---
name: article-magazine
zh_name: "雑誌記事"
en_name: "Magazine Article"
emoji: "📖"
description: "Substack / Medium の上質な長文レイアウト。公式アカウント・ブログ向け"
category: article
scenario: marketing
aspect_hint: "A4 / 縦長ページ"
featured: 11
tags: ["blog", "essay", "newsletter", "公式アカウント", "ブログ", "記事"]
example_id: sample-article-trq212-html
example_name: "雑誌記事 · HTML が Markdown に取って代わる"
example_format: markdown
example_tagline: "着想は @trq212 のツイート"
example_desc: "「AI 時代は HTML > Markdown」をめぐる延長コメント, 元ツイートの注とクリックできるリンクを含む"
example_source_url: "https://x.com/trq212/status/2052809885763747935"
example_source_label: "@trq212 / x.com"
---

【テンプレート: 雑誌記事】
- 上部 hero: 大タイトル (text-5xl/6xl) + 任意のサブタイトル + 著者 / 読了時間 / 日付のメタデータ。
- 本文: 1カラム, 最大幅およそ 700px, 中央揃え。段落 `text-lg leading-relaxed text-neutral-700 dark:text-neutral-300`。
- H2 / H3 タイトルは serif フォント, 本文とタイトルに視覚対比をつける。
- 引用ブロックは左側の太い accent 色ボーダー + 斜体。
- コードブロック: 角丸 + 暗い背景 + 明るい文字, 言語ラベルを表示。
- リスト項目はカスタム bullet（小さな四角 / accent の丸点）。
- 章のあいだは `<hr>` で区切るが, 見た目は中央揃えの小さな ornament にする。
- 末尾にシンプルな「役に立ったら、シェアしてください」のアクションカードを付ける。
