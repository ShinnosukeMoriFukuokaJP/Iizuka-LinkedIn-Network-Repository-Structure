# Travel OSS Hub

**Iizuka LinkedIn Network** · Chikuho Region · Fukuoka Prefecture · Japan

[← Home](../README.md) | [Resources](../resources/README.md) | [Cities](../cities/README.md) | [Projects](../projects/README.md)

---

> **旅行は作品制作プロジェクトである。**  
> Every trip is a GitHub repository waiting to be built.

**Travel OSS Hub** は、旅行をオープンソース作品として設計・記録・公開するための完全無料インフラです。  
iPhone + GitHub + Claude の組み合わせで、誰でも再現できます。

---

## What Is This?

| Layer | Description |
|-------|-------------|
| 📐 **Design System** | 旅行プロジェクトをOSSとして設計するテンプレート群 |
| 📝 **Field Recording** | 旅行中にiPhoneで記録するMarkdownテンプレート |
| 🤖 **AI Prompt Library** | Claude無料版で動作する再利用可能プロンプト集 |
| 🌏 **City Intelligence** | JLI-OS形式の都市知識モジュール |
| 🚀 **Publication Pipeline** | GitHub Pages → LinkedIn までの公開フロー |

**対象読者**

- GitHubユーザー・OSS開発者
- AI活用・自動化に関心がある人
- 旅行好きなコンテンツクリエイター
- 地域DX・スマートシティに関わる人

---

## Quick Start

| Goal | Page |
|------|------|
| 旅行OSSプロジェクトを始めたい | [→ Project Template](templates/project-template.md) |
| 旅行中の記録テンプレートが欲しい | [→ Field Log Template](templates/field-log.md) |
| ClaudeプロンプトをGitHubに残したい | [→ Prompt Library](prompts/README.md) |
| READMEをすぐ公開したい | [→ README Template](templates/readme-template.md) |
| 都市ノードを作りたい（JLI-OS形式） | [→ City Node Template](cities/city-node-template.md) |

---

## The Philosophy

```
旅行前：  リポジトリ設計 + プロンプト準備
旅行中：  Markdownで記録 + GitHub push
旅行後：  README完成 + GitHub Pages + LinkedIn投稿
```

**完成定義**：旅行終了時に以下が揃っていること

- [ ] GitHub Repository（公開済み）
- [ ] README（即公開品質）
- [ ] GitHub Pages（静的サイト）
- [ ] Markdown記事 1本以上
- [ ] LinkedIn投稿テキスト（英語・日本語）
- [ ] 再利用可能テンプレート 1個以上

---

## Free Tool Stack

| Tool | Role | Cost |
|------|------|------|
| [GitHub](https://github.com/) | リポジトリ・Pages・Actions | 無料 |
| [Claude](https://claude.ai/) | 設計・文章生成・プロンプト | 無料プラン |
| iPhone | 唯一のデバイス | 既存 |
| [iA Writer](https://ia.net/writer) / メモ帳 | Markdown記録 | 無料 |
| [Working Copy](https://workingcopyapp.com/) | iPhone→GitHub push | 無料プラン |
| [LinkedIn](https://linkedin.com/) | 発信・ネットワーク | 無料 |

---

## Output Types

| Type | Description | Storage |
|------|-------------|---------|
| **設計ドキュメント** | アーキテクチャ・ディレクトリ構成 | GitHub |
| **Markdown記事** | 旅行記・都市レポート・分析 | GitHub + GitHub Pages |
| **プロンプト集** | Claude用・再利用可能 | GitHub |
| **テンプレート** | Fork可能・MIT License | GitHub |
| **LinkedIn投稿** | バイリンガル・Indo-Pacific視点 | LinkedIn |
| **コード** | 必要な場合のみ生成 | GitHub |

---

## Claude Output Protocol

Claude（無料版）を使う際は、毎回この順序で分割実行してください：

```
① 目的
② 完成イメージ
③ ディレクトリ構成
④ 必要な無料ツール
⑤ Claudeで担当する作業
⑥ GitHubで管理するファイル
⑦ Markdownテンプレート
⑧ README
⑨ 改善案
⑩ 次に作るべき作品
```

→ 詳細：[Prompt Library](prompts/README.md)

---

## Repository Structure

```
travel/
├── README.md                    ← このファイル
├── templates/
│   ├── project-template.md      ← 旅行OSSプロジェクト設計テンプレート
│   ├── field-log.md             ← 旅行中の記録テンプレート
│   └── readme-template.md       ← 公開用READMEテンプレート
├── prompts/
│   └── README.md                ← Claudeプロンプトライブラリ
└── cities/
    └── city-node-template.md    ← JLI-OS形式の都市ノードテンプレート
```

---

## Connection to JLI-OS

このハブは **Japan Local Intelligence OS (JLI-OS)** と連携しています。  
旅行先の都市データは JLI-OS の City Node 仕様に準拠して記録・統合できます。

→ 詳細：[City Node Template](cities/city-node-template.md)

---

## License

MIT License — Fork freely, build openly.

*Iizuka LinkedIn Network · AI HOLDINGS OS 2026 · Chikuho Region · Fukuoka Prefecture · Japan*
