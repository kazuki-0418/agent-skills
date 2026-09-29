---
name: deck-ljg-present
zh_name: "宣言型スピーチ（Outline-Faithful）"
en_name: "Outline-Faithful Manifesto Deck"
emoji: "✊"
description: "outline を 1:1 で色面・大文字の宣言 deck にする。原文は動かさず見た目だけ。テーマ 3 種 black / red / yellow"
category: slides
scenario: creator
aspect_hint: "16:9 横スライド"
tags: ["deck", "manifesto", "slogan", "outline", "宣言", "スピーチ", "色面", "大文字", "ultra-bold"]
example_id: sample-ljg-present-ai
example_name: "宣言型スピーチ · AI 革命"
example_format: markdown
example_tagline: "Red 宣言 · ずらし大文字 · 左揃え"
example_desc: "8 ページ outline-faithful スピーチ。一級タイトルのカバー + リストのずらし + 区切りの休止ページ + 締めの反問。原文は最後まで書き換えない"
example_source_url: "https://github.com/lijigang/ljg-skills/tree/md/skills/ljg-present"
example_source_label: "lijigang/ljg-skills · ljg-present"
---

【テンプレート: 宣言型スピーチ（Outline-Faithful）】

【意図】ユーザーの outline / markdown を 1:1 で色面・大文字の manifesto deck にする。**抽出しない、書き換えない、並べ替えない、圧縮しない**——決めるのは各行/各節をどのページに描くかだけ。見た目の参照：Felipe Franco / BIG STUDIOS の manifesto 大文字ポスター。

【絶対ルール — 1 つでも破ったら作り直す】
- タイトルの字は変えない。段落の字は変えない。リストの字は変えない。順序は並べ替えない
- 許される「動かし」は**物理的な改ページ**だけ（段落が長すぎるとき複数ページに割る）
- manifesto を抽出しない / 新しい文を書かない / 内容を消さない / 画像やアイコンを置かない / トランジションアニメは使わない
- 1 本につきテーマ色は 1 つ（black / red / yellow から 1）

【outline → ページ対応】

| 入力要素 | 出力ページ |
|---|---|
| `# 一級見出し` | 独占 **emphasis** カバーページ（accent 地色。多くは 1 字/短い語） |
| `## 二級見出し` | 独占 **theme** ページ（大文字タイトルが 1 ページを独占） |
| `### 三級見出し`+ | 独占 theme ページ（字サイズは自動で 1 段下げる） |
| 段落（≤30字） | theme ページ 1 枚 |
| 段落（30-80字, 句点が多い） | 1 文 1 ページ（medium 段） |
| 段落（>80字） | 約 30 字で 1 ページに割り、末尾に `⋯` |
| `- リスト項目`（≤4） | 1 ページにすべて出す。indent は入れ子の深さ 0/1/2 |
| リスト 5-8 項 | 2 ページに割る。各ページ 3-4 項。項数は近づける |
| リスト >8 項 | 複数ページに割る。各ページ 4 項 |
| 表 ≤6 行 | 1 ページ |
| 表 >6 行 | 複数ページに割る。各ページで表頭を残す |
| `**強調**` / `` `code` `` | 自動 `hl: true` |
| `---` 区切り | 独立 **emphasis 休止ページ**（空の emphasis。純色面） |

**先頭と末尾は自動 emphasis**：文書の先頭段（すでに `#` なら結合）+ 文書の末段 = emphasis の開き / 締めページ。一級見出しは天然の章の区切り。リズム合わせのために emphasis を足さない。

【テーマ色の推定 — 1 本につき 1 つだけ】

| 文書の調子 / タグ | theme | 既定ページ | emphasis ページ | hl 色（theme ページでのみ効く） |
|---|---|---|---|---|
| 思索 / 論証 / ノート（既定） | **black** | 黒地白字 | 赤地白字 | 赤 `#E63956` |
| 宣言 / 呼びかけ / スピーチ（`share` / `manifesto` / `keynote` / `talk` タグまたは口調を含む） | **red** | 赤地白字 | 黒地白字 | 柔金黄 `#FFE082` |
| 皮肉 / 警戒 / 批判（`critique` / `warn` / `rant` を含む） | **yellow** | 黄地黒字 | 黒地白字 | 赤 `#E63956` |

