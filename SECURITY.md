# Security Policy / セキュリティポリシー

**Iizuka LinkedIn Network** · Chikuho Region · Fukuoka Prefecture · Japan

---

## Supported Versions

| Branch | Status |
|--------|--------|
| main | ✅ Active |

---

## Reporting a Vulnerability / 脆弱性の報告

セキュリティ上の問題を発見した場合は **GitHub Issues には投稿せず** 以下へご連絡ください:

- GitHub: [@ShinnosukeMoriFukuokaJP](https://github.com/ShinnosukeMoriFukuokaJP) へDM
- LinkedIn Group (ILN): https://www.linkedin.com/groups/14722875 経由

通常 **7日以内** に初回返答します。

---

## ⚠️ APIキー・認証情報の取り扱い / API Key Handling

本リポジトリは APIキー・認証情報を **絶対にコミットしない** ことを原則とします。

### コミットしてはいけないもの（.gitignoreで除外済み）

```
.env
.env.local
.streamlit/secrets.toml
automation/credentials/
automation/secrets/
```

### ✅ 安全な管理方法

```bash
# 1. .env.example をコピーして使う
cp .env.example .env

# 2. .env に実際の値を入力（このファイルはGitに入らない）
# 3. コードからは os.getenv("API_KEY") で読み込む
```

### 万一APIキーをコミットしてしまった場合

1. **即座に該当サービスのキーを無効化・再発行**
   - Anthropic: https://console.anthropic.com
   - Google: https://console.cloud.google.com
   - Slack: https://api.slack.com/apps
   - Zapier: https://zapier.com/app/settings/connected-accounts

2. コミット履歴から削除（BFG Repo-Cleaner 推奨）

3. `git push --force` で履歴を上書き

> ⚠️ GitHub に push した時点でキーは漏洩したとみなしてください。
> 削除より **先にキーの無効化** を必ず行ってください。

---

## 個人情報保護 / Personal Data Protection

本リポジトリの運営は **個人情報の保護に関する法律（個人情報保護法）** に準拠します。

- メンバーの個人情報をリポジトリに保存しないこと
- `cities/` や `jobs/` には公開情報・公開統計のみ掲載
- LinkedInグループのメンバーリスト・連絡先をコミットしないこと
- 個人が特定できるデータを含むファイルは絶対にコミットしないこと

---

## n8n / Zapier ワークフローのセキュリティ

- ワークフロー JSON に認証情報・トークンを直接記載しないこと
- n8n の Credentials は n8n 管理画面で管理
- Zapier の接続情報は Zapier アカウント側で管理
