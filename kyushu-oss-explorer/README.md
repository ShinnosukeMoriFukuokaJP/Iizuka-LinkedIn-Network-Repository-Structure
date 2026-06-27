# kyushu-oss-explorer

**九州各地の旅行記録をOSSとして体系化するアグリゲーター**

> 九州7県の都市を City Node として記録し、JLI-OS に統合できる構造で設計。
> SME向けDX事例・Indo-Pacific 経済圏としての九州を発信するプラットフォーム。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 概要

九州の各都市を「開発可能なオープンデータ」として整理するリポジトリです。

- 各都市を JLI-OS 互換の City Node として記録
- 旅行者・ビジネス・研究者が参照できる構造化データ
- Indo-Pacific 文脈で九州を位置づけるナレッジベース

---

## 対象都市（MVP）

| 都市 | 県 | ステータス |
|------|----|-----------|
| 飯塚市 | 福岡県 | ✅ Reference Node |
| 福岡市 | 福岡県 | 🔄 作成中 |
| 北九州市 | 福岡県 | 📋 予定 |
| 長崎市 | 長崎県 | 📋 予定 |
| 熊本市 | 熊本県 | 📋 予定 |
| 那覇市 | 沖縄県 | 📋 予定 |
| 鹿児島市 | 鹿児島県 | 📋 予定 |

---

## ディレクトリ構成

```
kyushu-oss-explorer/
├── README.md
├── INDEX.md                    # 全都市インデックス
├── indo-pacific-context.md     # 九州のIndo-Pacific的位置づけ
├── cities/
│   ├── fukuoka/
│   │   ├── iizuka/
│   │   │   └── city-node.md   # 飯塚市（Reference）
│   │   └── fukuoka-city/
│   │       └── city-node.md
│   ├── nagasaki/
│   ├── kumamoto/
│   ├── okinawa/
│   └── kagoshima/
└── templates/
    └── city-node-template.md  # 新都市追加用テンプレート
```

---

## Indo-Pacific における九州の位置づけ

九州は地理的・経済的に東アジア・東南アジアとの接点に位置します。

- **福岡市** — 日本のスタートアップ特区・アジアの玄関口
- **長崎市** — 歴史的な日欧・日中交流の拠点
- **那覇市** — 沖縄-台湾戦略回廊の起点（OTSCプロジェクト）
- **飯塚市** — 産業転換モデルとして注目される筑豊地域

---

## 貢献方法

```
1. このリポジトリを Fork
2. cities/[県名]/[都市名]/city-node.md を作成
3. templates/city-node-template.md をコピーして記入
4. Pull Request を送る
```

> ⚠️ 個人情報（氏名・連絡先）を含むデータは提出しないでください。

---

## 関連プロジェクト

- [JLI-OS](https://github.com/ShinnosukeMoriFukuokaJP/Iizuka-LinkedIn-Network-Repository-Structure)
- [iizuka-travel-intel](https://github.com/ShinnosukeMoriFukuokaJP/iizuka-travel-intel)
- [travel-oss-template](https://github.com/ShinnosukeMoriFukuokaJP/travel-oss-template)

---

## 免責事項

- 掲載情報は調査・訪問時点のものです。最新情報は各公式サイトでご確認ください。
- 掲載サービス名は各社の商標です。本リポジトリは各社と無関係です。
- 個人情報・肖像権に配慮した情報のみ掲載しています。

---

*AI HOLDINGS OS 2026 | Kyushu OSS Explorer v1.0 | Iizuka, Fukuoka, Japan*
