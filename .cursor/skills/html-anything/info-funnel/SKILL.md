---
name: info-funnel
zh_name: "ファネル情報図"
en_name: "Funnel Infographic"
emoji: "🪣"
description: "3-6 段の減少ファネル。コンバージョン / フィルタ比率 / 流入ロスを強調。縦図は IG Story / Xiaohongshu 向け"
category: data
scenario: marketing
aspect_hint: "1080×1920 (9:16) 縦画面"
tags: ["funnel", "conversion", "ファネル", "コンバージョン率", "marketing", "infographic", "social", "story"]
example_id: sample-info-funnel-saas
example_name: "ファネル情報図 · SaaS 登録コンバージョン"
example_format: markdown
example_tagline: "5 段 · 生成り + Klein Blue · 大きな数字 + コンバージョン率"
example_desc: "訪問者 → 登録 → トライアル → 有料 → リテンション の 5 段ファネル。左に絶対数、右に段階コンバージョン率。下部は累計ロスの洞察"
example_source_url: "https://github.com/JimLiu/baoyu-skills#baoyu-infographic"
example_source_label: "baoyu-skills · infographic/funnel"
---

【テンプレート: ファネル情報図（Funnel Infographic）】

【意図】「大きいものから小さいものへ」のコンバージョン / フィルタ / ロスの過程を一目で見せる。**広い頂（入力）→ 狭い底（結果）**, 各段に「いくら残ったか」と「いくら漏れたか」を明示する。典型シーン：marketing funnel（露出→クリック→登録→有料）、採用ファネル（応募→面接→内定→入社）、意思決定ファネル（候補→フィルタ→確定）。

【データの形】

入力は順序付きの **3-6 段** + 各段の絶対値（人数 / 件数 / 金額）。各段の名前、説明、単位は任意。ユーザーが割合だけ渡した場合、既定の頂 = 100% / 10000 人。

```
段階 1: 100,000 名の訪問者
段階 2:  18,500 名の登録（18.5%）
段階 3:   6,200 名がトライアル開始（33.5%）
段階 4:   1,450 名が有料化（23.4%）
段階 5:     920 名が 30 日リテンション（63.4%）
```

【レイアウト規則】

| 領域 | 内容 | 割合 |
|---|---|---|
| **Hero 上部**（約 15%） | タイトル（≤ 20 字, 22-32px CJK）+ サブタイトル / 時間窓（灰色 14-16px） | 上 15% |
| **ファネル本体**（約 65%） | 3-6 個の台形 stage。各段: 左の大きな数字（48-72px tabular-nums）+ 右の段階名（18-22px bold）+ 右の 2 行説明（13-15px 灰）+ 段間の小さな矢印でコンバージョン率 | 中 65% |
| **下部 stat strip**（約 20%） | 累計コンバージョン率（最大字サイズ 80-120px）+ 洞察テキスト 1-2 文（ロスが最も大きい段 / 要点） | 下 20% |

【ファネルの実装】

**CSS `clip-path: polygon()`** で台形を切る。SVG は使わない：
- 各段 stage は `<div>` 1 つ。固定 height（120-200px）+ それぞれ異なる clip-path
- clip-path の左右の縮み = 50% × `(1 - bottom_width_ratio)`。累計で各段は一段上より狭い
- 各段の背景は同じ hue で lightness を変える。頂が最も飽和、底が最も深い（accent → ink）
- 段の間に 4-8px gap を置き、「流れ」をはっきりさせる
- 数字は `font-variant-numeric: tabular-nums`, letter-spacing `-0.02em`

【テーマ色 — 3 から 1 つ, 混ぜない】

| テーマ | 向いている | 頂 | 底 | ink | paper |
|---|---|---|---|---|---|
| **klein-blue**（既定） | ビジネス / SaaS / AI 製品 | `#4F7BD8` | `#002FA7` | `#0A0A0A` | `#FAFAF8` |
| **sunset-amber** | 小売 / 消費 / 飲食 | `#FBB040` | `#C73E1D` | `#0A0A0A` | `#FFF8EC` |
| **deep-forest** | 採用 / 教育 / 健康 | `#56A06E` | `#1F4D2E` | `#0A0A0A` | `#F4F0E6` |

文字色：
- ファネル内の数字と名前はすべて白（`#FFFFFF`）
- 頂 / サブタイトル / 下部 strip は ink（`#0A0A0A`）
- 灰色の補助文字：`rgba(10,10,10,0.55)`

【フォントスタック】

```
"PingFang SC", "Heiti SC", "Helvetica Neue", "Arial", -apple-system, sans-serif
```

