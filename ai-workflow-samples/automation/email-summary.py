# Conceptual example: Email summarization workflow

def summarize_email(email_text):
    """
    Simulated AI summary function
    (In real case, connect to OpenAI API)
    """

    summary = {
        "main_points": [],
        "action_items": [],
        "priority": "medium"
    }

    # Example logic (placeholder)
    if "deadline" in email_text:
        summary["action_items"].append("Check deadline")

    if "meeting" in email_text:
        summary["main_points"].append("Meeting related content")

    return summary


# Example input
email = """
We need to finalize the project by next week.
Please join the meeting tomorrow.
"""

print(summarize_email(email))
