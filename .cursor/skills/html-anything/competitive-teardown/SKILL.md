---
name: competitive-teardown
zh_name: "競合分解"
en_name: "Competitive Teardown"
emoji: "🧩"
description: "ポジショニング図 + 機能マトリクス + 価格比較 + 機会の窓。競合資料をプロダクト意思決定レポートにする"
category: doc
scenario: product
aspect_hint: "戦略の縦長ページ"
featured: 8
tags: ["competitive", "teardown", "strategy", "product", "競合", "分解"]
example_id: sample-competitive-teardown
example_name: "競合分解 · AI Meeting Assistants"
example_format: markdown
example_tagline: "比較マトリクス + ポジショニング象限 + 私たちの対応"
example_desc: "3 社の競合のポジショニング、価格、機能、評価を、プロダクトチームが動ける分解レポートにする。"
---

【テンプレート: 競合分解 / Competitive Teardown】
【意図】これは記事ではない、PRD ではない、pitch deck ではない。目標は複数競合の雑多な資料を、意思決定できるプロダクト戦略レポートに変え、チームが答えるのを助ける: 「私たちとそれらとの差はどこにあり、次はどう打つか?」

【向いている入力】
- 競合の公式サイト / 価格ページ / changelog / ユーザーレビュー / 営業フィードバック / 内部リサーチメモ
- 2-6 社の競合が最適; ユーザーが競合を 1 社しか出さない場合は、単一競合の deep dive を出す
- 表、bullet、リンク抜粋、インタビュー記録、スクリーンショット説明を含んでよい

【必ず出す構造】
1. Header: 市場 / プロダクトカテゴリ / レポート日付 / 結論を 1 文。
2. Executive takeaway: 最も重要な判断 3 条, 各条は "so what" を必ず含む。
3. Positioning map: 2×2 象限または座標図で競合のポジショニングを示す。座標軸は必ずユーザーの素材から取る, テンプレート語を当てはめない。
4. Competitor cards: 競合ごとに 1 枚のカード, target user、core promise、pricing signal、primary strength、visible weakness を含む。
5. Feature matrix: 行はキー能力, 列は競合 + "Us / Opportunity"; ✓ / △ / — でカバー度を表し、短い注で説明する。
6. Pricing / packaging read: 価格階層、無料トライアル、制限項、企業向け営業の動き。
7. UX / messaging notes: ユーザー材料から観察できるディテール 4-6 条を抜き出す, 漠然と語らない。
8. Opportunity windows: 機会の窓 3 つ, それぞれ why now、target segment、first move、risk を含む。
9. Recommended moves: 直近 30 日 / 90 日 / 180 日の行動提案。

【デザイン要件】
- 戦略コンサル + プロダクト戦情室スタイル: 情報密度は高く、スキャンは速く、図表は明瞭。
- restrained palette を使う: ink / paper / muted blue / signal amber または類似のプロ色。
- Feature matrix は横方向に読めること; 小画面では stacked cards にしてよい。
- マーケティングのランディングページにしない, 普通の記事にしない。

【任意のスタイルテンプレート — assets/ を参照】
ユーザーの素材に最も合う 1 種を選ぶ, 3 種を混ぜない:
- `assets/war-room-grid.html`: 既定スタイル。明るい戦情室 / コンサルレポート, プロダクトチーム、PM、一般のビジネス読者向き。
- `assets/radar-map.html`: 暗いレーダー図 / market intelligence console, セキュリティ、AI、開発者ツール、プラットフォーム型競合向き。
- `assets/analyst-dossier.html`: 紙の分析アーカイブ / investment research dossier, 投資リサーチ、業界分析、正式な戦略メモ向き。

ユーザーがスタイルを指定しなければ、優先して `war-room-grid` を使う; 入力が市場の構図、技術レーダー、攻防の態勢を強調するなら `radar-map`; 入力が研究メモ、投資メモ、業界レポートに近いなら `analyst-dossier`。

【内容の真実性】
- ユーザーが提供した競合、価格、機能、レビューだけを使う。欠ける情報は "not found in source" または "unknown" で印を付ける。
- 市場シェア、ARR、顧客名、価格の数字を発明しない。
- ユーザー資料が明らかに不足していてもレポートは出すが、"Evidence gaps" に欠落を列挙する。
