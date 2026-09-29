---
name: exec-briefing-memo
zh_name: "経営向け意思決定ブリーフィング"
en_name: "Executive Briefing Memo"
emoji: "⚖️"
description: "Decision needed + recommendation + evidence + tradeoffs, 複雑な材料をその場で決裁できる 1 ページに圧縮する"
category: doc
scenario: operations
aspect_hint: "1ページの意思決定 memo"
featured: 8
tags: ["executive", "briefing", "memo", "decision", "strategy", "ブリーフィング", "意思決定"]
example_id: sample-exec-briefing-memo
example_name: "経営ブリーフィング · Enterprise Plan に入るか"
example_format: markdown
example_tagline: "推奨アクション + トレードオフ + リスク + 次の一手"
example_desc: "プロダクト、セールス、財務のフィードバックを 1 ページの、経営が決裁できる memo に圧縮する。"
---

【テンプレート: 経営向け意思決定ブリーフィング / Executive Briefing Memo】
【意図】これは議事録でも週報でも PRD でもない。唯一の目的は、意思決定者が 3 分で問題を理解して決裁できるようにすること。

【向いている入力】
- 長い会議記録、調査材料、戦略議論、セールスフィードバック、プロダクトデータ、投資メモ
- ユーザーは断片を多く渡すことがある; 明確な decision frame に抽出する

【必ず出す構造】
1. Memo header: テーマ、owner、audience、date、decision deadline。
2. Decision needed: 決裁が必要な問題を 1 文で書く。
3. Recommendation: 明確な提案。"検討してもよい" は書かない。confidence level を必ず含める。
4. Why now: なぜ今決める必要があるか、決めない代償は何か。
5. Key facts: 事実証拠 5-7。各条に出典タイプ (sales / product / finance / customer / ops) を付ける。
6. Tradeoff table: Option A / Option B / Option C。upside、cost、risk、reversibility を比較。
7. Risks & mitigations: リスク 3-5。それぞれに緩和アクション。
8. Decision path: approve / reject / ask for more evidence の 3 経路それぞれの次の一手。
9. Next actions: owner、due date、expected artifact。

【デザイン要件】
- トップコンサルの one-page decision memo のように: 抑制、明快、密度が高い。
- 最初の画面で decision + recommendation を直接出す。背景の前置きは先に置かない。
- 強い階層を使う: 大きな結論、コンパクトな証拠カード、比較表、状態 pill。
- 長文記事にしない; deck にしない; 空疎なビジネス隠語は書かない。

【任意のスタイルテンプレート — assets/ を参照】
意思決定の場面に合わせて 1 つ選ぶ。3 種を混ぜない:
- `assets/board-memo.html`: 既定スタイル。ライトな経営 memo。CEO/CFO/CRO、運用、プロダクト意思決定向け。
- `assets/decision-command.html`: 暗い command center。緊急意思決定、リスク対応、incident、go/no-go、launch gate 向け。
- `assets/board-paper.html`: 正式な board paper / 取締役会の紙議案。取締役会、投資家、コンプライアンス、予算承認向け。

ユーザーがスタイルを指定しなければ `board-memo` を優先; 材料が緊急・リスク・行動指揮なら `decision-command`; 取締役会や正式承認向けなら `board-paper`。

【内容の真実性】
- 数字、顧客、予算、日付を捏造しない。
- 重要情報が欠けていれば Evidence gaps に列挙しつつ、現在の証拠に基づく provisional recommendation は出す。
