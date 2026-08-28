# プラグインとして配る

このリポジトリは Cursor Plugin（`.cursor-plugin/plugin.json`）と、Grok Bot が読んでいる Claude 形式（`.claude-plugin/plugin.json`）の両方を持つ。中身の正本は `.cursor/skills/` と `.cursor/agents/`。

NotebookLM のノートは含まれない。配るのは手順だけ。

## growth-squad の Team plugins に出す

honcho と同じ棚に出す。ダッシュボード操作はこちらからはできない。

1. growth-squad の marketplace にこの GitHub repo を足す  
   `https://github.com/kazuki-0418/agent-skills`  
   Cursor なら Dashboard → Plugins → marketplace に repo を Import / Add  
   private なので、そのチームの GitHub App がこの repo を読める必要がある
2. Grok Bot アプリ → Settings → Plugins → 検索欄に `agent-skills`
3. Team plugins に出たら **Add**
4. チャットで `/ad-copy` `/buzzy-video-prompt` `/ugc-assets` が使えるか確認する

出なければ、Plugins の画面をスクショして判断する。項目名は見ていないので書かない。

## この Mac で先に試す

```
ln -sfn /Users/kazukijo/Desktop/dev/agent-skills ~/.cursor/plugins/local/agent-skills
```

Cursor を Reload Window し、Customize に `agent-skills` と 3 スキル + 採点役 2 つが出るか見る。
