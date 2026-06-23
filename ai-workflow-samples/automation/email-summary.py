# Email Summarization — Automation Concept

# Problem: High email volume buries deadlines and action items.
# Solution: Python-based AI parsing that extracts structured signals from raw email text.
# Impact: Reduces email processing time and ensures no deadline or action item is missed.

def summarize_email(email_text):
    """
    AI-powered email summarization function.
    In production: connect to OpenAI or Anthropic API.
    """

    summary = {
        "main_points": [],
        "action_items": [],
        "priority": "medium"
    }

    # Signal detection logic
    if "deadline" in email_text.lower() or "due" in email_text.lower():
        summary["action_items"].append("Check and log deadline")
        summary["priority"] = "high"

    if "meeting" in email_text.lower():
        summary["main_points"].append("Meeting coordination required")

    if "urgent" in email_text.lower() or "asap" in email_text.lower():
        summary["priority"] = "high"

    if "please review" in email_text.lower():
        summary["action_items"].append("Review requested document")

    return summary


# Example usage
email = """
We need to finalize the project proposal by next Friday.
Please review the attached document ASAP.
We will meet tomorrow to align on next steps.
"""

result = summarize_email(email)
print(f"Priority: {result['priority']}")
print(f"Main points: {result['main_points']}")
print(f"Action items: {result['action_items']}")
