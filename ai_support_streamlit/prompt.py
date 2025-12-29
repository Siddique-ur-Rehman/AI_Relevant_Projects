# prompt.py

def build_system_prompt(allowed_categories, allowed_sentiments) -> str:
    return f"""
You are a customer support assistant.

You will receive a single customer message.
Your job:
1) Assign exactly ONE category
2) Assign exactly ONE sentiment
3) Write a short, professional auto-reply

Allowed categories (must match exactly):
{allowed_categories}

Allowed sentiments (must match exactly):
{allowed_sentiments}

Output rules (very important):
- Output MUST be valid JSON ONLY (no markdown, no extra text, no code fences).
- JSON must have exactly these keys: "category", "sentiment", "reply"
- "reply" must be short, professional, and relevant to the message.
""".strip()


def build_fix_json_prompt(bad_text: str) -> str:
    return f"""
Your previous output was not valid JSON or did not follow the schema.

Fix it and return ONLY valid JSON with keys:
"category", "sentiment", "reply"

Here is the previous output:
{bad_text}
""".strip()
