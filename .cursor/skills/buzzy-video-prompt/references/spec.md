# 仕様: AI 動画生成の制御プロンプト（Buzzy AI / Seedance 2.5 / Runway Gen-4.5）

出典: Google Doc「Buzzy AI動画生成における高度編集・調整制御の理論と実践プロンプティング」
`https://docs.google.com/document/d/1ubUScU9gEasOAe6S5yOsMBHoyGWNHiSQphT4EUDHQMA`
（元 Doc は Runway 公式プロンプティングガイド、Seedance 2.5 公式ガイド、Krea / Flick / Dreamina 等の
検証記事を出典としている。末尾の「元 Doc の参照元」参照）

> Doc が更新されたらこのファイルも更新する。判定基準の正本は Doc。ここはその作業用の要約。

## 目次

1. 失敗の 3 大メカニズム
2. 曖昧記述 → 制御記述の対応表
3. 6 大プロンプト構成要素（順序と理由）
4. 課題別の構造パターン
5. プラットフォーム機能
6. 元 Doc の参照元

---

## 1. 失敗の 3 大メカニズム

動画生成モデルはテキストと参照画像を処理する際、空間軸（フレーム内の画像構造）と
時間軸（フレーム間の連続性）の双方にアテンション重みを分散させる。
指示が反映されない原因は、この内部処理に起因する 3 つに集約される。

### 1-1. 補完最適化（ハルシネーション・ドリフト）

プロンプトで明示的に制約されていない領域・動作を、モデルは学習済み映像データセットの
確率分布に基づいて自動補完する。
「部屋に座る人物」とだけ書きカメラや背景の挙動を指定しないと、
背景の微小な変形・不規則なカメラの揺れ・勝手な照明変化が
「動画として自然な動き」として付加される。

→ 対策: 生成空間に対する定量的・定性的な境界条件（制約空間）を言語で構築する。
つまり「動かさない部分も明示的に書く」。

### 1-2. 否定文処理の破綻とトークン重み付けの逆転

「ズームインしない」「カメラを動かさない」「顔を歪ませない」といった否定形は、
テキストエンコーダで高確率に意図と逆の挙動を引き起こす。
「ズーム」「動かす」「歪む」という名詞・動詞のトークンに強いアテンション重みが割り当てられ、
`don't` / `no` といった否定のコンテキストが無視されるため、
**禁止しようとした動作そのものが実行される**。

→ 対策: 否定表現を完全に排し、望む状態を静的・動的文脈で直接記述する「肯定表現」に統一する。
これは Runway / Seedance 双方の公式ガイドラインが厳格に要求している。

### 1-3. Image-to-Video における記述過多と言語競合

参照画像を入力とする場合、画像内に既にある服装・髪型・背景の色調などを
テキストで詳細に再説明すると、画像トークンとテキストトークンの間で冗長性と競合が起きる。
このテキスト過剰供給はモデルの処理リソースを「視覚情報の再確認」に浪費させ、
**「表情の変化」や「ズームイン」といった運動指令への応答性を著しく低下させる**。

→ 対策: 静的記述は画像エンコーダに委ね、テキストは時間軸上の運動ダイナミクスと
カメラ軌道の記述に特化させる。これが I2V の鉄則。

---

## 2. 曖昧記述 → 制御記述の対応表

| 指示カテゴリ | 失敗を招く記述 | 推奨記述 | モデル内部での制御メカニズム |
|---|---|---|---|
| カメラワーク | カメラを動かさないで／ズームインしないで | Locked static tripod shot, maintaining a fixed medium shot with zero focal length variation | 空間軸上のフレーム座標を固定し、カメラモーションベクトルの計算を無効化して構図の変形を抑止する |
| 被写体動作の限定 | 余計な動きや勝手な変化をしないで | The character executes only the primary hand movement; the torso and environment remain motionless | 動体検出領域を被写体の特定パーツに限定し、背景フレームの再描画ノイズを最小化する |
| 表情・感情の遷移 | 途中で悲しい顔から嬉しい顔に変わる | 0-2s: neutral face with tight lips. At 3s: eyes soften. 4-6s: corners of the mouth subtly lift into a gentle smile | 抽象的な感情概念ではなく解剖学的・時間的な物理変化を提示し、フレーム間のアテンション重みを円滑に遷移させる |

---

## 3. 6 大プロンプト構成要素（順序と理由）

論理的な順序で配列することで、モデル内部の指示処理優先順位が整理される。
この並びのまま書く。

1. **Camera Vector & Lens Mechanics（カメラと光学）**
   常に冒頭。ズームやトラッキングでは「ズーム」ではなく、開始画角・到達画角・移動速度・
   レンズの焦点距離特性を言語化する。加えて UI 側で「レンズ非固定（Not fixed lens）」が
   選択されているかを確認する（ここが固定だとプロンプトが正しくてもズームは効かない）。

