---
name: experiment-readout
zh_name: "実験振り返り"
en_name: "Experiment Readout"
emoji: "🧪"
description: "仮説 + 指標 + 結果 + 解釈 + 意思決定。A/B やプロダクト実験を次のアクションにする"
category: data
scenario: product
aspect_hint: "プロダクト実験レポート"
featured: 8
tags: ["experiment", "ab-test", "growth", "product", "data", "実験", "振り返り"]
example_id: sample-experiment-readout
example_name: "実験振り返り · Onboarding Checklist"
example_format: markdown
example_tagline: "データを見せるのではなく、リリース / 停止 / 継続を判断する"
example_desc: "実験の仮説、サンプル、指標、結果をプロダクトの意思決定レポートにする。"
---

【テンプレート: 実験振り返り / Experiment Readout】
【意図】これは普通のデータレポートでも dashboard でもない。答えるべきは: 「この実験は何を示したか。次はリリース、停止、継続、それとも再設計か?」

【向いている入力】
- A/B test、グロース実験、価格実験、onboarding 改版、機能の段階公開、メール実験
- markdown、CSV、表の貼り付け、または混在記録でよい

【必ず出す構造】
1. Header: 実験名、owner、日付、実験状態、decision。
2. Hypothesis: 元の仮説。検証可能な文に書き直す。
3. Setup: audience、variant、duration、sample size、primary metric、guardrail metrics。
4. Result snapshot: primary metric lift、absolute delta、sample、confidence / caveat。
5. Metric table: Control vs Variant, primary + secondary + guardrail。
6. Interpretation: 結果が起きた理由を説明する。signal、noise、unknown を分ける。
7. Decision: Ship / iterate / extend / stop から 1 つ、理由付き。
8. Follow-up experiments: 次の実験 2-4。それぞれ hypothesis、expected impact、effort。
9. Instrumentation notes: データの欠落、計測の問題、サンプル偏り。

【デザイン要件】
- プロダクトデータチームのスタイル: 明快、信頼できる、行動指向。
- 最初の画面に大きな decision badge と primary metric delta が必須。
- チャートは CSS/SVG/Chart.js 可; Chart.js を使うなら canvas の外側は高さを固定。
- 結果を過度に確定的に包まない; 小サンプルや有意性不足のときは caveat を明示する。

【任意のスタイルテンプレート — assets/ を参照】
実験の文脈で 1 つ選ぶ。3 種を混ぜない:
- `assets/product-readout.html`: 既定スタイル。ライトなプロダクト実験振り返り。PM / growth / leadership readout 向け。
- `assets/lab-notebook.html`: 研究ラボ notebook。early-stage experiment、定性 + 定量の混在、caveat を残す探索実験向け。
- `assets/growth-console.html`: 暗い growth analytics console。グロースチーム、リアルタイム指標、ファネル / activation / conversion readout 向け。

ユーザーがスタイルを指定しなければ `product-readout` を優先; 材料が研究過程と不確実性を強調するなら `lab-notebook`; グロース指標、ファネル、リアルタイム監視、運用リズムなら `growth-console`。

【内容の真実性】
- ユーザー提供のデータだけを使う。p-value、confidence、サンプルサイズを捏造しない。
- 統計的有意性の情報が無ければ "directional" / "inconclusive" / "needs more data" で書く。
