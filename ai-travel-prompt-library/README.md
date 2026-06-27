# ai-travel-prompt-library

**旅行計画・記録・公開に特化したAIプロンプト集**

> 実際の旅行OSSプロジェクトで使用・検証済みのプロンプトをOSS化。
> Claude・ChatGPT等の主要AIツールで動作確認済み（2026年6月時点）。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 概要

旅行の3フェーズ（計画・記録・公開）それぞれに対応したプロンプトを収録。
iPhone のみ・無料プランで完結する設計を前提としています。

---

## ディレクトリ構成

```
ai-travel-prompt-library/
├── README.md
├── INDEX.md                      # プロンプト一覧
├── phase1-planning/              # 旅行前：計画・設計
│   ├── repo-design.md
│   ├── itinerary-builder.md
│   └── city-research.md
├── phase2-recording/             # 旅行中：記録・整形
│   ├── markdown-formatter.md
│   ├── spot-review.md
│   └── daily-summary.md
├── phase3-publishing/            # 旅行後：公開・発信
│   ├── readme-generator.md
│   ├── linkedin-post-en.md
│   └── linkedin-post-ja.md
└── advanced/                     # 応用
    ├── city-node-builder.md
    └── oss-architect.md
```

---

## 収録プロンプト一覧

### Phase 1｜旅行前
| プロンプト | 用途 |
|-----------|------|
| repo-design | GitHubリポジトリ構成を設計する |
| itinerary-builder | 旅程をMarkdownで構造化する |
| city-research | 都市の基本情報をまとめる |

### Phase 2｜旅行中
| プロンプト | 用途 |
|-----------|------|
| markdown-formatter | 箇条書きメモをMarkdownに整形 |
| spot-review | スポットの記録を構造化 |
| daily-summary | 1日の記録をまとめる |

### Phase 3｜旅行後
| プロンプト | 用途 |
|-----------|------|
| readme-generator | GitHub READMEを生成 |
| linkedin-post-en | LinkedIn英語投稿を作成 |
| linkedin-post-ja | LinkedIn日本語投稿を作成 |

### Advanced
| プロンプト | 用途 |
|-----------|------|
| city-node-builder | JLI-OS互換City Nodeを作成 |
| oss-architect | 旅行OSSプロジェクト全体設計 |

---

## 使い方

各プロンプトファイルは以下の構成になっています。

```
## 用途
## 前提条件
## プロンプト本文（コピペ用）
## 入力例
## 出力例
## 注意事項
```

---

## 動作確認済みAIツール（2026年6月時点）

- Claude（Anthropic）— 無料プラン
- ※ 各AIサービスのプロンプト処理は変更される場合があります

---

## 免責事項

- 本ライブラリで言及するAIサービス名は各社の商標です。本リポジトリは各社と無関係です。
- プロンプトの出力結果は利用するAIサービスや時期により異なります。
- 出力内容の正確性・完全性は保証されません。公開前に必ずご自身で確認してください。

---

*AI HOLDINGS OS 2026 | AI Travel Prompt Library v1.0 | Iizuka, Fukuoka, Japan*