明示の上書き：ユーザーが「red を使う / yellow を使う / 黒地を使う」と書けば指示どおり。手がかりがなければ既定は black。

【見た目の規定 — 数値は固定】

パレット（4 色のみ。hex は変えない）：
```
--c-black:  #1A1A1A
--c-red:    #E63956
--c-yellow: #FFD400
--c-white:  #FFFFFF
--c-gold:   #FFE082
```

フォントスタック（ultra-bold 900 必須, letter-spacing `-0.05em`）：
```
"Helvetica Neue", "Arial Black", "Inter", "PingFang SC", "Heiti SC", "STHeiti", -apple-system, sans-serif
font-weight: 900
```

字サイズの段（そのページの**いちばん長い行**の文字数。CJK は 1.8 で重み付け。複数行ページは 1 段下げる）：

| 段 | 文字数 | font-size |
|---|---|---|
| single | ≤2 | `clamp(320px, 80vmin, 1100px)` |
| short | 3-6 | `clamp(240px, 55vmin, 780px)` |
| medium | 7-14 | `clamp(150px, 35vmin, 480px)` |
| long | 15-26 | `clamp(100px, 22vmin, 320px)` |
| xlong | 27+ | `clamp(64px, 14vmin, 200px)` |

組版：
- padding `6vmin 7vmin`。大文字を端まで張る
- `.lines` ブロックは画面内で水平中央。ブロック内の各行は **left-aligned**（右の空きを消しつつ indent のずらしは残す）
- line-height `1.05`, 行間 gap `0.15em`
- 内容は垂直中央
- フッター：左下ページ番号（`01 / 08`）+ 右下サブタイトル, 13px monospace, opacity 0.5, uppercase, letter-spacing `0.12em`
- emphasis ページ：背景は `--acc-bg`、字色は `--acc-fg`。行内 `.hl` は自動で `color: inherit`（emphasis のページ全体がハイライト）
- indent の段：0 = `0`, 1 = `7vmin`, 2 = `16vmin`

【出力の約束】

出力は**単ファイル HTML**。完全に自己完結。inline CSS + inline JS。iframe sandbox の中でそのまま動く。骨格はこのテンプレートどおり。`SLIDES` 配列、`<title>`、`{{SUBTITLE}}`、`body[data-theme]` を埋めればよい。**CDN の外リンクは使わない。外部リソースは使わない**。

SLIDES 配列の各要素の形：
```js
// 既定の theme ページ
{ lines: [ { indent: 0, chunks: [ {t: "前段"}, {t: "ハイライト語", hl: true}, {t: "後段"} ] } ] }
// emphasis ページ（accent 地色。inline hl は自動で無視）
{ emphasis: true, lines: [ { indent: 0, chunks: [ {t: "AI"} ] } ] }
// 休止ページ = emphasis + 空の lines
{ emphasis: true, lines: [] }
```

