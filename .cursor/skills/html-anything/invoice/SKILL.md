---
name: invoice
zh_name: "印刷できる請求書"
en_name: "Printable Invoice"
emoji: "🧾"
description: "標準の請求書: 差出/宛先 + 明細 + 税 + 合計 + 支払い案内"
category: finance
scenario: finance
aspect_hint: "A4"
recommended: 13
tags: ["invoice", "bill", "請求書"]
---

【テンプレート: 印刷できる請求書】
【意図】A4 で印刷できる請求書 1 ページ。
【レイアウト】
- Header: 請求書番号 / 日付 / 支払期限
- From / Bill to の 2 ブロック
- Line items table (説明 / 数量 / 単価 / 金額)
- Tax breakdown + Totals (右揃え)
- Payment instructions 区
【デザインの要点】
- @media print スタイル; 色のコントラストは残す
