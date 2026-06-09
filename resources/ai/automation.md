# AI Automation for Chikuho SMEs

**Iizuka LinkedIn Network** · Fukuoka Prefecture · Japan

[← AI Resources](README.md)

Connect AI to your business processes to automate repetitive work.

---

## What Is AI Automation?

AI automation means connecting AI tools to your existing workflows so that tasks happen automatically — without you doing them manually each time.

**Example**: Instead of manually checking for new customer emails, writing a response, and saving it to Notion every morning — automation does it while you sleep.

---

## The Free Automation Stack

| Tool | Role | Cost |
|------|------|------|
| [n8n](https://n8n.io/) | Workflow orchestrator (self-hosted = free) | Free |
| [Zapier](https://zapier.com/) | No-code automation (100 tasks/month free) | Free tier |
| [Make](https://make.com/) | Visual automation builder | Free tier |
| Claude API | AI brain for automations | Pay-per-use |
| Google Sheets | Simple data storage | Free |
| Notion | Task management output | Free |

---

## 5 Automations You Can Build Today

### 1. Customer Email → AI Response Draft
```
Gmail receives email → n8n triggers → Claude drafts reply → 
saves to Google Docs for review → notification in Slack
```
**Time saved**: 30 min/day for busy inboxes

### 2. LinkedIn Post Generator
```
You write 1 sentence in Notion → n8n triggers → Claude expands to 
full post with hashtags → saves draft → you review and post
```
**Time saved**: 45 min/week

### 3. Job Application Screener
```
Applications arrive in email → n8n extracts text → Claude scores 
against criteria → summary added to Notion → top candidates flagged
```
**Time saved**: 2–4 hours per hiring round

### 4. Weekly Business Report
```
Every Monday 8AM → n8n pulls Sheets data → Claude writes summary 
report → sent to owner via email
```
**Time saved**: 1 hour/week

### 5. Social Media Monitor
```
Daily → n8n searches for mentions of your business or keywords → 
Claude summarizes → digest sent to your inbox
```
**Time saved**: 30 min/day

---

## Getting Started with n8n

n8n is the recommended tool for Chikuho Region businesses because it is **free when self-hosted** and handles Japanese text well.

### Option A: n8n Cloud (Easiest)
1. Sign up at [n8n.io](https://n8n.io/)
2. Free trial, then ~$20/month
3. No server setup required

### Option B: Self-Hosted (Free)
1. Install on a local computer or ¥1,000/month VPS
2. Access via browser
3. Completely free, your data stays local

### Your First n8n Workflow
1. Open n8n
2. Create a new workflow
3. Add trigger: "Schedule" (every day at 8AM)
4. Add node: "HTTP Request" → call Claude API
5. Add node: "Gmail" → send result to your email
6. Save and activate

---

## Claude API for Automation

For automation, you use the Claude API (not claude.ai). It costs approximately **¥0.2–2 per request** depending on length.

```javascript
// Example API call
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: {
    "x-api-key": "YOUR_API_KEY",
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
  },
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [{
      role: "user",
      content: "Summarize this customer email in 3 bullet points: [email]"
    }]
  })
});
```

→ Get your API key at [console.anthropic.com](https://console.anthropic.com)

---

## Resources

- [n8n documentation (English)](https://docs.n8n.io/)
- [Zapier Help Center (Japanese available)](https://help.zapier.com/)
- [Claude API documentation](https://docs.anthropic.com/)

→ Attend an [AI Workshop](../../events/README.md) to build your first automation live

*Iizuka LinkedIn Network · Chikuho Region · Fukuoka Prefecture · Japan*