完全な HTML 骨格（agent は **CSS と JS を再利用し、変えない**。埋めるのは SLIDES / title / subtitle / data-theme だけ）：

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title><!-- 文書タイトル --></title>
<style>
  :root {
    --c-black: #1A1A1A; --c-red: #E63956; --c-yellow: #FFD400;
    --c-white: #FFFFFF; --c-gold: #FFE082;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    width: 100%; height: 100%;
    font-family: "Helvetica Neue", "Arial Black", "Inter", "PingFang SC", "Heiti SC", "STHeiti", -apple-system, sans-serif;
    font-weight: 900; overflow: hidden;
    -webkit-font-smoothing: antialiased;
    letter-spacing: -0.05em;
  }
  body[data-theme="black"]  { --bg: var(--c-black);  --fg: var(--c-white); --acc-bg: var(--c-red);   --acc-fg: var(--c-white); --hl: var(--c-red); }
  body[data-theme="red"]    { --bg: var(--c-red);    --fg: var(--c-white); --acc-bg: var(--c-black); --acc-fg: var(--c-white); --hl: var(--c-gold); }
  body[data-theme="yellow"] { --bg: var(--c-yellow); --fg: var(--c-black); --acc-bg: var(--c-black); --acc-fg: var(--c-white); --hl: var(--c-red); }
  body { background: var(--bg); }
  .stage { position: fixed; inset: 0; }
  .slide {
    position: absolute; inset: 0; display: none;
    flex-direction: column; justify-content: center; align-items: center;
    padding: 6vmin 7vmin;
    background: var(--bg); color: var(--fg);
  }
  .slide.active { display: flex; }
  .slide[data-emphasis="true"] { background: var(--acc-bg); color: var(--acc-fg); }
  .slide .hl { color: var(--hl); }
  .slide[data-emphasis="true"] .hl { color: inherit; }
  .lines { display: flex; flex-direction: column; gap: 0.15em; line-height: 1.05; max-width: 100%; align-items: flex-start; }
  .line { white-space: nowrap; text-align: left; }
  .line[data-indent="0"] { padding-left: 0; }
  .line[data-indent="1"] { padding-left: 7vmin; }
  .line[data-indent="2"] { padding-left: 16vmin; }
  .slide[data-len="single"] .lines { font-size: clamp(320px, 80vmin, 1100px); }
  .slide[data-len="short"]  .lines { font-size: clamp(240px, 55vmin, 780px); }
  .slide[data-len="medium"] .lines { font-size: clamp(150px, 35vmin, 480px); }
  .slide[data-len="long"]   .lines { font-size: clamp(100px, 22vmin, 320px); }
  .slide[data-len="xlong"]  .lines { font-size: clamp(64px,  14vmin, 200px); }
  .pager, .subtitle {
    position: fixed; bottom: 2.5vmin;
    font-family: "Menlo", "Monaco", monospace;
    font-size: 13px; font-weight: 400; letter-spacing: 0.12em;
    user-select: none; z-index: 10; text-transform: uppercase;
    opacity: 0.5; color: var(--fg);
  }
  .pager { left: 3vmin; }
  .subtitle { right: 3vmin; }
  body[data-current="emphasis"] .pager,
  body[data-current="emphasis"] .subtitle { color: var(--acc-fg); }
