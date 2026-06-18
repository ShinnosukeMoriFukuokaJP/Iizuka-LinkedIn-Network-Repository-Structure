# Security OS — Architecture & Operations Manual

```
Repository: ShinnosukeMoriFukuokaJP/Iizuka-LinkedIn-Network-Repository-Structure
Version: 1.0.0
Classification: Internal
```

---

## 概要

このリポジトリは **Security Operating System (Security OS)** として動作します。  
GitHub Actions をカーネルとし、自己監視・自己検知・自己応答を行う4層構造のセキュリティ基盤です。

---

## アーキテクチャ：4層構造

```
┌─────────────────────────────────────────────────────────────┐
│                    SECURITY OS                              │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │  Git Push   │    │     PR      │    │  Schedule   │     │
│  │  (trigger)  │    │  (trigger)  │    │  (trigger)  │     │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘     │
│         └─────────────────┼────────────────────┘           │
│                           ▼                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ① DETECT LAYER  (detect.yml)                       │   │
│  │                                                     │   │
│  │  Gitleaks → Semgrep → Dependabot → Nuclei           │   │
│  │  [Secret]   [SAST]    [Deps]       [ExtSurf]        │   │
│  │                                                     │   │
│  │  Output: SARIF + JSON artifacts                     │   │
│  └─────────────────────┬───────────────────────────────┘   │
│                        │  workflow_run trigger              │
│                        ▼                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ② ANALYZE LAYER  (analyze.yml)                     │   │
│  │                                                     │   │
│  │  Parse → Classify → Score → Decide                  │   │
│  │                                                     │   │
│  │  CRITICAL(×40) + HIGH(×15) + MED(×5) + LOW(×1)     │   │
│  │       ↓              ↓           ↓         ↓        │   │
│  │  pipeline_fail   pr_block   pr_comment  log_only    │   │
│  └─────────────────────┬───────────────────────────────┘   │
│                        │  workflow_run trigger              │
│                        ▼                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ③ RESPONSE LAYER  (respond.yml)                    │   │
│  │                                                     │   │
│  │  Issue生成 → Fix Branch → Auto PR → PR Comment      │   │
│  │  (全severity) (HIGH+CRIT)  (HIGH+CRIT) (MEDIUM)     │   │
│  │                                                     │   │
│  │  ⚠️ Auto-merge は絶対禁止                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  ④ GOVERNANCE LAYER  (policy.yml + scheduled.yml)   │   │
│  │                                                     │   │
│  │  Branch Protection Check                            │   │
│  │  Workflow Permissions Audit                         │   │
│  │  CODEOWNERS / SECURITY.md / dependabot.yml 検証     │   │
│  │  Audit Log (365日保持)                               │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## データフロー詳細

### detect → analyze

```
detect.yml (Job: aggregate-detect)
  └─ artifact: detection-metadata-{run_id}.json
       └─> analyze.yml reads via actions/download-artifact
            └─ artifact: classified-findings-{run_id}.json
            └─ artifact: analysis-report-{run_id}.json
```

### analyze → respond

```
analyze.yml (Job: trigger-response)
  └─ analysis-report-{run_id}.json
       └─> respond.yml reads risk_label / action_required
            ├─ CRITICAL/HIGH → create-issue + create-fix-pr
            ├─ MEDIUM        → create-issue + comment-on-pr
            └─ LOW           → log_only (no action)
```

### scheduled → audit log

```
scheduled.yml (daily/weekly)
  ├─ S-1: Gitleaks
  ├─ S-2: Semgrep (quick/full)
  ├─ S-3: Nuclei (weekly only)
  ├─ S-4: Dependency audit
  └─ S-5: Audit log entry (365日保持)
       └─ weekly: GitHub Issue "Weekly Scan Report" 自動生成
```

---

## Severity → Action マトリクス

| Severity | スコア閾値 | パイプライン | Issue | Fix PR | PRコメント | ログ |
|----------|-----------|-------------|-------|--------|-----------|------|
| CRITICAL | ≥ 40      | ❌ FAIL      | ✅    | ✅     | -         | ✅   |
| HIGH     | ≥ 15      | ⚠️ Block     | ✅    | ✅     | -         | ✅   |
| MEDIUM   | ≥ 5       | -            | ✅    | -      | ✅        | ✅   |
| LOW      | < 5       | -            | -     | -      | -         | ✅   |

---

## スキャンスケジュール

| スキャン | 頻度 | Gitleaks | Semgrep | Nuclei | Deps |
|---------|------|----------|---------|--------|------|
| Quick   | 毎日 03:00 JST | ✅ | 軽量 | ❌ | ✅ |
| Full    | 毎週月曜 09:00 JST | ✅ | フル | ✅ | ✅ |

---

## Artifact 保持ポリシー

| Artifact | 保持期間 | 用途 |
|----------|---------|------|
| detection-metadata | 90日 | Detect Layer出力 |
| classified-findings | 90日 | Analyze Layer出力 |
| analysis-report | 90日 | Respond Layerインプット |
| governance-report | 90日 | Governance確認 |
| audit-log | **365日** | 法的・監査証跡 |

---

## Governance ルール（必須）

```yaml
# Branch Protection（要手動設定）
main:
  direct_push: BLOCKED
  required_reviewers: 1 (owner)
  dismiss_stale_reviews: true
  require_status_checks: true

