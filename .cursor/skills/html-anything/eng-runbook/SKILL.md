---
name: eng-runbook
zh_name: "エンジニアリング Runbook"
en_name: "Engineering Runbook"
emoji: "📕"
description: "サービス概要 + alerts 表 + dashboards + 操作コマンド + on-call + 事故リスト"
category: doc
scenario: engineering
aspect_hint: "縦長ページ"
tags: ["runbook", "ops", "oncall", "sre"]
---

【テンプレート: Engineering Runbook】
【意図】エンジニアリング oncall 用の、コマンドをコピーできる runbook 単ページ。
【レイアウト】
- Service overview (トポロジ + 依存)
- Alerts table (severity / threshold / runbook link)
- Dashboards links カード
- Common procedures (mono コードブロック, ワンクリックコピー)
- On-call rotation (今週 + 来週)
- Incident response checklist
