---
name: vfx-text-cursor
zh_name: "VFX テキストカーソル"
en_name: "VFX Text Cursor"
emoji: "✨"
description: "カーソルの引き光 + 色収差の光線 + 指向性フレア。動画オープニングで一字ずつ名言を出す用"
category: video
scenario: video
aspect_hint: "1920×1080 (16:9)"
featured: 38
recommended: 7
tags: ["vfx", "text", "cursor", "chromatic", "reveal", "frame"]
example_id: sample-vfx-text-cursor
example_name: "VFX カーソル · オープニング名言"
example_format: markdown
example_tagline: "一字ずつ開示 + chromatic 引き光"
example_desc: "カーソル打ち hot pink + cyan 色収差。動画オープニング用"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · vfx-text-cursor"
---

【テンプレート: VFX テキストカーソル (Text Cursor)】
【意図】動画オープニング/Hero フレーム —— カーソルがキャンバス上で「タイプ」し、文字が一字ずつ現れ、後ろに色収差の尾 + 指向性フレアを引く。Inspired by hyperframes vfx-text-cursor。

【キャンバス】1920×1080, 背景 `#06070a` マットな黒 または `#0a0d12` (暖色寄りの青); 控えめな vignette。

【内容】
- 名言 1 文 (日英どちらでも), 中央揃え, サイズ 6-8vw, weight 700, フォント `Inter Tight` / `Source Sans 3` / `Noto Sans SC`。
- 一字ずつ開示, 各文字 80ms 間隔; 現在の文字の後ろに cursor `▍` (または細い vertical bar)。
- 出た文字はデフォルト白 `#f5f5f7`, opacity 1; これから出る位置に chromatic ghost: `text-shadow: 2px 0 #ff3b6f, -2px 0 #00d4ff` を reveal の瞬間に足し, 200ms で通常に戻る。
- カーソル本体: 幅 16px の矩形, 色 = accent (1 つ取る: hot pink `#ff3b6f` / cyan `#00d4ff` / amber `#ffb547`), 点滅 `@keyframes` 1.0s 周期; 後ろに 60-120px の motion blur trail (放射グラデーションで透明へ)。

【フレア / 光線】
- タイプ位置の近くに **指向性フレア** (light leak) を 3-5 本ランダムに: `linear-gradient(45deg, transparent, accent20, transparent)` の細長い矩形 + `mix-blend-mode: screen`, 不規則な角度。
- 打ち終わったら、全文に 0.5s shimmer sweep (光の帯が横切る)。

【フィールド】
- 上部 caption (uppercase letterspace 0.18em, 11px, opacity 0.5): "FRAME 01 · OPENING"。
- 文字の下のサブタイトル (24-28px, opacity 0.6): 出典 / 章。
- 右下 timecode (`00:03:21` mono)。

【デザインの要点】
- **禁止**: 多色虹の chromatic (hot pink + cyan のような二色の色収差 1 組だけ。R/G/B 全色は使わない)。
- フォント: 欧文 `Inter Tight` Bold; 日本語 `Noto Sans SC` Bold; セリフは禁止。
- モーションは `@keyframes` + JS タイマー (`setTimeout` で一字ずつ)。`prefers-reduced-motion` でオフにできる (全文字をすぐ出す)。
- ユーザーが渡した名言を使う; 捏造しない。
- 単ファイル HTML。フォント以外の外部リソースは使わない。
