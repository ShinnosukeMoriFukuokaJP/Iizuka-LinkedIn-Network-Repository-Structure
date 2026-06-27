# Travel OSS GitHub System

**旅行を、GitHubで公開できるOSS作品にするためのシステム**

> "旅行者目線ではなく、GitHubユーザー・OSS開発者・AI利用者・旅行好き — 全員が参考になる設計"

---

## 概要

このディレクトリは、旅行プロジェクトをオープンソースとして設計・記録・公開するための
テンプレート・プロンプト・ワークフロー集です。

- **iPhone のみ**で完結
- **無料プラン**ツールを中心に活用（2026年6月時点の各サービス無料枠を前提）
- **Claude（無料版）**を小さな単位で繰り返し活用
- 旅行終了時に **Fork 可能な OSS** として公開できる状態にする

---

## ディレクトリ構成

```
travel-oss/
├── README.md                  # このファイル
├── SYSTEM_PROMPT.md           # Claude用システムプロンプト（コピペ用）
├── CHECKLIST.md               # 旅行前・中・後のチェックリスト
├── templates/
│   ├── travel-record.md       # 旅行中の記録テンプレート
│   ├── city-node.md           # 都市ノード（JLI-OS互換）
│   ├── linkedin-post.md       # LinkedIn投稿テンプレート（英/日）
│   └── repo-readme.md         # 旅行リポジトリ用READMEテンプレート
└── .github/
    └── workflows/
        └── travel-publish.yml # GitHub Actions（公開自動化）
```

---

## 使い方 — 3フェーズ

### Phase 1｜旅行前（設計）

1. `SYSTEM_PROMPT.md` を Claude にコピペ
2. `CHECKLIST.md` の「旅行前」セクションを完了
3. 新しい GitHub リポジトリを作成
4. `templates/repo-readme.md` をカスタマイズして push

### Phase 2｜旅行中（記録）

1. `templates/travel-record.md` を iPhone のメモに貼り付け
2. 気づき・写真・データを記録
3. Claude で Markdown を整形 → GitHub に push

### Phase 3｜旅行後（公開）

1. `CHECKLIST.md` の「旅行後」セクションを完了
2. `templates/linkedin-post.md` を使って発信
3. GitHub Pages を有効化
4. `templates/city-node.md` を JLI-OS に追加（任意）

---

## ツールスタック（2026年6月時点の無料プランを利用）

| ツール | 用途 | 備考 |
|--------|------|------|
| GitHub | リポジトリ・Pages・Actions | 無料枠あり（利用規約・制限は随時確認を） |
| Claude | コンテンツ生成・整形 | 無料プランで分割実行 |
| iPhone | 記録・編集・push | PCなし完全運用 |
| LinkedIn | 発信 | 無料プラン |
| GitHub Pages | 静的サイト公開 | 無料枠内で利用 |

> **注意**: 各サービスの無料プラン内容・制限は変更される場合があります。
> 利用前に各サービスの最新利用規約をご確認ください。

---

## 対象読者

- **GitHub ユーザー** — 旅行記録をリポジトリとして管理したい人
- **OSS 開発者** — Fork して自分の旅行に使いたい人
- **AI 利用者** — Claude を活用したコンテンツ生成に興味がある人
- **旅行好き** — 旅行を「作品」として残したい人

---

## ライセンス

MIT License — Fork・改変・商用利用すべて自由

---

## 免責事項

- 本テンプレートで言及するサービス名（GitHub、Claude、LinkedIn 等）はそれぞれの企業の商標または登録商標です。本リポジトリはこれらの企業とは無関係であり、公式に承認・提携しているものではありません。
- 旅行記録の公開にあたっては、第三者のプライバシー・肖像権・個人情報の取り扱いに十分注意してください。詳細は `CHECKLIST.md` を参照してください。
- 各ツールの利用は、それぞれのサービス利用規約に従ってください。

---

*Part of [AI HOLDINGS OS 2026](https://github.com/ShinnosukeMoriFukuokaJP) | Built with Claude + iPhone | Iizuka, Fukuoka, Japan*
