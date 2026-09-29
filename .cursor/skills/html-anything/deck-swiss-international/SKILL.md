---
name: deck-swiss-international
zh_name: "スイス国際主義 Deck"
en_name: "Swiss International Deck"
emoji: "🟦"
description: "16 列グリッド + 単一の鮮やかな accent + 固定版面 22 (Klein Blue / Lemon / Mint / Safety Orange)"
category: slides
scenario: marketing
aspect_hint: "16:9 横スライド"
featured: 50
recommended: 2
tags: ["swiss", "grid", "international", "ikb", "editorial", "facts"]
example_id: sample-swiss-international
example_name: "Swiss International · 製品ロードマップ"
example_format: markdown
example_tagline: "Klein Blue IKB + 16 列グリッド"
example_desc: "S01 Cover + S06 KPI Tower の 2 ページプレビュー。IKB 全画面タイトル + 4 本の棒 KPI"
example_source_url: "https://github.com/op7418/guizang-ppt-skill"
example_source_label: "op7418/guizang-ppt-skill"
---

【テンプレート: スイス国際主義 Deck (Swiss International)】
【意図】事実、製品、分析、方法論の表現。極度に冷静、理性、アカデミック。手描き / ノイズ / 装飾は一切なし。Inspired by op7418/guizang-ppt-skill Style B。

【テーマ】**下の 4 セットから 1 つ。混用禁止、hex 変更禁止**:
- 🔵 **Klein Blue (IKB)** — accent `#002FA7`, paper `#fafaf8`, ink `#0a0a0a`. ビジネス / AI / デザインの場面。
- 🟡 **Lemon Yellow** — accent `#FFD500`, paper `#f7f5ee` (淡クリーム), ink `#0a0a0a`. 若年 / リテール / スポーツ。文字は黒必須 (白は不可)。
- 🟢 **Lemon Green / Neon** — accent `#C5E803`, paper `#f7f5ee`, ink `#0a0a0a`. サステナブル / テックスタートアップ / Gen-Z ブランド。文字は黒必須。
- 🟠 **Safety Orange** — accent `#FF6B35`, paper `#f7f5ee`, ink `#0a0a0a`. 工業 / 自動車 / 緊急メッセージ。文字は白 + bold ≥ 600。

【レイアウト — 再利用できる版面プール 22。版面の追加や改造は禁止; **枚数は内容で決める**, 【ユーザーの素材】をすべて覆い終わるまで (短い素材は 6-10 から。長い素材はこの範囲を大きく超える。同じ版面を別の章で繰り返してよい)】
- **S01 Cover** — 全画面 accent + ASCII の呼吸ドットマトリクス + 反転タイトル + メタデータ chrome (date / № / topic)。
- **S02 Vertical Timeline** — 左の破線軸 + 丸点; 右のノード = 年 + KPI + 説明。
- **S03 Statement** — 9.6vw 中央揃えの巨大字 + 左の大きな余白 + 下部 hairline + 注釈。
- **S04 Six Cells** — 2×3 グリッド。各マス: icon + 番号 + 短いタイトル + 1 行の説明。
- **S05 Three Sub-cards** — 左 hero タイトル + 右に水平積みの灰色カード 3 枚。
- **S06 KPI Tower** — 4 列の高さの違う青の棒; 柱の上に icon; 柱の下に大きな数字 + ラベル。
- **S07 H-Bar Chart** — 水平ランキングの横棒。幅がデータを表す。末端に数字。
- **S08 Duo Compare** — 垂直の分割線; 左 Before / 右 After。
- **S09 Closing Manifesto** — 左 IKB ブロック + ASCII ドットマトリクス + 宣言; 右白地 + 要点 3。
- **S10 Dot Matrix Statement** — 中央揃えの宣言 + 角の幾何ドットマトリクス / 円環マトリクス。
- **S11 Horizontal Timeline** — 上部 headline、中部 hairline 軸、等間隔ノード、ノード下にステップ名。
- **S12 Manifesto + Ink Banner** — 上半分 headline + 説明; 下半分全幅の黒バナー + 反転の小さい字。
- **S13 Three Forces Cards** — 左 ink hero ブロック; 右 灰色カード 3 枚。各カード: 大きな数字 + テキスト。
- **S14 Loop Diagram** — 左 番号付きステップ; 右 SVG 同心円; 中心 "LOOP" ラベル。
- **S15 Image Matrix + Hero Stat** — 4×3 等高カード (12 項) + 下部 summary の大きな数字 + ラベル。
- **S16 Multi-card Brief** — 3×2 の小さなカード; 本文は左上、脚注は右下、1 枚を accent ハイライト。
- **S17 System Diagram** — 左 headline + 説明 3 段; 右 SVG 三重同心円 + 外側ラベル。
- **S18 Why Now** — 3 列。各列: category label + headline + 説明 + 下部の数字 (最後の列は accent)。
- **S19 Four Cards** — 上部 accent hairline + headline + 等幅カード 4 枚 (メタデータ / タイトル / 本文)。
- **S20 Stacked KPI Ledger** — 垂直の行 + hairline 区切り; 左 大きな数字 / 中 ラベル / 右 icon。
- **S21 Tech Spec Sheet** — 左 タイトルブロック / 中 KPI hairline 3 / 右 高さの違う柱 / 下 データ。
- **S22 Image Hero** — 上 60% 全幅図 + 白のタイトルブロックを重ねる; 下 40% 説明 + 3 列 KPI。

【デザインの要点 — 絶対ルール】
- **直角だけ**: 最後まで `border-radius: 0`。角丸 = 即違反。
- **1px hairline borders**, 黒または accent; 影 / グラデーション / blur は禁止。
- **16 列グリッド**: `grid-template-columns: repeat(16, 1fr); gap: 0`。
- **書体**: Inter Tight (Latin display) / Inter (body) / Noto Sans SC (中国語) / JetBrains Mono (データ); セリフ禁止、装飾書体禁止。
- **字サイズの極端な対比**: cover は 9.6vw display, body 14-16px, label 11px uppercase letterspacing 0.08em。
- **キーボード ← / → 切替 + hash 同期**; 角の標は固定: `№N/N` 右下, topic ラベル左下。
- **捏造は禁止**: 数字はユーザー入力から。チャートの柱の高さ = 実データを比率どおり。
- 単ファイル HTML を出す。外部画像 URL は使わない; 装飾の幾何 (ASCII マトリクス / 同心円) は純 CSS またはインライン SVG。
