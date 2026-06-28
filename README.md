# Iizuka LinkedIn Network & AI Systems Portfolio

**Shinnosuke Mori** · Iizuka, Fukuoka, Japan · Built entirely on iPhone · ¥0 infrastructure

> *"Systems beat heroics. Reproducibility beats talent."*

---

## 🗂 このリポジトリに含まれるシステム

| システム | カテゴリ | 概要 |
|---------|---------|------|
| [飯塚・筑豊 LinkedIn Network](#-chikuho-regional-dx-platform) | 🌏 地域DX | 筑豊11市町村カバー・GitHub Pages公開中 |
| [Security OS](#-security-os--devsecops-pipeline) | 🔒 セキュリティ | Gitleaks・OWASP ZAP・自己修復型パイプライン |
| [Autonomous AI PR Engine](#-autonomous-ai-pr-engine) | 🤖 AI自動化 | blast-radius制限・バグ学習DB・自律PR生成 |
| [GitHub Actions × Claude API Pipeline](#-github-actions--claude-api-pipeline) | ⚡ 自動化 | Issue自動応答・PR自動生成 |
| [LinkedIn Network Analysis AI](#-linkedin-network-analysis-ai) | 📊 分析AI | NetworkX × Claude API・4層アーキテクチャ |
| [Shimonoseki LN Repository](#-shimonoseki-linkedin-network) | 🌏 地域DX | 山口県下関市・Streamlit実装 |
| [Japan Local Intelligence OS (JLI-OS)](#-japan-local-intelligence-os) | 🗾 知識基盤 | 都市=リポジトリ構造・25+ファイル |
| [Travel OSS System](#-travel-oss-system) | ✈️ 自動化 | 旅行先ごとにリポジトリ自動生成 |

---

## 🌏 Chikuho Regional DX Platform

**筑豊地域（飯塚・田川・直方ほか11市町村）のDXプラットフォーム**

- 90+ ファイル構成 · GitHub Pages で公開中
- 企業情報・求人・イベント・地域データを統合
- 日英バイリンガル対応

```
cities/          → 各市町村ページ（14都市）
companies/       → 地域企業データベース
docs/            → 戦略・ガバナンス文書
.github/         → 自動化ワークフロー
```

---

## 🔒 Security OS / DevSecOps Pipeline

**iPhone のみで構築した自己修復型セキュリティシステム**

- **Gitleaks** — APIキー・シークレット漏洩検出
- **Semgrep** — 静的コード解析・脆弱性スキャン
- **Nuclei** — 既知の脆弱性テンプレートスキャン
- **OWASP ZAP** — Webアプリケーションセキュリティテスト
- 脆弱性検出時に自動で修正PRを生成するガードレール付き

> ✅ Secret scanning で APIキー漏洩ゼロを確認済み（2026年6月28日）

---

## 🤖 Autonomous AI PR Engine

**ガードレール付き自律 AI Pull Request エンジン**

- **Blast-radius 制限** — 1PRあたりのファイル変更数を制限
- **バグ学習 DB** — 過去の失敗パターンを記録・再発防止
- **Unified diff 出力** — 変更内容を人間が検証可能な形式で出力
- 完全自律稼働しながら暴走リスクを3層で抑制

---

## ⚡ GitHub Actions × Claude API Pipeline

**Issue への自動応答と PR 自動生成パイプライン**

- GitHub Issues にラベルを付けると Claude API が自動応答
- `/tmp/issue_context.json` を経由したマルチライン対応（v3で安定）
- Python `urllib` のみで実装（外部ライブラリ不使用）

---

## 📊 LinkedIn Network Analysis AI

**NetworkX × Claude API による LinkedIn ネットワーク分析システム**

- 4層アーキテクチャ（収集・解析・生成・出力）
- NetworkX でグラフ構造を分析
- 日本のスクレイピング規制（不正競争防止法）に準拠した設計

---

## 🌏 Shimonoseki LinkedIn Network

**山口県下関市の LinkedIn ネットワークリポジトリ**

- 30+ ファイル構成
- Streamlit による可視化ダッシュボード
- 下関市の産業・企業・地域特性データを統合

---

## 🗾 Japan Local Intelligence OS

**「都市=リポジトリ」構造の日本版地域知識インフラ**

- 各都市の知識ベースを GitHub リポジトリとして管理
- AIエージェントによる自動更新設計
- 25+ ファイル生成済み · 日本法コンプライアンス審査中

---

## ✈️ Travel OSS System

**旅行先ごとに fork 可能なリポジトリを自動生成するシステム**

- 旅行記録をそのまま OSS として公開
- 日英バイリンガルの LinkedIn 投稿を自動生成
- GitHub Actions で全工程を自動化

---

## 🛠 Tech Stack

| レイヤー | 使用技術 |
|---------|---------|
| **AI** | Claude API (Anthropic) · NetworkX |
| **自動化** | GitHub Actions · Zapier · n8n |
| **セキュリティ** | Gitleaks · Semgrep · Nuclei · OWASP ZAP |
| **言語** | Python (urllib のみ) |
| **フロントエンド** | GitHub Pages · Streamlit |
| **開発環境** | iPhone Safari のみ · PC不使用 · ¥0 |

---

## 📌 About

- **開発者**: Shinnosuke Mori
- **拠点**: 福岡県飯塚市（筑豊地域）
- **開発期間**: 2024年11月〜現在
- **開発環境**: iPhone Safari のみ（PC不使用）
- **コスト**: ¥0（全て無料ツール）
- **GitHub**: [ShinnosukeMoriFukuokaJP](https://github.com/ShinnosukeMoriFukuokaJP)

---

*現場を知った上でデジタル化を推進できる人材を目指しています。*
*DX推進・AI導入支援に関するご連絡はLinkedInまたはGitHub Issuesからどうぞ。*
