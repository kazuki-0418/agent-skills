---
name: article-sketchnote-editorial
zh_name: "編集式ビジュアルノート"
en_name: "Editorial Sketchnote"
emoji: "📒"
description: "ひとつの概念を雑誌の特集アーカイブにする——本当の問題→失敗→転換→洞察→命名。layout 型 6 + 書体コントラスト 4 + 捜査ファイルのディテール"
category: article
scenario: education
aspect_hint: "1080 × 適応（縦の長図）"
tags: ["sketchnote", "magazine", "editorial", "アーカイブ", "雑誌", "ビジュアルノート", "narrative", "ナラティブ", "concept-history", "概念史"]
example_id: sample-sketchnote-emergence
example_name: "ビジュアルノート · 創発の命名"
example_format: markdown
example_tagline: "還元論の失敗 → Anderson 1972"
example_desc: "「創発」を終点とする概念史の特集, 6 つの layout リズム = 開放→密→密→爆発→開放→静"
example_source_url: "https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-card"
example_source_label: "lijigang/ljg-skills · ljg-card"
---

【テンプレート: 編集式ビジュアルノート（Editorial Sketchnote）】

【魂】ひとつの**概念**を編集式の図文アーカイブに鋳造する。読者はそれを学術誌の特集をめくるようにめくる——本当の問題（特集の刊頭）→ 失敗した試み（付箋の注釈、アーカイブのラベル）→ 「待てよ——」の転換（段をまたぐ大タイトル）→ そのものを見る（Hero 見開き）→ 名前（Closing の名札）。

**博物館の陳列ではない。雑誌の欄である。教科書の定義ではない。捜査ファイルである。** 視覚とナラティブがともに担い、読者自身が「行き詰まる—通らない—めくり越える—見えた」の弧を経験する。文章は抑制し、結論を先に言わない。

【公理 6 条 — ひとつでも通らなければ、やり直し】

1. **本当の問題を先に置く** — 起点は具体的で、触れられる、行き詰まった問題。「X とは何か」ではない。「当時の人々は A、B、C では足りなかった」。問題には裂け目が必要。
2. **失敗が必須** — 経路の中に少なくとも一度の失敗（または逸脱、半正解）。線形の「これより得られる」は緊張を殺す。
3. **洞察が先、命名が後** — 読者は先に「見る」, それから「これは……と呼ばれる」と告げられる。**タイトルに概念名を出さない**。
4. **「いま」の視点** — 各駅は「彼/彼女がその瞬間に見えていたもの」, 「100 年後から振り返る私たち」ではない。後世の評価は画面に入れない。
5. **文章は抑制し、結論を先に言わない** — 「いま学んだのはひとつの概念だと思っているだろう」「それを再び産み直した」のようなメタ自己言及は禁止。ナラティブの緊張が発明感を自ら生むようにする。詩的な余韻は可（「こうして、山が見えた」）。
6. **日本語として自然に** — 翻訳調は使わない。動詞駆動 / 具体物 / 口語のリズム。禁忌: 「X される」「X を行う」「…の背景のもとで」「X の発展に伴い」「当該手法は複数の次元で優位を示す」。

【layout 型 6 — リズムを固定】

各駅は**異なる** layout を使う。そうしてリズムが現れる：

| 順 | 駅 | class | 視覚の特徴 |
|---|---|---|---|
| 01 | 起点 / Feature | `.feature` | ベージュ地 + grid 6fr/6fr, 左に大きな SVG 図 / 右に文字; kicker + Serif 大タイトル + italic lead + drop-cap body |
| 02 | 失敗一 / Note | `.note` | 2カラム grid（左 sidekick 落書きエリア + 右 540px 付箋紙）; 付箋を 0.5deg わずかに回転 + 上部の破線パンチ穴 + 赤ペン取り消し線 + scribble + footnote ¹ |
| 03 | 失敗二 / Archive | `.archive` | 全幅 + 黒い印章 stamp（168px, ✕ の大文字を含む）+ 右欄 body + SVG グリッド図 + verdict 赤の italic |
| 04 | 転換 / Cross | `.cross` | 全幅 + Serif 200px **内容が決める転換の爆点**（「待てよ」の使い回し禁止）+ amber ハイライト + 2欄 |
| 05 | 洞察 / Hero | `.hero` | 青の上辺 4px + grid 7fr/5fr; 左に大きな SVG / 右 pull-quote + drop-cap body |
| 06 | 命名 / Closing | `.closing` | ベージュ地 + 二重線の上辺 + 中心対称 + 巨大な Serif 名 + byline 上下の細線 + epilogue |

**リズムの絶対ルール**: 開放（feature）→ 密（note のずれ）→ 密（archive 横長）→ 爆発（cross 200px）→ 開放（hero）→ 静（closing 中心対称）。均等に展開しない。呼吸がある——開放と密が交替し、転換で大爆発、最後に中心対称へ戻る。