数字（tabular-nums 必須）：
```
"SF Mono", "JetBrains Mono", "Menlo", "Roboto Mono", monospace
```

**Inter は使わない** —— 「AI 既定」の味が強すぎる。優先は PingFang SC（CJK）+ Helvetica Neue（ラテン）。

【字サイズ / 間隔は固定】

- メインタイトル：`clamp(28px, 2.8vw, 36px)` font-weight 800 letter-spacing `-0.02em`
- サブタイトル：`14-16px` font-weight 500 ink/0.6
- 段内の大きな数字：`clamp(48px, 5.5vw, 72px)` tabular-nums font-weight 900 white
- 段内の段階名：`20-22px` font-weight 700 white
- 段内の説明：`13-15px` font-weight 400 white/0.85
- 段間のコンバージョン率バッジ：`13px` font-weight 700, paper 地に ink の字, 角丸 6px, padding 2px 8px
- 下部の累計の大きな数字：`clamp(80px, 12vw, 120px)` font-weight 900 ink letter-spacing `-0.04em`
- 下部の洞察：`16-18px` font-weight 500 ink/0.75 max-width 80%
- 全体 padding：`6vmin 7vmin`
- 段間 gap：`6px`
- Hero とファネルの間の gap：`32-48px`
- ファネルと strip の間の gap：`48-64px`

【出力の約束】

出力は**単ファイル HTML**, inline CSS, **JS は書かない**（静的図）。**CDN / アイコンライブラリ / フォントファイルは外部リンクしない**。
- アイコンは置かない / emoji 装飾は使わない（ファネル自体が図）
- チャートは置かない（円グラフ / 棒グラフ）—— 1 本につきファネル 1 つ
- 会社 logo は置かない
- background は paper, 図全体が viewport を埋める
- `aspect-ratio: 9 / 16` でコンテナを固定, 内容は flex column で埋める

【データの規則】

- 頂の数 = 100% 基準
- 各段のコンバージョン率 = `現在の段 / 一段上`
- 累計コンバージョン率 = `末段 / 頂段`
- 数字の 3 桁区切りは半角カンマ（10,000。10000 は使わない）
- パーセントは小数 1 位（18.5%。18.50% も 19% も使わない）
- 単位（人 / 件 / $）は数字の後ろ、13-15px 灰色
- 絶対数の方が割合より説得力がある（「81,500 人減った」は「81.5% 漏れた」より刺さる）

【洞察テキスト（下部 strip）】

**1-2 文**, 総長 ≤ 60 字：
- 1 文目：累計数字 + 評価（"100,000 人の訪問者のうち、残ったのは 920 人だけ"）
- 2 文目（任意）：最大ロスの段を指す（"最大の流出は『訪問者→登録』。81.5% が最初の一歩で去った"）

AI コピー口調は禁止（「本図からわかるように」「したがって」「以上より」）。事実を直接書く。

【段ごとの視覚幅の計算】

5 段のとき, top_width=100%, bottom_width=30%（ファネルの閉じ）。各段の bottom_width は一段上より `(100-30)/5 = 14%` 狭い。例：
- Stage 1: top 100% → bottom 86%
- Stage 2: top 86% → bottom 72%
- Stage 3: top 72% → bottom 58%
- Stage 4: top 58% → bottom 44%
- Stage 5: top 44% → bottom 30%

clip-path の式（各段独立の div）：
```css
clip-path: polygon(
  {(100-top)/2}% 0%,
  {100-(100-top)/2}% 0%,
  {100-(100-bottom)/2}% 100%,
  {(100-bottom)/2}% 100%
);
```

3-4 段のときは閉じを `40-45%` まで緩めてよい。6 段のときは `22-25%` まで落とす。

【やってはいけないこと】
- ファネル段の中にアイコン / イラストを描かない
- 数字を段の右、名前を左に置かない（左数字 / 右名前。視覚の重心を作る）
- 段の高さを数値に連動させない（これは funnel であり H-bar chart ではない。情報密度は幅の収縮で伝える）
- ファネルを中央に浮かせない——中段を埋め、上は Hero に、下は strip に付ける
- 6 段を超えない（情報過多。2 枚に分ける）
- 3D / 影 / 発光は使わない（platine のきれいな組版）
- Inter フォントは使わない（上記）
- 「以下はファネル」「下図の通り」のような meta 文は書かない

【クレジット】
本 skill のデザインは [baoyu-skills · baoyu-infographic](https://github.com/JimLiu/baoyu-skills) の funnel layout 規範を参照。視覚の補完 + HTML 実装は html-anything が独立して書いた。