# Workflow Permissions（全ファイル共通）
permissions:
  contents: read          # 最小権限
  issues: write           # Issue作成のみ
  pull-requests: write    # PR作成のみ
  security-events: write  # SARIF upload
  actions: read           # artifact download

# 禁止事項
secrets_in_logs: BLOCKED
auto_merge: BLOCKED
write_all_permissions: BLOCKED
```

---

## iPhone 単独運用ガイド

### 必要アプリ（無料）

| アプリ | 用途 |
|--------|------|
| GitHub (公式) | PR承認・Issue確認・ワークフロー手動実行 |
| Safari | GitHub Actionsログ確認 |
| 設定 > メール | GitHub通知メール受信 |

### iPhone での日常オペレーション

#### 1. アラート確認（Issue）
```
GitHub App
  → リポジトリ
    → Issues タブ
      → [CRITICAL] / [HIGH] ラベルでフィルタ
```

#### 2. Fix PR のレビュー・承認
```
GitHub App
  → Pull Requests タブ
    → "Security OS Auto-fix" PR を開く
      → Files changed を確認
        → 問題なければ "Approve" → "Merge"
          ※ Auto-merge は Security OS ポリシーで禁止
```

#### 3. 手動スキャン実行
```
GitHub App
  → Actions タブ
    → "Scheduled Scan — Security OS" を選択
      → "Run workflow" ボタン
        → mode: full / quick / secrets-only を選択
          → "Run workflow" タップ
```

#### 4. Artifact（スキャン結果）確認
```
Safari → github.com/[repo]/actions
  → 対象 Run をタップ
    → Artifacts セクション
      → classified-findings / audit-log をダウンロード
```

#### 5. Branch Protection 確認
```
GitHub App
  → リポジトリ Settings（Webブラウザ）
    → Branches
      → main の Protection Rules を確認
```

### GitHub通知設定（推奨）

```
GitHub App → Settings → Notifications
  ✅ Issues (mentions + assigned)
  ✅ Pull Requests (review requested)
  ✅ Actions (workflow failures only)
  ✅ Security alerts
```

---

## 初回セットアップ手順

### Step 1: YAMLファイルをリポジトリに配置

```bash
# ローカル or GitHub Web Editor で配置
.github/workflows/detect.yml
.github/workflows/analyze.yml
.github/workflows/respond.yml
.github/workflows/policy.yml
.github/workflows/scheduled.yml
```

### Step 2: Branch Protection を手動設定

```
GitHub.com → Settings → Branches → Add rule
Branch name pattern: main

✅ Require a pull request before merging
  ✅ Require approvals: 1
  ✅ Dismiss stale pull request approvals
✅ Require status checks to pass before merging
  ✅ Require branches to be up to date
✅ Restrict who can push to matching branches
  → 自分のアカウントのみ追加
✅ Include administrators
```

### Step 3: Secrets の設定（オプション）

```
Settings → Secrets and variables → Actions

SEMGREP_APP_TOKEN  → Semgrep.dev の無料トークン（省略可）
GITLEAKS_LICENSE   → Community版は不要（省略可）
```

### Step 4: 動作確認

```bash
# 手動でdetect.ymlを実行
Actions → "Detect Layer" → "Run workflow"

# 結果確認
Actions → 実行済みRun → Artifacts
→ detection-metadata-{run_id}.json を確認
```

---

## セキュリティモデル

```
脅威モデル                対策
─────────────────────────────────────────
Hardcoded secrets    → Gitleaks（Detect）+ env化（Respond）
脆弱なコードパターン  → Semgrep OWASP Top10（Detect）
依存パッケージ脆弱性  → npm audit / pip-audit + Dependabot
外部攻撃面            → Nuclei（週次）
不正push              → Branch Protection（Govern）
権限昇格              → permissions: minimum（Govern）
監査証跡欠如          → Artifact 365日保持（Govern）
```

---

*Security OS v1.0 — Built for 1 human + AI agents operating model*  
*Designed for iPhone-only operations in Fukuoka/Chikuho region*