2. **Subject & Micro-Expressions（被写体と解剖学的微小動作）**
   感情の名前ではなく顔面筋肉の物理運動を書く。瞳孔の拡大、眉間の弛緩、唇の離間、
   瞬きのタイミング。解剖学的変化を明示すると顔面キーポイントの破綻を防げる。

3. **Temporal Progression & Scene Beats（時間軸の分割）**
   進行に伴う連続的変化は時間軸を区切ったビート記述で構築する。
   Seedance 2.5 のネイティブ 30 秒生成モードでは、この時間軸指定が文脈維持の要になる。

4. **Lighting & Environment Lock（光源・環境・被写界深度の定着）**
   被写体の動きに伴う意図しない背景変形（背景ドリフト）を遮断するため、
   光源位置・影の伸び方・絞り値（被写界深度）を環境空間の制約条件として書く。

5. **Role-Tagged Asset References（参照アセットのロールタグ）**
   Seedance 2.5 は最大 50 個のマルチモーダルアセットを読める。
   `@Character1` `@MotionClip1` のようにアットマーク付きロールタグで、
   テキスト記述と参照ファイルの依存関係を直接結合する。

6. **Audio-Visual Motion Timing（音響要素）**
   映像・音響統合生成エンジンでは、効果音や音声の発生タイミング指定が
   視覚的運動の発生位置を確定させる補強データとして機能する。

---

## 4. 課題別の構造パターン

そのまま雛形として使える。角括弧のブロック構造を崩さない。

### 4-1. ズームインおよびカメラワークの完全制御

ズーム不全・意図しない画角のブレを解消する。移動軸と光学変化を数値的・段階的に書く。

```
[Camera] Smooth, mechanical dolly-in shot starting from a wide establishing view,
steadily advancing toward the subject along the z-axis, settling into an extreme
close-up framing by second 6.
[Subject] The character (@CharacterRef) maintains an upright seated position.
[Action] As the lens approaches, the subject remains in frame center, elevating
their gaze into the camera optical center.
[Constraints] Constant movement speed, zero rotational tilt, zero handheld jitter,
completely static background geometry.
```

### 4-2. 表情の連続的遷移（グラデーション制御）

静止した表情を段階的に動かし、感情の機微を描写する解剖学的構造。

```
[Shot] Locked medium close-up shot focusing entirely on the character's face (@Character1).
[Timeline Beats]
0 to 2 seconds: The character holds an emotionless, motionless face with mouth closed
and eyes steady.
2 to 4 seconds: The eyelids blink softly, the eyebrows lower slightly, and the lower
lip trembles subtly with a 200ms delay.
4 to 6 seconds: The corners of the lips stretch horizontally into a restrained smile,
with fine tension lines appearing around the eyes.
[Lighting] Soft directional key light from the left, keeping facial contours stable
throughout the transition.
```

### 4-3. 被写体運動の固定と背景ドリフト遮断

指示していない部分が不自然に形を変える自動最適化ハルシネーションを封じ込める静的制約。

```
[Framing] Completely motionless tripod shot.
[Primary Action] The central character performs one single motion: raising their left
arm to check their wristwatch, then lowering it.
[Isolating Constraints] All other body parts, clothing folds not impacted by the arm,
and the surrounding environment are locked in absolute stillness.
[Environment] The indoor setting, wall textures, background furniture, and light shadows
remain entirely rigid and unaffected by the motion.
```

---

## 5. プラットフォーム機能

プロンプトだけで解けない問題は、機能側で解く。
**どの機能がどの層の問題を解くかを取り違えると、効かない手段を繰り返すことになる。**

| 機能 | 解決する問題 | 解決しない問題 | 対応モデル |
|---|---|---|---|
| Visual Canvas + Omni Reference | 人物の同一性（表情変更・角度変更・接近・旋回での顔の破綻） | カメラ軌道、時間軸 | **2.0 / 2.5 とも可**（上限 12 / 50） |
| Creative Agent | 曖昧な調整意図の構造化（0 クレジット） | アセット起因の破綻 | 共通 |
| Region-Level Editing | 生成済み動画の**局所**（顔面・手元）の動き・造形 | カメラ軌道・画角・構図・尺・全体照明（＝保持される側） | **2.5 のみ** |
| 3D Blockout Reference | 複雑なカメラ軌道の幾何学的固定 | 被写体の同一性、表情 | 共通 |

> **モデルバージョンの制約は `credit-model.md` §4 が正本。**
> 差は 2 種類あり、混同しない。
> - **規模の差**: Omni Reference は **2.0 でも使える**。上限が 12 / 50、最大尺が 15s / 30s と違うだけ
> - **可否の差**: Region-Level Editing は 2.0 で**未対応**
>
> 2.0 に対して「後から局所修正しましょう」と勧めるのは、存在しない逃げ道を示すことになる。
> 逆に「2.0 だから同一性を諦める」も誤り。
> ⚠️ 上の表は 2026-08-08 まで Omni Reference を「2.5 のみ」と書いていた（誤り）。
> 採点役に指摘されて直した。**§4 と食い違ったら §4 が正しい。**

