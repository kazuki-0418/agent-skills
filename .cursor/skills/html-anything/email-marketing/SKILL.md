---
name: email-marketing
zh_name: "マーケティングメール"
en_name: "Marketing Email"
emoji: "📧"
description: "製品リリースメール。masthead、hero、CTA、仕様表、table-fallback を含む"
category: email
scenario: marketing
aspect_hint: "600 メール幅"
featured: 7
tags: ["email", "newsletter", "mjml"]
---

【テンプレート: ブランド製品リリースメール】
【意図】純 HTML メール、600px 1カラム、メールクライアント互換。
【レイアウト】
- Masthead (wordmark 中央揃え)
- Hero 図ブロック (SVG プレースホルダ)
- Headline lockup (skewed-italic accent を含む)
- Body copy + primary CTA ボタン
- Specifications grid (3 列)
- Footer (SNS + 配信停止)
【デザインの要点】
- `<table role='presentation'>` でレイアウトのフォールバック
- 色は inline style (class に依存しない)
