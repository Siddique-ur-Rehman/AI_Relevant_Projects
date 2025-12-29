# config.py

MODEL_NAME = "gemini-2.5-flash"  # quickstart commonly uses gemini-2.5-flash :contentReference[oaicite:3]{index=3}

ALLOWED_CATEGORIES = [
    "Complaint",
    "Refund/Return",
    "Sales Inquiry",
    "Delivery Question",
    "Account/Technical Issue",
    "General Query",
    "Spam",
]

ALLOWED_SENTIMENTS = ["Positive", "Neutral", "Negative"]

# For more deterministic classification/replies:
TEMPERATURE = 0.2

# Safety fallback if the model output is invalid
FALLBACK = {
    "category": "General Query",
    "sentiment": "Neutral",
    "reply": "Thanks for reaching out. Could you please share a bit more detail so we can assist you?",
}
