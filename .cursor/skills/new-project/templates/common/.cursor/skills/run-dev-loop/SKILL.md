---
name: run-dev-loop
description: Runs Explorer → Implement → Review → PR as a phased contract. Use when implementing an issue or execution packet, when the user says run-dev-loop / 実装ループ / Explorer, or before editing files on a development task.
---

# /run-dev-loop

Issue または実行パケットをもとに、探索 → 実装 → 検証 → レビュー → PR 作成を進める。

## Role

依頼を最小変更で満たし、機械ゲートを実際に走らせ、レビュー判定を経て PR を作る。

## Inputs

- 引数: Issue 番号、Issue テキスト、または実行パケット
- 引数がない場合: チャット直前の依頼を使う
- 両方ない場合: 停止して依頼内容を要求する

## Forbidden

- スコープを広げない。unrelated refactor をしない
- 人間への確認なしに merge / deploy / publish しない
- `main` へ直接 push しない
- 自動 merge しない
- Explorer phase 完了前にファイル編集（Edit / Write / NotebookEdit）をしない
- Explorer phase 完了前に状態を変えるコマンド（commit / push / install / build / migrate 等）を実行しない。調査用の read-only コマンドは可
- レビュー判定が出る前に PR を作らない。`fix before merge` のまま PR を作らない

## 段階契約

実行は **Explorer → Implement → Review → PR**。**Phase 1 (Explorer) を完了させてから Phase 2 (Implement) に入る。** Explorer 完了前にファイル編集や状態変更コマンドをしない。

**Explorer 完了の判定**: 下記 step 1〜5 を実施し、Explorer report を出し、Elicitation 発火条件の評価を終えた状態。この時点で編集と状態変更コマンドが解禁される。

### Phase 1: Explorer (read-only)

1. 関連する既存コードとドキュメントを読む
2. 影響範囲を特定する（変更ファイル、関連テスト、生成物）
3. PR base を確定する（プロジェクトのブランチ規約があればそれに従う。無ければデフォルトブランチ。**自分の判断で main に直接載せない**）
4. Explorer report を出す
5. スコープ外の重大発見があれば Elicitation を出す。通常の発見は report に書いて Phase 2 へ進む

### Phase 2: Implement

6. Explorer report をベースに、最小変更で受け入れる計画を書く
7. 最小の変更を実装する
8. 機械ゲートを実際に走らせる
9. レビューを行い、判定が `fix before merge` なら 1 回修正して再レビューする
10. 最終判定が `safe to merge` または `confirm before merge` のときだけ PR を作る

## Explorer Report Format

空セクションは「該当なし」と明示する（省略しない）。

```text
# Explorer Report

## Findings
- 関連コード / 既存パターン / ドキュメントから確認した事実

## Assumptions
- 確認していないが暫定的に置いた仮定。根拠を併記する

## Impacted Areas
- 変更が必要なファイル群
- 影響するテスト / ドキュメント / 生成物

## PR Base Decision
- 判定した base
- 根拠

## Open Questions
- スコープ内で曖昧な点
- スコープ外で気になる点
```

## Elicitation

出すときは次の **5 要素** を必須とする。粒度は「部下が 2 つ上の部長に確認する程度」。現場コードを見ていない前提で書く。

1. **文脈** — どの依頼のどのフェーズで作業中か
2. **発見** — 何が起きて、なぜ判断が必要か
3. **影響** — それぞれの選択肢で何が起きるか
4. **選択肢** — 2〜4 個。Yes/No ではなく内容で選べる形式
5. **推奨** — 現時点の判断と理由

禁止例: 「問題があります。続けますか?」「これで OK ですか?」「方針を確認してください」

### 発火条件

- 認証 / 課金 / 権限境界 / 個人情報の判断が必要
- 受け入れ条件だけでは挙動が一意に決まらない
- 凍結された受け入れ条件と実コードに矛盾がある
- スコープ外の制約・前提を発見した
- 要件が実質的に不明瞭

発火しない（report に書いて Phase 2 へ）:

- スコープ内の通常の選択肢（どちらでも受け入れ条件を満たせる）
- 軽微な命名や comment の追加判断
- スコープ外でも実害が無い軽微な発見

## Stop Conditions

次の場合は即座に停止する。

- 認証 / 課金 / 権限境界 / 個人情報の判断が必要
- 要件が実質的に不明瞭
- ゲートが失敗し、現在のスコープで解決できない
- 1 回の修正後もレビューが `fix before merge` を返す
- シークレット漏えいの疑い

停止時の出力:

```text
# Blocked
## Reason
## What Needs Human Confirmation
## Current Status
```

## Validation / Gate report

- ゲート結果は `Gates Passed` / `Gates Failed` / `Gates Not Run` のいずれか 1 つ
- 走らせていないゲートを passed と書かない

## PR 作成

- merge しない。`gh pr merge` を呼ばない
- publish しない
- 検証していない項目は PR body に「未検証」として列挙する
