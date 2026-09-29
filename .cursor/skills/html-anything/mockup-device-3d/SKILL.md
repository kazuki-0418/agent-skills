---
name: mockup-device-3d
zh_name: "iPhone × MacBook 立体スタンド"
en_name: "Device 3D Showcase"
emoji: "📱"
description: "iPhone + MacBook の GLTF 風静的スタンド。画面内に本物の HTML。ガラスレンズの屈折、360° ターンテーブル構図"
category: poster
scenario: product
aspect_hint: "1920×1080 (16:9)"
featured: 47
tags: ["device", "mockup", "iphone", "macbook", "html-in-canvas", "product"]
example_id: sample-mockup-device-3d
example_name: "iPhone × MacBook 立体スタンド"
example_format: markdown
example_tagline: "HTML-in-Canvas デバイスショー"
example_desc: "iPhone 画面 + MacBook 画面の両方に本物の UI。ガラスレンズの屈折"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · vfx-iphone-device"
---

【テンプレート: デバイス 3D スタンド (Device 3D Showcase / HTML-in-Canvas)】
【意図】製品発表、App デモ、デザイン案の展示。ユーザーが渡した UI を iPhone / MacBook の「画面」に本物として描き、周囲は CSS 3D transform で GLTF モデルのガラス / ハイライト / 屈折を模す。Inspired by hyperframes vfx-iphone-device。

【必須構図】
- **キャンバス**: 1920×1080, 暖灰グラデーション背景 `radial-gradient(#1a1a1f → #0a0a0f)`, 下部反射地面 (mirror gradient)。
- **iPhone 15 Pro モデル**: 左側 / 中央, `transform: rotateY(-12deg) rotateX(4deg) translateZ(40px)`; 枠はチタン銀 `#a8a8ad` (実線 4px) + 画面角丸 56px; 画面内は iframe-like div, ユーザーの HTML を本物として描く (mobile viewport 375×812)。
- **MacBook Pro 14"** (任意の 2 台目): 右側, やや小さく, `rotateY(8deg)`; 上蓋画面にデスクトップ viewport を埋め込む (1440×900 スケール); ベースのキーボード + trackpad は CSS 影の線で描く (キーキャップの細部は描かない)。
- **ガラス / レンズフレア**: 上部に 2-3 個の `radial-gradient(ellipse, rgba(255,255,255,0.4) 0%, transparent 60%)` 楕円 highlight。morphing glass lens を模す。
- **地面反射**: デバイス下に `transform: scaleY(-1)` + `mask-image: linear-gradient(to bottom, rgba(0,0,0,0.4), transparent 70%)`。

【画面コンテンツの出所】
- ユーザーがテキスト/データ → 自動で mock app 画面にする (上部 status bar + タイトル + body + 下部 tab bar または home indicator)。
- ユーザーが HTML → そのまま画面 div に埋め込む (scale transform で画面の幅高さに合わせる)。
- 画面内 UI は Tailwind。サイズは mobile 実寸 (text-sm / text-base, text-9xl は使わない)。

【任意の追加要素】
- 右下 "product slug" コーナーバッジ: 大きな logo + 1 行 tagline + サブタイトル hairline。
- 上部 1 行 caption (欧文 sans, サイズ小, 透明 0.6): 製品 codename / 日付 / バージョン。
- 8s 自動 CSS ターンテーブル: `@keyframes turntable` rotateY -12 ↔ 12, ease-in-out infinite alternate; `prefers-reduced-motion` でオフにできる。

【デザインの要点】
- **禁止**: 外部 mockup 画像 URL (unsplash / dribbble link いずれも)。デバイスはすべて CSS / SVG で描く。
- フォント: デバイス外の caption / logo は `Inter Tight` / `SF Pro` スタイル; デバイス内はユーザー内容に合わせて。
- 背景は任意で調色 4 セット: charcoal / pearl / midnight blue / mocha; 虹グラデーションは使わない。
- 単ファイル HTML; iframe の srcdoc 入れ子は使わない (壊れやすい)。`<div class="screen">` + Tailwind で描く。
- 画面の中身はユーザーの実データで埋める。lorem ipsum や "Your text here" は禁止。
