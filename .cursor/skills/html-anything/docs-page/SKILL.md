---
name: docs-page
zh_name: "技術ドキュメントページ"
en_name: "Docs Page"
emoji: "📘"
description: "3 カラムのドキュメントページ: サイドナビ + 本文 + 右 TOC"
category: doc
scenario: engineering
aspect_hint: "デスクトップ 1440"
tags: ["docs", "api", "tutorial", "guide"]
---

【テンプレート: 技術ドキュメントページ】
【意図】API / チュートリアルドキュメントの単ページ。長文の読みやすさを優先。
【レイアウト】
- Inline-start nav (sections + sticky)
- Article body (コードブロック、callouts、表を含む)
- Inline-end TOC (sticky, scroll-spy)
- トップバー search + version + テーマ切替
【デザインの要点】
- コードブロック: 角丸 + dark + 言語ラベル + コピーボタン
- callout: info / warn / danger の 3 色