**やってはいけないこと**：6 つの節がすべて 60-80px margin-top の均等間隔 = ギャラリー陳列であり、漫画の分鏡ではない。並べ直す。

【書体コントラスト — 4 種を同時に使う】

- **Serif** (`Noto Serif SC`)：雑誌の主タイトル、mega-name、italic lead、pull-quote
- **Sans** (`Noto Sans SC`)：本文 body-sans、failed station head、kicker の後の文字
- **Mono** (`JetBrains Mono` / `SF Mono`)：番号 num、kicker label、byline、footnote ¹、stamp
- **Hand** (`Caveat` / 楷体)：手書き注釈 scribble、ask の問い、caption

**ひとつでも欠ける = 視覚が AI 単一書体の均質感に戻り、魂が崩れる**。

【色のシステム — 主色 ≤4】

```
--bg:          #FAF7EF   /* 暖かい米白地 */
--paper:       #F5F1E5   /* ベージュカード（feature/closing 地）*/
--ink-strong:  #0F0F0F   /* 重要な文字, #000 を避ける */
--ink:         #1F1F1F   /* body */
--ink-light:   #6B6B6B   /* kicker, caption */
--red:         #B23A2C   /* 誤り、注釈、強調 */
--blue-deep:   #3D5A80   /* 洞察の視覚 */
--amber:       #BB8A2B   /* 転換のヒント */
--amber-soft:  #D7A85A   /* ハイライト地色 */
```

**`#000` の純黒は禁止**。主色 ≤ 4（赤 + 青 + amber + 中性）。

【必須の装飾構造パーツ】

`kicker / drop-cap / byline / stamp` は構造の必須項。他は必要に応じて使う：

- **kicker** — 駅の番号 + 種別の小文字：Mono uppercase 13px + 黒地白字 num の四角 + 36px 短い横線
- **drop-cap** — body の頭文字：`::first-letter` float left, 96px Serif
- **lead** — feature の導入：italic 23px Serif + 赤の左ボーダー 2px
- **pull-quote** — hero の核心文：italic 38px Serif + 青のボーダー 4px + 浮動 `\201C` 大引用符 100px
- **strike** — failed body でキーワードを取り消し：`text-decoration: line-through` 赤 2.5px
- **scribble** — note の赤ペン注釈：Caveat 24px + 6deg 回転 + 赤 + 破線の赤枠
- **stamp** — archive の失敗印章：黒地白字 12px Mono + ✕ Serif 64px
- **verdict** — archive の結審文：italic 19px Serif 赤 + 上の破線区切り
- **footnote** — note の脚注：Mono 13px + ¹ 上付き
- **byline** — closing の出典：Mono 14px uppercase + letter-spacing 0.18em + 上下の細い黒線
- **mega** — cross の転換爆点：Serif 200px + amber グラデーションハイライト（核心の字 1-3 個）
- **epilogue** — closing の余韻：italic 26px Serif + `—` 赤のダッシュ接頭

【sidekick 落書きエリア — note 型の左欄は空にしない】

3 つの埋め方（内容に合わせて選ぶ, 詰め込まない）：
- **SVG スケッチ** — 失敗の本質を 1-2 個の図形の姿勢で描ける → `<svg viewBox="0 0 280 220">` 簡略画 + 赤ペン注釈
- **手書き公式** (`.formula`) — 失敗の本質を 1-3 行の文字関係に圧縮できる → Caveat 22px + 破線の左ボーダー + わずかに回転 -1deg
- **矢印のコメント** (`.arrow`) — 一点の強調 → Caveat 26px + わずかに回転 6deg + 赤

**制約**：sidekick は脚注であり主役を奪わない / 落書き感を精緻より優先（傾き、破線、隙間を残す）/ 色は抑制（黒灰 + 赤）/ 内容密度は低く（3 つの図を詰め込むより少なく）。

【HTML 骨格（agent が再利用する構造, 内容はナラティブの弧が決める）】

