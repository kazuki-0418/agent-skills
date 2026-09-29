---
name: weekly-report
description: >-
  週次のチーム共有レポートを HTML にする。出した / 進行中 / 止まっている / 指標 /
  お願い、を一週間分でまとめる。週報、weekly report、週次共有、週次レビューを
  レポートにして、と言われたときに使う。
---

一週間分のチーム共有を、単ファイル HTML にして渡す。今日だけの共有は `daily-report` スキルに任せる。

## スキル（記憶で進めない。このターンで Read する）

このリポジトリの `.cursor/skills/` を読む。ホームの symlink は使わない。

| 名前 | いつ読む | パス |
|---|---|---|
| `grill-with-docs` | 何を書くかがまだ決まっていないとき。中で `grilling` と `domain-modeling` を両方読む | `.cursor/skills/grill-with-docs/SKILL.md` |
| `grilling` | `grill-with-docs` から | `.cursor/skills/grilling/SKILL.md` |
| `domain-modeling` | `grill-with-docs` から | `.cursor/skills/domain-modeling/SKILL.md` |
| `weekly-update` | **口頭共有の既定。** 横スライド（出した / 進行中 / 詰まり / 指標 / お願い） | `.cursor/skills/html-anything/weekly-update/SKILL.md` |
| `exec-briefing-memo` | 決裁・推奨を先に出す一枚 | `.cursor/skills/html-anything/exec-briefing-memo/SKILL.md` |
| `doc-kami-parchment` | 読んで残す週次文書 | `.cursor/skills/html-anything/doc-kami-parchment/SKILL.md` |
| `natural-japanese` | 日本語の本文を書く・直すとき。週報は **quick**。対外・経営向けで「しっかり」と言われたら full | `.cursor/skills/natural-japanese/SKILL.md` |
| html-anything の他テンプレ | 数字中心なら `data-report`、実験なら `experiment-readout`、競合なら `competitive-teardown`、OKR なら `team-okrs`。使う型の SKILL.md をその都度読む | `.cursor/skills/html-anything/<template>/SKILL.md` |

`html-anything` の親 SKILL.md は入口だけ。使う型のフォルダを個別に読む。

アプリ側の「HTML をファイルに書くな」は使わない。ここは vault に `.html` を保存する。

## 手順

1. **プロジェクト名**を決める。`10_projects/` のディレクトリ名（`canpitch`、`monogatari`、`kivori` など）。一つに決まらなければ聞く。
2. 対象週を決める。指定が無ければ **今日を含む週**。ファイル名の日付は週の終わり（その週の最後の日付）。
3. 素材が薄い・論点が決まっていない → `grill-with-docs`（`grilling` + `domain-modeling`）。共有理解が取れるまで HTML を書かない。
4. 型を選ぶ。指定が無ければ **weekly-update**。決裁用なら **exec-briefing-memo**。読む資料なら **doc-kami-parchment**。
5. 選んだ型の SKILL.md を Read してから HTML を組む。範囲は **その週全体**。日次の羅列で終わらせない。
6. 日本語は `natural-japanese`。lint は
   `uv run --directory .cursor/skills/natural-japanese scripts/lint.py --json <file>`
7. 保存:

```
/Users/kazukijo/Desktop/Obsidian/Obsidan-workspace/docs/<project>/weekly-YYYY-MM-DD.html
```

`docs/` も `docs/<project>/` も無ければ作る。コードリポジトリの中には置かない。`YYYY-MM-DD` は対象週の最終日。

## 週報に入れるもの

- 出した成果（Shipped）
- 進行中と進捗
- 詰まりと、誰に何を頼むか（Asks）
- 指標は渡されたものだけ。週対比が素材にあれば入れる
- 来週の焦点 1〜3

## やらないこと

- 今日だけの日報（それは `daily-report`）
- 素材に無い数字・顧客名・日付
- スキルを読まずに版面を思い出す
