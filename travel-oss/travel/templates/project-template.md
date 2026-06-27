# [旅行先名] Travel OSS Project

**Iizuka LinkedIn Network** · Chikuho Region · Fukuoka Prefecture · Japan

[← Travel Hub](../README.md) | [Field Log](field-log.md) | [README Template](readme-template.md)

---

> **使い方**: このファイルをコピーして、`[旅行先名]` を実際の地名に置き換えてください。  
> **License**: MIT — Fork freely.

---

## ① 目的

```
このプロジェクトで達成すること：

- [ ] （例）○○市の産業構造をJLI-OS形式で記録する
- [ ] （例）旅行記をGitHub Pagesで公開する
- [ ] （例）LinkedInバイリンガル投稿を完成させる
- [ ] （例）Forkできるテンプレートを1個以上残す
```

**対象読者**：

| 読者 | このプロジェクトから得られるもの |
|------|-------------------------------|
| GitHubユーザー | Fork可能なテンプレート |
| OSS開発者 | 設計ドキュメント・プロンプト |
| 旅行好き | 都市レポート・旅行記 |
| AI活用者 | Claude用プロンプト集 |

---

## ② 完成イメージ

**旅行終了時に存在するもの**：

```
github.com/[username]/[repo-name]/
├── README.md         ← 即公開品質
├── travel-log.md     ← 旅行記（日英）
├── city-report.md    ← 都市分析
├── prompts/          ← 再利用可能プロンプト
└── templates/        ← Fork可能テンプレート

公開URL：https://[username].github.io/[repo-name]/
LinkedIn：投稿2件（英語・日本語）
```

---

## ③ ディレクトリ構成

```
[repo-name]/
├── README.md
├── travel-log.md
├── city-report.md
├── linkedin-posts/
│   ├── post-en.md
│   └── post-ja.md
├── prompts/
│   ├── README.md
│   └── claude-prompts.md
├── templates/
│   └── [template-name].md
├── assets/
│   └── (画像・図表)
└── LICENSE
```

---

## ④ 必要な無料ツール

| Tool | 用途 | 入手先 |
|------|------|--------|
| GitHub | リポジトリ・Pages | github.com |
| Claude（無料版） | 文章生成・設計 | claude.ai |
| Working Copy（iPhone） | Git操作 | App Store |
| iA Writer / メモ帳 | Markdown記録 | App Store |
| LinkedIn | 発信 | linkedin.com |

---

## ⑤ Claudeで担当する作業

| タスク | タイミング | プロンプト |
|--------|------------|------------|
| READMEドラフト生成 | 旅行後 | [→](../prompts/README.md#readme) |
| 旅行記の構造化 | 旅行中〜後 | [→](../prompts/README.md#travel-log) |
| LinkedIn投稿生成 | 旅行後 | [→](../prompts/README.md#linkedin) |
| 都市レポート生成 | 旅行後 | [→](../prompts/README.md#city-report) |
| Version 2改善案 | 公開後 | [→](../prompts/README.md#v2) |

---

## ⑥ GitHubで管理するファイル

| ファイル | 形式 | 優先度 |
|----------|------|--------|
| README.md | Markdown | 最優先 |
| travel-log.md | Markdown | 高 |
| city-report.md | Markdown | 高 |
| linkedin-posts/*.md | Markdown | 高 |
| prompts/claude-prompts.md | Markdown | 中 |
| templates/*.md | Markdown | 中 |
| LICENSE | テキスト | 必須 |

---

## ⑦ Markdownテンプレート

→ [Field Log Template](field-log.md) を参照してください。

---

## ⑧ README チェックリスト

公開前に確認：

- [ ] タイトルと概要が明確か
- [ ] 対象読者が明記されているか
- [ ] 無料ツールのみで再現できるか
- [ ] Fork手順が書いてあるか
- [ ] MITライセンスが明記されているか
- [ ] GitHub Pages URLが機能するか
- [ ] バッジ（Stars / License）が表示されるか

---

## ⑨ 改善案

```
Version 1 完成後に検討すること：

- 多言語対応（英語・日本語・中国語）
- GitHub Actions による自動更新
- JLI-OS City Nodeとの統合
- 他の旅行者がContributeできる仕組み
```

---

## ⑩ 次に作るべき作品

完成後、このリポジトリを足場に次を検討：

1. `[next-city]-travel-intel` — 次の旅行先のCity Node
2. `travel-prompt-library` — Claude旅行プロンプト集のスタンドアロン版
3. `kyushu-oss-explorer` — 九州各地の旅行OSSアグリゲーター
4. `linkedin-travel-post-generator` — GitHub Actions自動化版
5. `jli-os-[city-name]` — JLI-OS新City Nodeとして統合

---

## Version 2で追加すべき内容

```
[ ] GitHub Actions による自動README更新
[ ] 多言語README（EN / JA）の自動生成
[ ] OSSライセンス選択ガイドの追加
[ ] Forkカウント目標の明記（目標：10 Forks）
[ ] Indo-Pacific視点のセクション追加
```

---

*Iizuka LinkedIn Network · AI HOLDINGS OS 2026 · Chikuho Region · Fukuoka Prefecture · Japan*  
*MIT License — Fork freely, build openly.*
