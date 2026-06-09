# Automation Architecture

**Iizuka LinkedIn Network** · Chikuho Region · Fukuoka Prefecture · Japan

Future automation infrastructure for community management, content, and growth.

---

## Architecture Overview

```
INPUTS                    PROCESSING              OUTPUTS
──────────────────────────────────────────────────────────
RSS Feeds (AI/DX news) ──→ n8n Workflow ──────→ GitHub PR (resource update)
LinkedIn Events ──────────→ n8n + Claude ──────→ EVENTS.md update
Job Board Scrape ─────────→ n8n + Gemini ──────→ jobs/README.md update
GitHub Issues ────────────→ Claude Review ──────→ Auto-label + respond
New PR Submission ────────→ GitHub Actions ─────→ Format check + notify
Newsletter Draft ─────────→ Claude + n8n ───────→ LinkedIn Newsletter post
Member Milestones ────────→ n8n + Slack ────────→ Celebration posts
Event Reminders ──────────→ GitHub Actions ─────→ LinkedIn Event update
```

---

## GitHub Actions Workflows

### `lint-markdown.yml`
Automatically checks all `.md` files for:
- Broken internal links
- Missing breadcrumb navigation
- Required frontmatter fields

### `welcome-contributor.yml`
Triggers on first-time Pull Request:
- Posts welcome message
- Labels PR as `first-contribution`
- Notifies maintainers

### `update-readme-stats.yml`
Weekly automated update of:
- Member count (manual input)
- Event count
- Resource count

### `stale-issues.yml`
Marks issues inactive after 30 days with a comment.

---

## n8n Workflows

### 1. News Aggregation
```
Trigger: Daily 8:00 AM JST
Sources: RSS — AI/DX Japan news, Fukuoka Prefecture announcements
Process: Claude filters for Chikuho relevance
Output: Draft GitHub Issue with resource suggestion
```

### 2. Job Listing Sync
```
Trigger: Weekly Monday
Sources: Indeed JP, LinkedIn Jobs (Fukuoka)
Filter: AI, DX, Engineering roles in Fukuoka Prefecture
Output: Draft PR to jobs/README.md
```

### 3. Event Tracker
```
Trigger: Daily
Sources: Connpass, Doorkeeper, Meetup (Fukuoka)
Filter: AI, DX, Startup, Career events in Chikuho/Fukuoka
Output: Draft update to events/YYYY/README.md
```

### 4. Newsletter Builder
```
Trigger: Last Monday of month
Sources: GitHub repo new files (past 30 days), LinkedIn Group top posts
Process: Claude drafts newsletter in template format
Output: Google Doc draft → human review → LinkedIn Newsletter publish
```

### 5. LinkedIn Content Scheduler
```
Trigger: 3x/week (Mon, Wed, Fri 8:00 AM JST)
Sources: GitHub new resources, upcoming events, member stories
Process: Claude generates LinkedIn post variants
Output: Scheduled LinkedIn post via API
```

---

## AI Models Used

| Model | Role | When |
|-------|------|------|
| Claude | Long-form writing, editorial judgment | Newsletter, articles |
| ChatGPT | Research, brainstorming | Resource curation |
| Gemini | Google integration, real-time search | News aggregation |

---

## Implementation Timeline

| Phase | Automation | Timeline |
|-------|-----------|---------|
| Phase 1 | GitHub Actions: lint, welcome | Month 1 |
| Phase 2 | n8n: news aggregation | Month 3 |
| Phase 3 | n8n: newsletter builder | Month 6 |
| Phase 4 | Full LinkedIn automation | Month 9 |
| Phase 5 | Job listing sync | Year 2 |

---

*This architecture is aspirational. Contributions to build these workflows are welcome.*
*See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.*

*Iizuka LinkedIn Network · Chikuho Region · Fukuoka Prefecture · Japan*
