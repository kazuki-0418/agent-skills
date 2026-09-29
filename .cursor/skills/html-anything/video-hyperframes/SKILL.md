---
name: video-hyperframes
zh_name: "Hyperframes 動画スクリプト"
en_name: "Hyperframes Video"
emoji: "🎞️"
description: "Hyperframes / Remotion 互換の連続フレームアニメーション。自動再生できる"
category: video
scenario: video
aspect_hint: "1920×1080 (16:9)"
recommended: 5
tags: ["video", "hyperframes", "remotion", "動画"]
example_id: sample-hyperframes-workflow
example_name: "Hyperframes · AI workflow 動画"
example_format: markdown
example_tagline: "8 フレーム自動再生。進捗バー + メタデータ"
example_desc: "映画的なアニメーションスクリプト。そのまま Remotion に渡して mp4 にできる"
example_source_url: "https://github.com/heygen-com/hyperframes"
example_source_label: "heygen-com/hyperframes"
---

【テンプレート: Hyperframes 動画フレーム】
- 連続する `<section class="frame">` を N 個出す。各 `w-[1920px] h-[1080px]`; N は【ユーザーの素材】の情報密度で決める (短いスクリプトは 6-10 フレームから。長いスクリプトは枚数を増やす。1 フレームはショット/概念 1 つだけ)。
- 各フレームはショット/概念 1 つ: テキスト + 視覚構図 (中央構図 / 黄金分割 / 三分割)。
- 各フレーム下部に隠しマーク `<!-- frame:N duration:3000 transition:fade -->`。後続の Remotion / Hyperframes レンダスクリプトが読む。
- 上部に JavaScript 自動再生: 3 秒ごとに次フレーム。クリック / 矢印キーも可; 隅に進捗バー。
- 1 フレーム目は hook (データ 1 / 反常識 1 / 問い 1), 2-N は論証, 最後は結論 + CTA。
- サイズは巨大 (text-9xl)。1 文で足りる。詰め込まない。
- 配色は映画的な 1 セット (暗い背景 + neon 強調色 1)。
- 出力の最後に短いコメント `<!-- HYPERFRAMES_META: ... -->`。各フレームの duration / transition / sceneSummary の JSON メタデータ。後で Remotion に渡す用。
