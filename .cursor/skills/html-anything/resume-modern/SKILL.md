---
name: resume-modern
zh_name: "ミニマル履歴書"
en_name: "Modern Resume"
emoji: "📄"
description: "現代のミニマル履歴書。A4 1 ページ。印刷や PDF 向け"
category: resume
scenario: personal
aspect_hint: "A4 (210×297mm)"
recommended: 12
tags: ["resume", "cv", "履歴書"]
example_id: sample-resume-frontend
example_name: "ミニマル履歴書 · フロントエンドエンジニア"
example_format: markdown
example_tagline: "A4 1 ページ。印刷 / PDF 出力できる"
example_desc: "シニアフロントエンドエンジニアの履歴書。2 カラム。数字の実績をハイライト"
---

【テンプレート: 現代ミニマル履歴書】
- コンテナ幅は A4 相当: `w-[210mm] min-h-[297mm] mx-auto`, 内側余白 16-20mm。
- 上部の氏名は大きく (text-4xl), 下に 1 行 contact (メール / 電話 / 都市 / GitHub / LinkedIn), 間は細い縦線で区切る。
- 本体は 2 カラム任意: 左 60% 主線（経歴/プロジェクト/学歴）, 右 40% 副線（スキル/言語/受賞）。
- 章タイトル: small caps スタイル, 上に短い accent 線 (w-8 h-0.5)。
- 経歴の各条: 会社 + 職位 + 期間 (右揃え), 下に bullet 1-3 を動詞始まりで。
- 派手な色は使わない。黒白灰 + accent 1 (濃い青 / 濃い緑)。
- @media print スタイルを足す。不要な要素は隠す。色は残す。
