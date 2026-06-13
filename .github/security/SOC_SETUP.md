# 🛡️ SOC Security System — Setup Guide

## 必要なラベルの作成（GitHub UI）

GitHubリポジトリの Settings → Labels から以下を作成：

| Label | Color | 説明 |
|-------|-------|------|
| `security-critical` | `#d73a49` | Critical severity security issues |
| `security-high` | `#e36209` | High severity security issues |
| `soc-alert` | `#b60205` | SOC auto-generated alert |
| `soc-weekly-report` | `#0075ca` | Weekly SOC scan report |
| `automated` | `#cfd3d7` | Auto-created by workflow |

---

## GitHub Branch Protections（Settings → Branches）

`main` ブランチに以下を設定：

- ✅ Require status checks to pass before merging
  - `🚦 PR Policy Gate` を必須に設定
- ✅ Require branches to be up to date before merging
- ✅ Do not allow bypassing the above settings

---

## Secrets（Settings → Secrets → Actions）

必須ではないが、あると機能が拡張：

| Secret | 用途 | 必須 |
|--------|------|------|
| `SEMGREP_APP_TOKEN` | Semgrep Cloud連携（任意） | ❌ |
| `GITLEAKS_LICENSE` | Gitleaks Pro機能（任意） | ❌ |

> `GITHUB_TOKEN` は自動で利用可能。追加設定不要。

---

## iPhone運用フロー

### 日常チェック（毎日2分）
1. GitHubアプリ → リポジトリ → **Actions** タブ
2. 最新ワークフロー実行を確認
3. ✅ = クリア / ❌ = 調査が必要

### PRレビュー時
1. PRを開くと自動でSOCコメントが投稿される
2. 🚨 BLOCKED → マージしない
3. 🟡 ADVISORY → コメント内の詳細を確認

### アラート対応
1. **Issues** タブ → `soc-alert` ラベルでフィルタ
2. 内容を確認 → Actions artifactでログを確認
3. 対応後にIssueをクローズ

---

## アーキテクチャ概要

```
DETECTION LAYER
├── Gitleaks     → Secret/認証情報漏洩
├── Semgrep      → コード脆弱性 (SAST)
└── Nuclei       → Web脆弱性 (DAST)

ANALYSIS LAYER
├── Severity分類  → CRITICAL/HIGH/MEDIUM/LOW
├── SOCレポート生成
└── Issue自動作成

RESPONSE LAYER
├── Pipeline block (CRITICAL)
├── Merge block (HIGH)
├── PR comment (MEDIUM)
└── Log only (LOW)

AUDIT LAYER
├── Artifacts (90日 / 365日保存)
├── GitHub Security Alerts (SARIF)
└── Weekly Report Issues
```
