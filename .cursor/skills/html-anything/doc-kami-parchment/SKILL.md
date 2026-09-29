---
name: doc-kami-parchment
zh_name: "Kami 羊皮紙ドキュメント"
en_name: "Kami Parchment Document"
emoji: "📜"
description: "暖色の羊皮紙地 (#f5f4ed) + 墨藍の単色 accent (#1B365D) + セリフ 1 書体。編集品質の組版"
category: doc
scenario: personal
aspect_hint: "A4 / Letter の縦長ページ"
featured: 48
recommended: 3
tags: ["kami", "parchment", "serif", "editorial", "report", "letter", "one-pager"]
example_id: sample-kami-parchment
example_name: "Kami 羊皮紙 · One-Pager"
example_format: markdown
example_tagline: "暖色羊皮紙 + 墨藍単色 + セリフ 1 つ"
example_desc: "1 ページの Open Design Studio Issue №26 編集品質 one-pager"
example_source_url: "https://github.com/tw93/kami"
example_source_label: "tw93/kami"
---

【テンプレート: Kami 羊皮紙ドキュメント】
【意図】本格的な組版ドキュメント: one-pager / 長文レポート / 手紙 / 履歴書 / 決算 / changelog / portfolio。Inspired by tw93/kami。「組版された紙のように書く」ことが要点。dashboard ではない。ウェブページではない。

【必須の視覚シグネチャ — 変更禁止】
- **キャンバス**: 暖色羊皮紙 `#f5f4ed` (純白 `#fff` は使わない)。副背景 `#efeee5`。
- **墨色**: 主文字 `#1f1d18` (ほぼ黒の暖色グレー。純黒 `#000` は使わない)。副文字 `#6b665b`。
- **唯一の色彩**: 墨藍 `#1B365D` ——すべての accent (リンク、tag の線、重点数字、引用の左 rule) はこの色だけ。多色は禁止。
- **フォント**: 言語ごとにセリフ 1 つ。全文で混ぜない:
  - 英語: `Charter` (fallback: `Source Serif Pro`, `Iowan Old Style`)
  - 中国語: `TsangerJinKai02 W04` (fallback: `Noto Serif SC`)
  - 日本語: `YuMincho` (fallback: `Noto Serif JP`)
  - Body 400, Heading 500 (700/800/900 は使わない)。
- **行高**: タイトル 1.1–1.3, コンパクトな本文 1.4–1.45, 読み物の本文 1.5–1.55。
- **絶対に**: drop-shadow / blur / 角丸 ≥ 8px / グラデーション / ネオン色 / rgba (solid hex を使う)。
- **細部**: tag は solid hex 背景の四角 (WeasyPrint は rgba の描画が弱いため); 単線の幾何 icon; 端の 1px hairline `#d4d1c5` rule, 長さは端まで届かないよう抑える。

【任意のドキュメントタイプ — ユーザーの素材で判断】
- **One-Pager** — 上の logotype (Charter italic) + タイトル + lede + 3 列の要点 + フッター metadata。
- **Long Doc** — カバーページ (大タイトル + サブタイトル + 著者 + 日付) → 目次 (kicker + page no.) → 章 (folio を角上 + section rule + body) → 注釈の脚注 + 末尾 colophon。
- **Letter** — レターヘッド住所 + 日付 + 宛先 + 本文 (左揃え, 段落間 1.5em) + 署名 + サインのプレースホルダ線。
- **Portfolio** — プロジェクト hero (大タイトル + sub) + 全幅図 1 枚 (CSS ブロックでプレースホルダ) + プロジェクト説明 + ロール / 時期 / stack のメタデータ row。
- **Resume** — 上部の氏名 (大きな字) + tagline 1 行 + contact row + 主要 section: experience (会社 / 時期 / 職位 / bullets) + skills + education。
- **Slides** — keynote 風。ページ数は【ユーザーの素材】で決める (短い素材は 6 ページから。長い素材は枚数を増やす)。各ページは羊皮紙で全面。大タイトル + lede + 角の page no.。「印刷された紙」だけが残る簡潔さ。
- **Equity Report** — 会社名 + ticker + Q × 年 + key metrics row (revenue / margin / yoy) + body の分析 + チャート (SVG 単色折れ線)。
- **Changelog** — バージョン番号 (Charter italic の大きな字) + 日付 + 変更リスト (Added / Changed / Fixed), 単一 rule で区切る。

【デザイン基準】
- "Composed pages, not dashboards." KPI カードを積まない。emoji アイコンを積まない。hero gradient は使わない。
- "Ring or whisper only, no hard drop shadows." 影は `0 0 0 1px #d4d1c5` のような hairline の線だけ。
- 文字の階層は**セリフの対比 + 字サイズ + 余白**で作る。色では作らない。
- 単ファイル HTML, Tailwind CDN を使う; 全文が CJK と英字の混在のときは和欧間スペースを入れる; 外部画像は使わない。プレースホルダは paper-tint の色ブロック + 1px ink の線。
