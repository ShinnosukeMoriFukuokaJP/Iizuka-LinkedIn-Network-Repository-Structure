# linkedin-travel-post-generator

**旅行Markdownから LinkedInバイリンガル投稿を自動生成するGitHub Actions**

> 入力：旅行記録Markdown  
> 出力：英語・日本語のLinkedIn投稿テキストファイル  
> 実行：GitHub Actions（無料枠内）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 概要

`travel-record.md` を push するだけで、LinkedIn投稿文を自動生成します。

- **入力**：`input/travel-record.md`
- **出力**：`output/post-en.md`（英語）・`output/post-ja.md`（日本語）
- **実行環境**：GitHub Actions（Python）
- **APIコスト**：なし（テンプレートベース生成）

---

## ディレクトリ構成

```
linkedin-travel-post-generator/
├── README.md
├── input/
│   └── travel-record.md      # ここに旅行記録を入れる
├── output/
│   ├── post-en.md            # 自動生成：英語投稿
│   └── post-ja.md            # 自動生成：日本語投稿
├── scripts/
│   └── generate_posts.py     # 生成スクリプト
└── .github/
    └── workflows/
        └── generate-posts.yml
```

---

## 使い方

### Step 1｜旅行記録を用意する

`input/travel-record.md` に以下のフォーマットで記録を入れる。

```markdown
---
city: 長崎市
prefecture: 長崎県
period: 2026-08-01 〜 08-03
repo_url: https://github.com/ShinnosukeMoriFukuokaJP/nagasaki-oss-2026
tools: iPhone, Claude（無料プラン）, GitHub
---

## 作ったもの
- 旅行記録Markdown
- City Node（JLI-OS互換）
- テンプレート

## 都市の特徴
長崎は江戸時代から日本の国際交流の玄関口として機能してきた港湾都市。
```

### Step 2｜push する

```bash
git add input/travel-record.md
git commit -m "Add travel record: Nagasaki 2026-08"
git push
```

### Step 3｜GitHub Actions が自動実行

push をトリガーに `generate_posts.py` が実行され、
`output/post-en.md` と `output/post-ja.md` が自動生成されます。

### Step 4｜投稿文をコピーして LinkedIn に貼り付ける

---

## 生成される投稿の形式

### 英語版（post-en.md）

```
Just turned my trip to [CITY] into an open-source project on GitHub.

[N] days in [CITY], [PREFECTURE], Japan — here's what I built:
...
```

### 日本語版（post-ja.md）

```
[都市名]への旅行を、GitHubのOSSプロジェクトに変えました。
...
```

---

## 注意事項・免責事項

- 生成された投稿文は必ず公開前に内容を確認してください。
- 他者の個人名・個人情報が含まれていないことを確認してください（個人情報保護法）。
- 「完全無料」等の断定表現は手動で修正してください（景品表示法）。
- 掲載サービス名（GitHub、LinkedIn等）は各社の商標です。本リポジトリは各社と無関係です。
- GitHub Actionsの無料枠は変更される場合があります（2026年6月時点）。

---

*AI HOLDINGS OS 2026 | LinkedIn Travel Post Generator v1.0 | Iizuka, Fukuoka, Japan*
