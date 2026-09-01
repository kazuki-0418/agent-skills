**English** | [日本語](README.ja.md)

# agent-skills

Canonical instructions for Claude Code, Cursor, and Grok Bot.

Edit procedure text here only. `~/.claude/skills/` and `~/.claude/agents/` are symlinks.

## What's in here

| Path | Role |
|---|---|
| `.cursor/skills/new-project/` | Scaffold a new project and wire GitHub, Linear, and Obsidian in one pass |
| `.cursor/skills/ad-copy/` | Ad copy and scripts, including vidIQ research |
| `.cursor/skills/buzzy-video-prompt/` | Production gate for still and video prompts |
| `.cursor/skills/ugc-assets/` | UGC asset inventory and review |
| `.cursor/skills/copy-review/` | One-pass write + review through four copy skills |
| `.cursor/skills/direct-response-copy/` | Sales copy (Palmer). Loaded by copy-review |
| `.cursor/skills/landing-page-copy/` | Bridge / pre-sell landers. Loaded by copy-review |
| `.cursor/skills/copychief/` | Copy-chief review format. Loaded by copy-review |
| `.cursor/skills/compliance-checker/` | Platform policy check. Loaded by copy-review |
| `.cursor/agents/ad-copy-auditor.md` | Scores ad copy. Does not rewrite |
| `.cursor/agents/buzzy-prompt-auditor.md` | Scores prompts and outputs. Does not rewrite |
| `.cursor/agents/copy-auditor.md` | Scores LP / sales copy across four lenses. Does not rewrite |
| `knowledge/` | Facts and decisions. No procedures |

Kivori-specific release steps do not live here. Those stay in the Kivori repo at `.claude/skills/kivori-release/`.

## Using /new-project

Public skill: [`.cursor/skills/new-project`](https://github.com/kazuki-0418/agent-skills/tree/main/.cursor/skills/new-project)

Requires: `gh auth login`, Linear MCP, Obsidian MCP. Unconnected integrations are skipped.

```
# Cursor: add this repo as a plugin / marketplace, or clone the skill
# Claude Code
/plugin marketplace add kazuki-0418/agent-skills
```

Type `/new-project` in chat. It asks for a name, parent folder, and Web vs Flutter. `scripts/setup-project.sh` creates the folder, git repo, and GitHub remote. Linear and Obsidian are linked via MCP.

## Local (this Mac)

After first setup, these paths point at the same directories.

```
~/.claude/skills/new-project            →  .cursor/skills/new-project
~/.claude/skills/ad-copy                →  .cursor/skills/ad-copy
~/.claude/skills/buzzy-video-prompt     →  .cursor/skills/buzzy-video-prompt
~/.claude/skills/ugc-assets             →  .cursor/skills/ugc-assets
~/.claude/skills/copy-review            →  .cursor/skills/copy-review
~/.claude/skills/direct-response-copy
~/.claude/skills/landing-page-copy
~/.claude/skills/copychief
~/.claude/skills/compliance-checker
~/.claude/agents/ad-copy-auditor.md     →  .cursor/agents/ad-copy-auditor.md
~/.claude/agents/buzzy-prompt-auditor.md
~/.claude/agents/copy-auditor.md
~/.cursor/agents/*.md                   →  same auditors
```

Edit this repository and commit. Changing the symlink side edits the same files.

## Plugin (growth-squad)

Same Team plugins shelf as honcho. Manifests are `.cursor-plugin/plugin.json` and `.claude-plugin/plugin.json`. Steps: [docs/plugin.md](docs/plugin.md).

## Grok Bot

After it is on Team plugins, add it from Settings → Plugins. Until it appears, clone it onto the cloud PC and Read it. Details: [docs/grok-bot.md](docs/grok-bot.md).
