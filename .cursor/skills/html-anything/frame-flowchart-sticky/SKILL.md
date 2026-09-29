---
name: frame-flowchart-sticky
zh_name: "付箋フローチャートフレーム"
en_name: "Sticky Flowchart Frame"
emoji: "📝"
description: "SVG 曲線接続 + 付箋ノード + カーソル操作。ホワイトボード brainstorm のように"
category: video
scenario: operations
aspect_hint: "1920×1080 (16:9)"
featured: 45
tags: ["flowchart", "diagram", "sticky", "whiteboard", "frame"]
example_id: sample-frame-flowchart-sticky
example_name: "付箋フローチャート · ユーザー onboarding"
example_format: markdown
example_tagline: "SVG 曲線 + 4 色付箋"
example_desc: "6 ノードの onboarding フロー、手書き体 + ホワイトボード紙地"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · flowchart"
---

【テンプレート: 付箋フローチャートフレーム (Sticky Flowchart)】
【意図】フロー / システム / ワークフローを「ホワイトボード + 付箋」に描く。onboarding 動画、運用フロー説明、システムアーキテクチャ解説向け。Inspired by hyperframes flowchart。

【キャンバス】1920×1080。背景: ベージュのホワイトボード紙 `#f4ede1` または冷灰のホワイトボード `#f0f2f4`; ごく薄い hex grid `rgba(0,0,0,0.04)` でホワイトボード感を出す。

【ノード (Sticky Notes)】
- 各ノード = 240×180px の付箋 1 枚。色 4 セットをランダム割当: 黄 `#fcd34d` / 桃 `#fca5a5` / ミント `#a7f3d0` / 空 `#a5b4fc`。
- 付箋はわずかに回転 `transform: rotate(±2deg)` で揃えない。投影 `drop-shadow(0 6px 14px rgba(0,0,0,0.12))`, 上部テープ `linear-gradient(...)` の装飾。
- ノード内容: emoji 1 つまたは単線 SVG icon + 大きなタイトル (16-20px) + 説明 1 行 (12px)。
- ノードフォント: `Kalam` / `Caveat` / `Patrick Hand` の手書き感フォント (中国語は `霞鹜文楷` または `LXGW WenKai Screen`)。

【接続線 (SVG)】
- `<path>` Bezier 曲線でノードを繋ぐ, stroke `#2a2a2a`, width 2.5, `stroke-linecap: round`, `stroke-dasharray: 0` (実線) または `8 6` (破線 = 条件分岐)。
- 矢印の端は `marker-end`, 黒い小さな三角矢印。
- 複雑なノードはループや分岐可: 同一ノードから 2 本 (分岐) または 2 本が 1 ノードへ入る (合流)。

【任意のインタラクション】
- 上部 caption (sans, 12px uppercase): "FLOW · MIGRATION · 2026"。
- マウス hover ノード: 影を上げる + scale 1.05, CSS transition。
- 「カーソル」装飾 (`<svg>` arrow + name tag), あるノードの横に浮かせ、figma の共同編集カーソルを模す。

【デザインの要点】
- ノードは最低 5、最大 12。
- ノード配置は全部を中央揃えにしない。ホワイトボードの「適当に貼った」感を残しつつ、接続線は交差せずはっきり。
- 禁止: 全画面の暗い背景、ネオン色、企業 dashboard スタイル。
- フォントに Inter / セリフは使わない。手書き感必須。
- 単ファイル HTML。外部アイコンライブラリは使わない (inline SVG)。
- ユーザーの実フローを使う; ノード文字はユーザー入力から直接。