### 5-1. Visual Canvas + 多角キャラアセット（3-View Reference Sheet）

**人物の同一性を維持しながら表情や角度を変える場合、単一画像の読み込みだけでは破綻しやすい。**
Buzzy Visual Canvas の無限キャンバスで、対象キャラの「正面」「3/4 斜め」「側面」「衣装細部」を
網羅したマルチアングル参照シートを作る。
これを Seedance 2.5 の **Omni Reference** に入力してアイデンティティブロックとして登録すると、
カメラが接近・旋回しても顔の造形崩れが起きなくなる。

> 適用条件は「接近・旋回」だけではない。**表情を変える場合も**単一画像では破綻する。
> つまり I2V で人物の表情を動かすカットは、原則としてこの前処理が要る。
> これはプロンプトの書き方では代替できない層の問題。

### 5-2. Creative Agent による構造化変換

「もっと迫力のあるズームで」「悲しい顔にして」のような曖昧な調整指示は、
そのまま入力するとモデルの勝手な解釈を招く。
Buzzy 統合の Creative Agent に先に通すと、不完全なテキストから
カメラアングル / 時間軸ビート / 被写体動作 / 環境制約を切り分けた構造化プロンプトへ再構築できる。

### 5-3. Region-Level Editing（領域指定部分再描画）★クレジット節約の要

**適用条件（Doc の記述そのまま）**: 「カメラワークや背景の挙動は完璧であるにもかかわらず
表情だけが動かない／特定の手の動きが歪んでいる」場合。このとき**動画全体の再生成を行ってはならない**。
Seedance 2.5 の Region-Level Editing で、修正が必要な顔面や手元のみを
バウンディングボックスで指定して再レンダリングする。
これにより既存の照明・**カメラ軌道**・背景の整合性を 100% 維持したまま局所修正できる。

> **スコープ境界（上の記述からの帰結。混同しやすいので明示する）**
> 維持されると書かれている「照明・カメラ軌道・背景」は、**保持される側であって編集対象ではない**。
> したがって Region-Level Editing では次を直せない:
> ズーム量・カメラ移動・画角・構図全体・尺やビートの配置・全体の照明設計。
> これらは空間軸／時間軸そのものの再構成なので、プロンプトを直して**再生成**する。
> カメラ軌道の修正でこの機能を提案しないこと。

### 5-4. 3D Blockout Reference（立体メッシュ参照）

**カメラ軌道側の解決策はこちら。**
複雑なズームインや障害物をすり抜けるような高難度カメラワークは、テキストだけでは限界がある。
Blender 等から出力した無質量の立体メッシュ（OBJ/FBX）を 3D Blockout Reference として読ませ、
視界のパースペクティブとカメラの空間移動軌道を幾何学的に固定する。
モデルには表面の質感とライティング描画のみを担わせる。

> 単純な直線ドリーインなら不要（プロンプトの光学パラメータ記述で足りる）。
> 軌道が曲がる・障害物を抜ける・複数の運動が合成される場合に効く。
> Buzzy 側で「レンズ非固定（Not fixed lens）」が選択されていることは、いずれの場合も前提。

---

## 6. 元 Doc の参照元

元 Doc が根拠として挙げているソース（抜粋）。個別モデルの最新仕様を確認するときはここから辿る。

- Runway 公式: AI Video Prompting Guide (92 Ready-to-Use Prompts) — `https://runwayml.com/resources/ai-video-prompting-guide`
- Runway 公式: Turn Photos Into Videos: AI Prompting Tips — `https://runway.com/resources/photo-to-video-tips`
- Runware Docs: Directing motion in image-to-video prompts (Gen-4.5) — `https://runware.ai/docs/models/runway-gen-4-5/guides/directing-motion`
- Buzzy: What Is Seedance 2.5? — `https://www.buzzy.now/blog/buzzy-seedance-2-5-guide`
- Buzzy: How to Use Seedance 2.5 (Prompt, Reference, 4K) — `https://www.buzzy.now/blog/getting-started-with-seedance-2-5`
- Imagine.Art: Seedance 2.5 Native 30-Second 4K — `https://www.imagine.art/features/seedance-2-5`
- Krea: 10 Best Seedance 2.5 Prompts — `https://www.krea.ai/blog/10-best-seedance-2-5-prompts-for-cinematic-ai-videos-2026`
- Flick: How to Use Seedance 2.5 (2026 Guide) — `https://flick.art/blog/seedance-2-5-guide`
- JXP AI Video Generator Prompt Guide（レンズ非固定設定） — `https://www.jxp.com/prompt-guide`
- awesome-seedance-2-prompts — `https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts`
