# LinkedIn Post Generator — English

## 用途
旅行OSSプロジェクトのLinkedIn英語投稿を生成する。旅行後に使用。

---

## プロンプト本文（コピペ用）

```
以下の情報をもとに、LinkedInの英語投稿文を作成してください。

# 条件
・文字数：1,200〜1,500文字（LinkedInの推奨範囲）
・トーン：プロフェッショナル・知識共有型
・必須要素：GitHubリポジトリURL・ハッシュタグ（最大10個）
・視点：Indo-Pacific・OSS・AI活用の文脈を含める
・禁止：他者の個人名・誇大表現

# 入力情報
旅行先：[都市名・都道府県]
期間：[YYYY-MM-DD 〜 MM-DD]
GitHubリポジトリ：[URL]
作ったもの：[箇条書きで]
使ったツール：[iPhoneのみ・無料プランのAIツール等]
都市の特徴：[Indo-Pacific視点で1〜2文]

# 出力形式
・フック（1文）
・作ったもの（箇条書き）
・使ったツール（箇条書き）
・都市の地域的意義（1〜2文）
・Call to Action（Fork・コメント等）
・リポジトリURL
・ハッシュタグ
```

---

## 入力例

```
旅行先：長崎市・長崎県
期間：2026-08-01 〜 08-03
GitHubリポジトリ：https://github.com/ShinnosukeMoriFukuokaJP/nagasaki-oss-2026
作ったもの：旅行記録Markdown・City Node・LinkedInテンプレート
使ったツール：iPhoneのみ・Claudeフリープラン・GitHub
都市の特徴：長崎は江戸時代から日本の国際交流の玄関口として機能し、現在もIndo-Pacific貿易ルートの重要な港湾都市
```

## 注意事項

- 生成された投稿は公開前に事実確認すること
- 「完全無料」「永続的に無料」等の断定表現は避けること
- 他者の個人名が含まれていないか確認すること

---

*ai-travel-prompt-library | AI HOLDINGS OS 2026*
