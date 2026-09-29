---
name: frame-macos-notification
zh_name: "macOS 通知バナー"
en_name: "macOS Notification Banner"
emoji: "🔔"
description: "本物に近い macOS 通知 banner + app icon + 見出し本文。video overlay / 製品発表予告向け"
category: card
scenario: video
aspect_hint: "1920×1080 動画または 480×120 バナー"
featured: 41
tags: ["macos", "notification", "banner", "overlay", "frame"]
example_id: sample-frame-macos-notification
example_name: "macOS 通知 · 新機能リリース"
example_format: markdown
example_tagline: "Big Sur フロストガラス banner"
example_desc: "App icon + タイトル + 2 行本文。動画の角に重ねる用"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · macos-notification"
---

【テンプレート: macOS 通知バナー】
【意図】告知 / メッセージ / ヒントを macOS Big Sur+ スタイルの通知バナーにする。動画の角オーバーレイ、製品リリース予告、SNS 図向け。Inspired by hyperframes macos-notification。

【キャンバス】使い方 2 種:
- 動画オーバーレイ 1920×1080, 通知は右上、周囲は透明。
- 単独 banner 480×120, 中央出力。

【バナー構造】
- 外枠: 角丸 14px (macOS Big Sur 標準), 480×120 (または本文込みで長く 480×180), 12-16px 内側余白。
- 背景: **frosted glass** 効果 — `background: rgba(245,245,247,0.78)` + `backdrop-filter: blur(40px) saturate(180%)`; 暗色版 `rgba(28,28,30,0.78)`。
- 枠線: 1px `rgba(0,0,0,0.06)` (light) / `rgba(255,255,255,0.08)` (dark); 上部に 1px 明るい highlight `rgba(255,255,255,0.5)`。
- 影: `0 10px 40px rgba(0,0,0,0.18), 0 2px 6px rgba(0,0,0,0.08)`。

【内容】
- 左側: **App icon** (44×44, 角丸 10px, CSS gradient + emoji 1 つまたは monogram の文字, **外部画像は使わない**)。
- 中央:
  - 上部 row: App 名 (SF Pro 13px, weight 600) + `now` または具体時刻 (12px, opacity 0.6) — 両端揃え。
  - タイトル (15px, weight 600, 1 行で切る)。
  - 本文 (13px, weight 400, 1-2 行で切る, line-height 1.35)。
- 右側 (任意): action button "Open" または "Reply" (capsule, 薄い灰地)。

【フォント】
- メイン: `SF Pro Text` → fallback `Inter` / `system-ui`; 中国語は `PingFang SC` / `Noto Sans SC`。

【任意の追加】
- 通知の重ね: 1 枚目が前、後ろ 2 枚は後ろ下へ縮小 (scale 0.96 + opacity 0.6 + translateY)。
- 入場モーション: 画面外右からスライドイン `transform: translateX(110%)→0`, 200ms ease-out; `prefers-reduced-motion` でオフ可。
- 右上の制御 chip "Clear" (hover で表示, opacity 既定 0)。

【デザインの要点】
- light mode は白フロスト、dark mode (動画推奨) はほぼ黒フロスト。
- icon に外部リンクの emoji 画像は使わない。unicode emoji または CSS の幾何。
- ユーザー提供の内容を使う; タイトル + 本文はユーザー入力からはっきり取る。
- 単ファイル HTML。`backdrop-filter` は Safari で `-webkit-` 接頭辞が必要。
