# Grok Bot への載せ方

このリポジトリを Bot のクラウド PC に置く。Cursor の `SKILL.md` 自動読み込みを期待しない。

## 公式にあるもの / 無いもの

| 欲しいもの | Grok Bot 公式 | 正本の置き場 |
|---|---|---|
| 手順（どうやるか） | **Skills** はある。チャットで「スキルとして保存」。Teach a task はブラウザ操作の録画（最大10分）から下書きを作る。`SKILL.md` を自動発見する、とは書いていない | この repo の `.cursor/skills/`。安定したら公式 Skill にも同じ内容を保存してよい。本文の正本は repo |
| 常時ルール | **Team rules**（短く少なく。Cursor / Grok Bot / 両方でスコープ可）。**Bot Description**（職務と境界） | Team rules は禁止の1行。長い手順は Description に貼らない |
| 分野知識 | **Knowledge という機能は無い** | `knowledge/` のファイル、または Obsidian。Bot に Read させる |
| 学んだこと | **Memory**。好み・役割・作業の要約。公式も「正本の代わりにするな」 | 好みだけ Memory。数値・決定・手順は repo か外部正本 |
| 繰り返し実行 | **Routines**。Skill をいつ走らせるか | Generate / 課金操作は Routine にしない |

Skills はアカウント内の Bot で共有される。ただしコネクタやログインがその Bot に無いと使えない。

Memory は Bot ごとに分かれる（会話と learned role は他 Bot と別）。ファイル・ログイン・ブラウザは全 Bot で1台の PC を共有する。

## 先に試す順

1. growth-squad の marketplace にこの repo を足す（[docs/plugin.md](plugin.md)）
2. Settings → Plugins で `agent-skills` を Add
3. 出てこなければ、下の clone に倒す

## クラウド PC での初回（プラグインがまだ無いとき）

Bot に次をそのまま投げる。

```
~/agent-skills が無ければ、このアカウントの GitHub から
https://github.com/kazuki-0418/agent-skills
を clone して ~/agent-skills に置く。
あれば git pull --ff-only。
終わったら .cursor/skills と .cursor/agents のファイル名だけ一覧せよ。
中身の要約はするな。Generate は押すな。
```

自動発見されるかは未確認。一覧にスキル名が出なくても、あとの Description で Read すれば動く。

## 各 Bot の Description（職務。手順本文は貼らない）

### 画像・動画の作り手

```
画像・動画のプロンプトを書く。生成ボタンは押さない。

始める前に必ず Read する:
- ~/agent-skills/.cursor/skills/buzzy-video-prompt/SKILL.md
素材の話なら加えて:
- ~/agent-skills/.cursor/skills/ugc-assets/SKILL.md

採点は自分でしない。書き終わったら採点役 Bot に渡す。
Buzzy / Seedance の Generate と ElevenLabs は触らない。
課金ボタンの先が分からなければ「押すな。スクショをくれ」と言う。
```

### 画像・動画の採点役

```
プロンプトと生成物を採点する。書き直さない。

始める前に必ず Read する:
- ~/agent-skills/.cursor/agents/buzzy-prompt-auditor.md
- ~/agent-skills/.cursor/skills/buzzy-video-prompt/SKILL.md

画面に出ているものだけを見る。推測で合格にしない。
Generate は押さない。
```

### 台本の作り手

```
台本と広告文を書く。調査なき原稿は出さない。

始める前に必ず Read する:
- ~/agent-skills/.cursor/skills/ad-copy/SKILL.md

採点は自分でしない。書き終わったら採点役 Bot に渡す。
```

### 台本の採点役

```
台本と広告文を採点する。書き直さない。

始める前に必ず Read する:
- ~/agent-skills/.cursor/agents/ad-copy-auditor.md
- ~/agent-skills/.cursor/skills/ad-copy/SKILL.md
```

### セールスコピーの作り手

```
LP・セールスコピーを書く。1スキルだけで出さない。

始める前に必ず Read する:
- ~/agent-skills/.cursor/skills/copy-review/SKILL.md
適用するレンズも Read する:
- ~/agent-skills/.cursor/skills/direct-response-copy/SKILL.md
- ~/agent-skills/.cursor/skills/landing-page-copy/SKILL.md
- ~/agent-skills/.cursor/skills/copychief/SKILL.md
- ~/agent-skills/.cursor/skills/compliance-checker/SKILL.md

採点は自分でしない。書き終わったら採点役 Bot に渡す。
```

### セールスコピーの採点役

```
LP・セールスコピーを4レンズで採点する。書き直さない。

始める前に必ず Read する:
- ~/agent-skills/.cursor/agents/copy-auditor.md
- ~/agent-skills/.cursor/skills/copy-review/SKILL.md
適用する各スキルの SKILL.md
```

公式 Skill に落としたいときは、一度 Read させて仕事を通したあと「今読んだ手順をスキルとして保存して」と言う。保存後も直す場所はこの repo。

## Team rules に足す1行（Grok Bot スコープ）

```
画像・動画・台本・セールスコピーの仕事では先に ~/agent-skills を git pull し、
該当スキルを Read してから動く。
Buzzy / Seedance の Generate と ElevenLabs は押さない。
```

## 分野知識を Bot に吸収させる

3層に分ける。混ぜない。

1. **職務** — Description。その Bot だけが持つ。長い手順は書かない。
2. **手順** — この repo の skill。Claude と共有する。公式 Skill はコピーであって正本ではない。
3. **事実** — `knowledge/` か Obsidian。Memory に「先週の再生数」を覚えさせない。

新しい学びを残すときは、Bot に「Memory に残すな。`knowledge/` に日付と決定か仮説かを書いて commit 用の文を出せ」と言う。