</style>
</head>
<body data-theme="red"><!-- black|red|yellow -->
<div class="stage" id="stage"></div>
<div class="pager" id="pager">01 / 01</div>
<div class="subtitle" id="subtitle"><!-- サブタイトル / ブランド。空でも可 --></div>
<script>
  const SLIDES = [ /* outline から対応させた slides 配列を入れる */ ];
  const stage = document.getElementById('stage');
  const pager = document.getElementById('pager');
  const body = document.body;
  function lineCharLen(chunks) {
    const CJK = /[　-〿㐀-䶿一-鿿豈-﫿＀-￯]/;
    return chunks.reduce((acc, c) => {
      let len = 0;
      for (const ch of (c.t || '')) len += CJK.test(ch) ? 1.8 : 1;
      return acc + len;
    }, 0);
  }
  function maxLineLen(lines) { return lines && lines.length ? Math.max(...lines.map(l => lineCharLen(l.chunks || []))) : 0; }
  function lengthTier(maxLen, lineCount) {
    const adj = maxLen + Math.max(0, lineCount - 1) * 4;
    if (adj <= 2)  return 'single';
    if (adj <= 6)  return 'short';
    if (adj <= 14) return 'medium';
    if (adj <= 26) return 'long';
    return 'xlong';
  }
  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  SLIDES.forEach((s) => {
    const el = document.createElement('div');
    el.className = 'slide';
    if (s.emphasis) el.setAttribute('data-emphasis', 'true');
    if (s.lines && s.lines.length) {
      el.setAttribute('data-len', lengthTier(maxLineLen(s.lines), s.lines.length));
      const linesEl = document.createElement('div');
      linesEl.className = 'lines';
      s.lines.forEach(line => {
        const lineEl = document.createElement('div');
        lineEl.className = 'line';
        lineEl.setAttribute('data-indent', String(line.indent || 0));
        lineEl.innerHTML = (line.chunks || []).map(c => {
          const t = escapeHtml(c.t);
          return c.hl ? '<span class="hl">' + t + '</span>' : t;
        }).join('');
        linesEl.appendChild(lineEl);
      });
      el.appendChild(linesEl);
    }
    stage.appendChild(el);
  });
  const slides = stage.querySelectorAll('.slide');
  let idx = 0;
  function show(i) {
    if (i < 0) i = 0; if (i >= slides.length) i = slides.length - 1;
    slides[idx].classList.remove('active');
    idx = i;
    slides[idx].classList.add('active');
    pager.textContent = String(idx + 1).padStart(2, '0') + ' / ' + String(slides.length).padStart(2, '0');
    body.setAttribute('data-current', slides[idx].getAttribute('data-emphasis') === 'true' ? 'emphasis' : 'theme');
  }
  function next() { show(idx + 1); }
  function prev() { show(idx - 1); }
  document.addEventListener('keydown', (e) => {
    switch (e.key) {
      case 'ArrowRight': case ' ': case 'Enter': case 'j': case 'PageDown': e.preventDefault(); next(); break;
      case 'ArrowLeft': case 'k': case 'PageUp': e.preventDefault(); prev(); break;
      case 'Home': e.preventDefault(); show(0); break;
      case 'End': e.preventDefault(); show(slides.length - 1); break;
      case 'f': case 'F': e.preventDefault(); document.fullscreenElement ? document.exitFullscreen?.() : document.documentElement.requestFullscreen?.(); break;
    }
  });
  let touchX = null;
  document.addEventListener('touchstart', (e) => { touchX = e.touches[0].clientX; });
  document.addEventListener('touchend', (e) => {
    if (touchX == null) return;
    const dx = e.changedTouches[0].clientX - touchX;
    if (dx < -40) next(); else if (dx > 40) prev();
    touchX = null;
  });
  document.addEventListener('click', (e) => {
    if (e.target.closest('.pager,.subtitle')) return;
    const mid = window.innerWidth / 2;
    if (e.clientX > mid) next(); else prev();
  });
  show(0);
</script>
</body>
</html>
```

【手順 — agent 内部】
1. ユーザーの素材を読む（markdown / outline / プレーンテキスト）
2. 上の表で **outline → slides 配列** を対応させる。抽出せず書き換えない
3. theme を推定する（タグ > 口調 > 既定 black）
4. 骨格を再利用し、`<title>` / `data-theme` / `<div id="subtitle">` の中身 / `SLIDES` 配列を差し替える
5. HTML 文書全体を一度に出す

【品位の基準】
- outline が真理。skill はレンダラ
- 一級見出し = emphasis カバー（天然の章の区切り）
- 二級見出し = 独占 theme ページ（タイトルに見合う重みを与える）
- リストのずらしは indent 0/1/2 で入れ子の深さを出す
- `**強調**` は自動 hl
- 改ページしても見た目は揃える（同じ塊の字サイズ/インデントを揃える）
- 左揃えであり中央ではない——これが manifesto 美学の核

【やってはいけないこと】
- manifesto を抽出しない（「釘を探すな」。著者はすでに outline を書いている）
- 新しい文を書かない。順序を組み直さない。内容を消さない
- 画像を置かない / アイコンを置かない / トランジションアニメを足さない
- emphasis ページで inline hl を使わない（emphasis のページ全体がハイライト）
- theme を複数混ぜない（1 本につき 1 つの気配）
- 勝手に emphasis を足さない（一級見出し / 先頭と末尾 / 区切りだけ）

【クレジット】
この skill は [lijigang/ljg-skills · ljg-present](https://github.com/lijigang/ljg-skills/tree/md/skills/ljg-present)（v3.0.0）からの改編。原版は複数テーマを出し、cyber-hacker モードと PNG 投影を含む; html-anything 版はテーマ 3 + 単ファイル HTML 出力だけ残す。見た目の着想は引き続き Felipe Franco / BIG STUDIOS の manifesto 書体ポスター。
