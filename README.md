# agent-skills

Claude Code / Cursor / Grok Bot が同じ手順を読むための正本。

手順の本文はここだけを直す。`~/.claude/skills/` と `~/.claude/agents/` は symlink。

## 何が入っているか

| パス | 役割 |
|---|---|
| `.cursor/skills/ad-copy/` | 台本・広告文。vidIQ 調査込み |
| `.cursor/skills/buzzy-video-prompt/` | 静止画 / 動画プロンプトの制作ゲート |
| `.cursor/skills/ugc-assets/` | UGC 素材の棚卸しと検品 |
| `.cursor/agents/ad-copy-auditor.md` | 台本の採点役。書き直さない |
| `.cursor/agents/buzzy-prompt-auditor.md` | プロンプト / 生成物の採点役。書き直さない |
| `knowledge/` | 事実・決定。手順は置かない |

Kivori 固有のリリース手順はここには置かない。それは Kivori リポジトリの `.claude/skills/kivori-release/`。

## ローカル（この Mac）

初回セットアップ後、次が同じディレクトリを指している。

```
~/.claude/skills/ad-copy                →  .cursor/skills/ad-copy
~/.claude/skills/buzzy-video-prompt     →  .cursor/skills/buzzy-video-prompt
~/.claude/skills/ugc-assets             →  .cursor/skills/ugc-assets
~/.claude/agents/ad-copy-auditor.md     →  .cursor/agents/ad-copy-auditor.md
~/.claude/agents/buzzy-prompt-auditor.md
~/.cursor/agents/*.md                   →  同じ auditor
```

直すときはこのリポジトリを編集して commit する。symlink 側を直接直しても同じファイルになる。

## Grok Bot

公式の Skills は `SKILL.md` の自動発見ではない。クラウド PC にこの repo を clone し、Bot に読ませる。手順は [docs/grok-bot.md](docs/grok-bot.md)。