```html
<div class="magazine-head">
  <div class="top-bar">
    <div class="left"><span class="badge">№ 01</span><span>[領域 · 年]</span></div>
    <div class="right">[ENGLISH CATEGORY]</div>
  </div>
  <h1>[ネタバレしないタイトル]<br>[2 行目は任意]</h1>
  <p class="deck">[italic 導入: 問題をほのめかし答えは明かさない]</p>
</div>

<section class="feature">
  <div class="visual"><svg>[大きな SVG 図, max-width 540]</svg></div>
  <div class="meta">
    <div class="kicker"><span class="num">01</span><span class="rule"></span>起点 · [時空のアンカー]</div>
    <h2 class="head-serif">[行き詰まった問題]</h2>
    <p class="lead">[簡潔なリード 1 文]</p>
    <div class="body-sans drop-cap"><p>[具体例]</p><p>[転換の要点は <em></em> で強調]</p><span class="ask">[開かれた問い？]</span></div>
  </div>
</section>

<aside class="note">
  <div class="sidekick">
    <!-- 3 択: SVG / .formula / .arrow + 任意の .doodle-caption -->
  </div>
  <div class="paper">
    <div class="kicker"><span class="num">02</span>最初の試み</div>
    <h3 class="head-sans">[動作名]</h3>
    <div class="body-serif"><p>[着想]</p><p>失敗は <span class="strike">取り消し線</span></p></div>
    <div class="footnote"><span class="mark">¹</span><span>[根本原因]</span></div>
    <div class="scribble">[赤ペン注釈 1 文]</div>
  </div>
</aside>

<section class="archive">
  <div class="stamp"><div class="label">EX-02</div><div class="x">✕</div><div class="case">Failed</div></div>
  <div class="body-area">
    <div class="kicker"><span>2 回目の試み</span></div>
    <h3 class="head-sans">[動作名]</h3>
    <div class="visual"><svg>[失敗の図示]</svg></div>
    <div class="body-serif"><p>[着想 + 失敗]</p></div>
    <div class="verdict">[結審文]</div>
  </div>
</section>

<section class="cross">
  <h2 class="mega"><span class="em">[転換の爆点 1-3 字]</span>[任意の接尾]</h2>
  <div class="grid">
    <div class="left">
      <div class="kicker"><span class="num">04</span>転換</div>
      <div class="body-serif"><p>[逆向きの陳述]</p></div>
      <span class="ask">[転換の問い？]</span>
    </div>
    <div class="right"><svg>[逆向きの姿勢]</svg><p class="caption">[caption]</p></div>
  </div>
</section>

<section class="hero">
  <div class="layout">
    <div class="visual"><svg>[大きな hero 図]</svg><p class="caption">[caption]</p></div>
    <div class="text">
      <div class="kicker"><span class="num">05</span>洞察</div>
      <h2 class="head-serif">[姿勢の名, 概念名は出さない]</h2>
      <div class="pull-quote">[核心の文]</div>
      <div class="body-serif drop-cap"><p>[洞察の具体的な言い表し]</p></div>
    </div>
  </div>
</section>

<section class="closing">
  <p class="approach">[この種の X の研究対象は、——と呼ばれる]</p>
  <h1 class="mega-name">[日本語の概念名]</h1>
  <div class="en-name">[English Name]</div>
  <div class="byline"><span><strong>[人名]</strong></span><span class="sep">·</span><span>[年]</span><span class="sep">·</span><span>[文献]</span></div>
  <div class="closing-body"><p>[それが開いたもの]</p><p>[それが取り替えた眼]</p></div>
  <p class="epilogue">[詩的な余韻, メタ自己言及しない]</p>
</section>
```

**字サイズとリズム padding の対照**：

| section | padding 上 / 下 | margin-top | 余白の尺度 |
|---|---|---|---|
| feature | 38 / 44 | — | 中 |
| note | 22 / 22 | 24 | 小 |
| archive | 22 / 24 | 24 | 小 |
| cross | 64 / 60 | 30 | 大 |
| hero | 52 / 48 | 32 | 中やや小 |
| closing | 60 / 64 | 32 | 大 |

完全な CSS は同ディレクトリの `example.html` を参照（各 class は実装済み）。

【出力の約束】

**単ファイル HTML** を出す, inline CSS + Google Fonts CDN（Noto Serif SC / Noto Sans SC / Caveat / JetBrains Mono）。JS は書かない, 静的な縦長図。容器幅 1080px, 高さは適応。

【セルフチェック 6 項 — ひとつでも通らなければ、やり直し】

1. **問題の駅**: タイトルに概念名が出ていない / 問題が具体的で触れられる / 「彼/彼女その瞬間」の視点
2. **失敗の駅**: 少なくとも 1 回の失敗 / 失敗に手がかりがある（取り消し線 / verdict / footnote）
3. **洞察が先、命名が後**: 命名は closing のみ / hero タイトルはネタバレしない
4. **文章の抑制**: 「いま……と思っているだろう」自己言及の構文がない
5. **日本語として自然に**: 「X される」「X を行う」「X の発展に伴い」などの翻訳調がない
6. **リズムが不均一**: 6 節の margin-top がすべて等しくない / 余白は cross と closing に集中

【やってはいけないこと】
- タイトルに概念名を出さない（ネタバレ）
- アイコン / emoji を装飾に使わない
- #000 の純黒は使わない
- すべてのタイトルを中央揃えにしない（feature/note/archive は左揃え / cross/closing だけ中央揃え）
- 6 節の padding を揃えない
- Inter フォントは使わない
- 結論を先に言うメタ自己言及はしない
- sidekick を空にしない

【クレジット】
本 skill は [lijigang/ljg-skills · ljg-card -v sketchnote](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-card)（v2.3.0）から改作。原版は PNG を出す（playwright スクリーンショット）, html-anything 版は単ファイル HTML を直接出す。公理 6 + layout 6 + 書体 4 + リズムは原版と一致。
