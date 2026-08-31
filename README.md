# agent-skills

Claude Code / Cursor / Grok Bot が同じ手順を読むための正本。

手順の本文はここだけを直す。`~/.claude/skills/` と `~/.claude/agents/` は symlink。

## 何が入っているか

| パス | 役割 |
|---|---|
| `.cursor/skills/new-project/` | 新規プロジェクトをスクリプトで作り、GitHub・Linear・Obsidian を一括接続 |
| `.cursor/skills/ad-copy/` | 台本・広告文。vidIQ 調査込み |
| `.cursor/skills/buzzy-video-prompt/` | 静止画 / 動画プロンプトの制作ゲート |
| `.cursor/skills/ugc-assets/` | UGC 素材の棚卸しと検品 |
| `.cursor/agents/ad-copy-auditor.md` | 台本の採点役。書き直さない |
| `.cursor/agents/buzzy-prompt-auditor.md` | プロンプト / 生成物の採点役。書き直さない |
| `knowledge/` | 事実・決定。手順は置かない |

Kivori 固有のリリース手順はここには置かない。それは Kivori リポジトリの `.claude/skills/kivori-release/`。

## /new-project を使う

公開スキル: [`.cursor/skills/new-project`](https://github.com/kazuki-0418/agent-skills/tree/main/.cursor/skills/new-project)

前提: `gh auth login`、Linear MCP、Obsidian MCP。未接続の連携はスキップされる。

```
# Cursor: このリポジトリを Plugin / marketplace に足すか、スキルを clone
# Claude Code
/plugin marketplace add kazuki-0418/agent-skills
```

チャットで `/new-project`。名前・置き場・Web か Flutter を聞く。`scripts/setup-project.sh` がフォルダ・git・GitHub を作り、Linear と Obsidian は MCP で紐付ける。

## ローカル（この Mac）

初回セットアップ後、次が同じディレクトリを指している。

```
~/.claude/skills/new-project            →  .cursor/skills/new-project
~/.claude/skills/ad-copy                →  .cursor/skills/ad-copy
~/.claude/skills/buzzy-video-prompt     →  .cursor/skills/buzzy-video-prompt
~/.claude/skills/ugc-assets             →  .cursor/skills/ugc-assets
~/.claude/agents/ad-copy-auditor.md     →  .cursor/agents/ad-copy-auditor.md
~/.claude/agents/buzzy-prompt-auditor.md
~/.cursor/agents/*.md                   →  同じ auditor
```

直すときはこのリポジトリを編集して commit する。symlink 側を直接直しても同じファイルになる。

## プラグイン（growth-squad 向け）

honcho と同じく Team plugins に載せられる。manifest は `.cursor-plugin/plugin.json` と `.claude-plugin/plugin.json`。手順は [docs/plugin.md](docs/plugin.md)。

## Grok Bot

Team plugins に出したあと、Settings → Plugins で Add する。まだ出ていない間はクラウド PC に clone して Read する。詳細は [docs/grok-bot.md](docs/grok-bot.md)。
