---
name: data-report
zh_name: "データ可視化レポート"
en_name: "Data Visualization Report"
emoji: "📊"
description: "CSV/Excel/JSON のデータを、きれいな可視化レポートページにする"
category: data
scenario: finance
aspect_hint: "デスクトップ縦長ページ"
featured: 10
tags: ["data", "report", "chart", "データ", "レポート"]
example_id: sample-data-weekly-report
example_name: "データレポート · 週報"
example_format: csv
example_tagline: "KPI カード + Chart.js チャート + 表"
example_desc: "9 か月の成長データを自動で可視化レポートにレンダー, Chart.js をインライン"
---

【テンプレート: データ可視化レポート】
- 頭部: レポートタイトル + 期間 + データ出典の説明。
- KPI カードグリッド: 最も重要な指標 3-5, 各カードは数値 + 前年同期変化 + ミニトレンド線を表示。
- 主チャートエリア: 少なくともチャート 2 つ (棒 / 折れ線 / 円 / 散布), Chart.js または ECharts を使う (jsdelivr CDN で導入), データはユーザー入力から解析する。
- **チャート容器には固定高さが必須**: 各 `<canvas>` の外側を `<div style="position:relative;height:NNNpx">` で包む (KPI ミニ図 ~40px, 主チャート ~240–280px)。Chart.js が `responsive:true, maintainAspectRatio:false` のとき、親容器に明示高さが無いと ResizeObserver の無限ループに入り、チャートが無限に高くなってブラウザが固まる。**canvas に `height=` 属性をレイアウトとして直接書いてはいけない**, それは初期値にすぎない。
- データ表: ユーザー原データの抜粋, `<table>` + 現代的なスタイル (zebra stripe, hover, sticky header)。
- 洞察ブロック: 文章の洞察 3-5 条, emoji で始め, プロダクト週報のように。
- 下部「方法論」折りたたみエリア。
- 配色は抑制しプロらしく: 主色 1 + 中性の色階, チャートはパレットを使う。
- **ユーザーが提供した実データを必ず解析する**, 捏造しない。
