# プラグインとして配る

このリポジトリは Cursor Plugin（`.cursor-plugin/plugin.json`）と、Grok Bot が読んでいる Claude 形式（`.claude-plugin/plugin.json`）の両方を持つ。中身の正本は `.cursor/skills/` と `.cursor/agents/`。

NotebookLM のノートは含まれない。配るのは手順だけ。

## growth-squad の Team plugins に出す

honcho と同じ棚に出す。honcho は公開 marketplace（`/plugin marketplace add plastic-labs/claude-honcho`）から来ている。`agent-skills` は private の自前 repo なので、**チーム管理画面で GitHub を Import する**。Grok Bot の Plugins モーダルの Add では repo を足せない。

### ダッシュボードでの足し方

公式: Dashboard → Plugins の Team Marketplaces。出典は [Cursor Plugins](https://cursor.com/docs/plugins.md) と 2.6 の告知。

1. ブラウザで [cursor.com/dashboard](https://cursor.com/dashboard) を開く
2. **個人の Pro+ ではなく、growth-squad のチーム**に切り替える（切替が画面のどこかは見ていない。チーム名が出ている状態にする）
3. 左の **Plugins**（Integrations ではない）
4. **Team Marketplaces** という見出しを探す
5. **Import** / **Add Marketplace** / **Import from Repo** のいずれか（表記は公式でも揺れている）
6. リポジトリにこれを貼る  
   `https://github.com/kazuki-0418/agent-skills`
7. 続行して、プラグイン `agent-skills` が1件見えることを確認して保存

Team Marketplaces が無い = 今見ているのがチーム管理画面ではないか、Teams プランの admin ではない。その画面のスクショをくれれば、そこから続ける。

private なので、そのチームの GitHub App がこの repo を読める必要がある（All repositories なら足りる想定）。

1. 下の「ダッシュボードでの足し方」で repo を Import する
2. Grok Bot アプリ → Settings → Plugins → 検索欄に `agent-skills`
3. Team plugins に出たら **Add**
4. チャットで `/new-project` `/ad-copy` `/copy-review` `/daily-report` `/weekly-report` `/html-anything` が使えるか確認する

出なければ、Plugins の画面をスクショして判断する。項目名は見ていないので書かない。

## この Mac で先に試す

```
ln -sfn /Users/kazukijo/Desktop/dev/agent-skills ~/.cursor/plugins/local/agent-skills
```

Cursor を Reload Window する。説明文が「daily/weekly HTML reports」を含み、Skills が 14（`html-anything` 含む）、Subagents が 5（`daily-report` / `weekly-report` / `copy-auditor` 含む）なら取れている。

カードが Skills 3 / Subagents 2 のまま、説明が「Use when writing ads or UGC scripts」なら、初回 Import の目録が残っている。`version` は `1.1.0`。Uninstall して入れ直す。Team Marketplace なら GitHub の最新 `main` を取り直してから Add する。
