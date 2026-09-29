---
name: social-spotify-card
zh_name: "Spotify 再生中カード"
en_name: "Spotify Now-Playing Card"
emoji: "🎵"
description: "Spotify Now Playing 風カード: アルバムジャケット + 進捗バー + 再生コントロール。動画オーバーレイ / プロフィール向け"
category: card
scenario: personal
aspect_hint: "1280×720 または 600×200"
featured: 43
tags: ["spotify", "music", "now-playing", "card", "overlay"]
example_id: sample-social-spotify-card
example_name: "Spotify Now Playing · Lo-Fi"
example_format: markdown
example_tagline: "Spotify クラシック dark カード"
example_desc: "Lo-Fi Beats · Chillhop 進捗バー 1:24 / 3:42 + コントロール行"
example_source_url: "https://hyperframes.heygen.com/catalog"
example_source_label: "hyperframes · spotify-card"
---

【テンプレート: Spotify Now-Playing カード】
【意図】曲、ポッドキャスト、または自己紹介を Spotify 再生中カードにする。video overlay / 個人 about page / クリエイター hero 向け。Inspired by hyperframes spotify-card。

【キャンバス】2 サイズ:
- 横の動画オーバーレイ: 1280×720, カードは中央または左下に浮かべる。
- コンパクト横バー widget: 600×200, どの hero にも埋め込める。

【カード構造】
- 外枠: 角丸 12-16px; bg はジャケット色から取った暗いグラデーション (e.g. `linear-gradient(135deg, #1e3264 0%, #0d1f3d 100%)`) または Spotify クラシック `#121212`; 縁に 1px subtle border。
- 左側: **アルバムジャケット** (CSS グラデーション + 大きな monogram または抽象ジオメトリ。外部画像 URL は使わない), 角丸 6px, 60-200px 正方形。
- 右側:
  - 上部 `NOW PLAYING` (uppercase letterspace 0.14em, 11px, 緑 `#1DB954`)。
  - **曲名 / タイトル** (Inter / Spotify Circular, 22-28px, weight 700, 白)。
  - **アーティスト / サブタイトル** (16px, weight 400, opacity 0.7)。
  - 進捗バー: 高さ 4px, 角丸, 灰背景 + 白 fill (`width: 38%`); 両端のタイムスタンプ `1:24 / 3:42` (mono, 11px, 灰)。
  - コントロール行: ⏮ ⏯ ⏭ icon (inline SVG, 24px, 白 fill), shuffle / repeat icon は小さめ。
- 右上: Spotify logo (インライン SVG, 緑 `#1DB954` 円 + 白い波形 3 本)。
- 任意: 右下に小さな波形モーション (bar 3 本 `@keyframes`)。

【フォント】
- 主: `Spotify Circular` → fallback `Inter` / `Inter Tight`, weight 400 / 700。
- 数字: 同じ主フォント。mono は多用しない。

【デザインの要点】
- Spotify クラシック dark mode: `#121212` bg, `#1DB954` accent, `#b3b3b3` secondary text。
- ユーザー入力がテキスト/タイトルなら → "タイトル" を曲名、"サブタイトル/著者" をアーティスト、"尺" はデフォルト 3:42。
- ユーザー入力が音楽関連なら → そのまま対応。
- 外部画像 URL は禁止; ジャケットは CSS グラデーション + 文字 logo / ジオメトリ。
- 小さなモーション: 波形は `@keyframes`。`prefers-reduced-motion` でオフにできる。
- 単ファイル HTML。
