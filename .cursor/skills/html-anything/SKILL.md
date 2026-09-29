---
name: html-anything
description: >-
  単ファイル HTML のテンプレート集（81）。日報・週報なら exec-briefing-memo / weekly-update /
  doc-kami-parchment。デッキ、レポート、LP、ポスターを HTML 1 枚にするときに使う。
  親フォルダに手順は無い。使う型の SKILL.md をこのターンで Read してから書く。
---

# html-anything

テンプレは `.cursor/skills/html-anything/<template>/SKILL.md`。このファイルは入口だけ。

アプリは起動しない。`pnpm install` しない。選んだ型の SKILL.md を Read し、単ファイル HTML を書く。

## レポートでよく使う型

| 名前 | いつ |
|---|---|
| `exec-briefing-memo` | 結論・推奨・根拠を先に出す一枚 |
| `weekly-update` | 横スライドの週報（出した / 進行中 / 止まっている / 指標 / お願い） |
| `doc-kami-parchment` | 読んで残す文書 |
| `data-report` | 数字・CSV が本体 |
| `meeting-notes` | 会議メモが本体 |

日次は `daily-report` エージェント、週次は `weekly-report` エージェントが型を選ぶ。

## 手順

1. 型を決める。決まらなければ `grill-with-docs`。
2. `.cursor/skills/html-anything/<template>/SKILL.md` を Read する。
3. その指示で HTML を組む。英語のクラス名・色コードはそのまま。
4. 保存先は HTML 保存ルール（Obsidian vault の `docs/<project>/`）。リポジトリ内には置かない。
