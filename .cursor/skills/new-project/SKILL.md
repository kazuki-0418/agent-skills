---
name: new-project
description: Scaffolds a new coding project with a deterministic shell script (folder copy, git init, gh repo create), then links Linear and Obsidian via MCP. Use when the user types /new-project or asks to create a new repo, bootstrap Next.js or Flutter, wire GitHub/Linear/Obsidian, stop re-linking tools by hand, or start coding without a setup checklist.
disable-model-invocation: true
---

# new-project

新規プロジェクトを **スクリプトで機械的に** 作り、GitHub・Linear・Obsidian を一度に紐付ける。Cursor / Claude Code 向け。

フォルダコピー・git・`gh repo create` は `scripts/setup-project.sh` に任せる。Linear / Obsidian は **MCP のみ**（シェルに API やトークンを書かない）。

トークンを節約するために、コピー先のツリーやコミット手順をエージェントが考え直さない。スクリプトを叩く。

## 前提

- `gh` が入り、`gh auth login` 済み
- Linear MCP が接続済み（プロジェクトと Issue を作る）
- Obsidian MCP が接続済み（`10_projects/<name>/` にノートを書く）
- 未接続の連携は、そのステップをスキップして完了報告に「未実行」と書く。勝手に curl しない

## やらないこと

- フォルダツリーを自前で `mkdir` / `cp -r` しない
- `scripts/` や `templates/` を実行のたびに編集しない
- Linear / Obsidian を curl / CLI で叩かない
- `DESIGN.md` の Reference 以外を書き換えない
- 認証情報をスクリプトに埋め込まない

## 3層

| 層 | 場所 | 役割 |
| --- | --- | --- |
| テンプレート | `templates/` | コピーするだけの完成ファイル。中身を生成しない |
| スクリプト | `scripts/setup-project.sh` | 決定的なコピー・git・gh |
| 呼び出し | この SKILL.md | 人間に聞き、スクリプトと MCP を順に呼ぶ |

## 進行

```
- [ ] 1. パラメータ収集
- [ ] 2. setup-project.sh
- [ ] 3. DESIGN.md Reference のみ
- [ ] 4. Linear（MCP）
- [ ] 5. Obsidian（MCP）
- [ ] 6. 完了報告
```

---

## 1. パラメータ収集

未指定のものだけ聞く。推測で埋めない。

| 項目 | 値 |
| --- | --- |
| プロジェクト名 | フォルダ名・リポ名・Linear 名・Obsidian フォルダ名 |
| 置き場 | 親ディレクトリ（例: `~/dev`）。既存の作業ルート |
| タイプ | Web (Next.js) → `web-next` / Mobile (Flutter) → `mobile-flutter` |
| GitHub 公開範囲 | `private`（デフォルト）または `public` |
| デザインの参考 | `DESIGN.md` の Reference。なければ「なし」 |

初期 Issue もここで聞く（例: `初期セットアップ完了` / `MVPスコープ定義`）。希望が無ければ、確認したうえでこの 2 件をデフォルトにする。勝手に増やさない。

---

## 2. セットアップスクリプト

このスキルディレクトリからの相対パスで実行する。自前でコピー・git・gh しない。

スキルルートは、この `SKILL.md` があるディレクトリ。

```
bash <skill-root>/scripts/setup-project.sh --root <置き場> <project-name> <type> [visibility]
```

- `type`: `web-next` \| `mobile-flutter`
- `visibility`: `private`（省略時）\| `public`

スクリプトがやること（再実装しない）: `templates/common` + `templates/<type>` を `cp -r`、`*.template` をリネーム、`{{PROJECT_NAME}}` を置換（Flutter の `pubspec.yaml` の `name` だけ snake_case）、`git init`、初期コミット `chore: initial scaffold from _template`、`gh repo create` + push。

標準出力から取る:

- `PROJECT_PATH=`
- `GITHUB_URL=`

失敗したらここで止める。

---

## 3. DESIGN.md Reference のみ

`{PROJECT_PATH}/DESIGN.md` を開く。`## Reference` 直下の `- <TBD>` を、聞いた参考サイト/アプリに置換する。

```markdown
## Reference

<!-- /new-project が対話で聞いた参考サイトだけを書く。他の節は <TBD> のまま残す -->
- https://example.com
```

- 複数なら `- ` を複数行
- 「なし」なら `- <TBD>` のまま
- コメント行は残す
- frontmatter・他見出し・他の `<TBD>` は触らない（該当行だけ置換）

---

## 4. Linear（MCP）

実行時に Linear MCP のツール一覧を確認する。シェルに出さない。

典型ツール（名前は環境で違うことがある）:

| ツール | 用途 |
| --- | --- |
| `get_workspace` / `list_teams` | チーム解決。ID をスキルにハードコードしない |
| `save_project` | プロジェクト作成（`id` なし）。`name` + チーム |
| `get_project` / `list_projects` | URL 取得 |
| `save_issue` | Issue 作成。`title` + `team` + `project` |

手順:

1. ワークスペースとチームを list する。デフォルトチームが不明なら人間に聞く
2. `save_project` — `name` はプロジェクト名
3. 戻り値の URL を保存
4. 聞いたタイトルで Issue を作る

Linear が未接続ならこのステップをスキップし、完了報告に「Linear: 未接続」と書く。

---

## 5. Obsidian（MCP）

Obsidian MCP で書く。シェルで vault パスに直接書き込まない。

既存のプロジェクトノート（`catchup` / `log-decisions` が読める形）に合わせ、次の 3 ファイルだけ作る。vault のプロジェクト根が `10_projects/` でない場合は、既存フォルダを list してそれに揃える。

```
10_projects/<project-name>/README.md
10_projects/<project-name>/decisions.md
10_projects/<project-name>/status.md
```

`overview.md` や `decisions/` フォルダは作らない。既存を上書きしない。

**README.md** — GitHub URL と Linear URL を必ず入れる。

```markdown
---
tags:
  - project
  - <project-name>
---

# <Project Name>

<1行の目的。不明なら「初期セットアップ」>

## リンク

- GitHub: <GITHUB_URL>
- Linear: <LINEAR_PROJECT_URL>
- コード: <PROJECT_PATH>

## 構成

| ファイル | 内容 |
| --- | --- |
| [[decisions]] | 意思決定ログ |
| [[status]] | 現状・次の一手 |
```

**decisions.md** — 空の足場。

```markdown
---
tags:
  - project
  - <project-name>
  - decisions
---

# <Project Name> 意思決定ログ

（まだ決定なし）
```

**status.md** — 初期状態。日付は実行日（YYYY-MM-DD）。

```markdown
---
tags:
  - project
  - <project-name>
  - status
status: active
date: YYYY-MM-DD
---

# <Project Name> ステータス

最終更新: YYYY-MM-DD

## 現在のフェーズ

初期セットアップ完了（template scaffold）。

## 次

- Linear の初期 Issue を消化する
```

Obsidian が未接続ならスキップし、完了報告に「Obsidian: 未接続」と書く。

---

## 6. 完了報告

必ずこの 4 行を出す。未実行は「未実行」と書く。

- 作成フォルダのパス
- GitHub リポジトリ URL
- Linear プロジェクト URL
- Obsidian ノートのパス（README / decisions / status）
