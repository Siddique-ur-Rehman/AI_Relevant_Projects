# app.py
import json
import os
import re
from typing import Any, Dict, Optional, Tuple

import streamlit as st
from dotenv import load_dotenv
from google import genai  # Google Gen AI SDK :contentReference[oaicite:4]{index=4}

from config import (
    MODEL_NAME,
    ALLOWED_CATEGORIES,
    ALLOWED_SENTIMENTS,
    TEMPERATURE,
    FALLBACK,
)
from prompt import build_system_prompt, build_fix_json_prompt


# ---------- Helpers ----------
def extract_json_object(text: str) -> Optional[str]:
    """
    Tries to extract the first {...} JSON object from a text response.
    This helps if the model accidentally adds extra characters.
    """
    if not text:
        return None
    text = text.strip()

    # If it's already clean JSON
    if text.startswith("{") and text.endswith("}"):
        return text

    # Otherwise, try to find a JSON object inside
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    return match.group(0).strip() if match else None


def validate_result(data: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate category/sentiment/reply according to the task rules."""
    if not isinstance(data, dict):
        return False, "Output is not a JSON object."

    for key in ("category", "sentiment", "reply"):
        if key not in data:
            return False, f"Missing key: {key}"

    if data["category"] not in ALLOWED_CATEGORIES:
        return False, f"Invalid category: {data['category']}"

    if data["sentiment"] not in ALLOWED_SENTIMENTS:
        return False, f"Invalid sentiment: {data['sentiment']}"

    if not isinstance(data["reply"], str) or not data["reply"].strip():
        return False, "Reply is empty or not a string."

    # Optional: keep replies short-ish
    if len(data["reply"]) > 350:
        return False, "Reply is too long."

    return True, "OK"


def parse_model_json(text: str) -> Optional[Dict[str, Any]]:
    """Parse model output into JSON dict, with extraction safety."""
    json_str = extract_json_object(text)
    if not json_str:
        return None
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None


@st.cache_resource
def get_client() -> genai.Client:
    """
    Create a Gemini client.
    If GEMINI_API_KEY is set as env var, it can be picked up automatically. :contentReference[oaicite:5]{index=5}
    We'll still allow explicit key if present in env.
    """
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if api_key:
        return genai.Client(api_key=api_key)  # explicit API key supported :contentReference[oaicite:6]{index=6}
    return genai.Client()  # relies on environment variable pick-up :contentReference[oaicite:7]{index=7}


def call_gemini(message: str) -> Dict[str, Any]:
    """Call Gemini, parse JSON, validate, retry once if needed."""
    client = get_client()

    system_prompt = build_system_prompt(ALLOWED_CATEGORIES, ALLOWED_SENTIMENTS)
    full_input = f"{system_prompt}\n\nCustomer message:\n{message}"

    # 1st attempt
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=full_input,
        config={"temperature": TEMPERATURE},
    )
    text1 = getattr(response, "text", "") or ""
    data1 = parse_model_json(text1)

    if data1:
        ok, _ = validate_result(data1)
        if ok:
            return data1

    # 2nd attempt: ask to fix JSON
    fix_prompt = build_fix_json_prompt(text1)
    response2 = client.models.generate_content(
        model=MODEL_NAME,
        contents=fix_prompt,
        config={"temperature": 0.0},
    )
    text2 = getattr(response2, "text", "") or ""
    data2 = parse_model_json(text2)

    if data2:
        ok, _ = validate_result(data2)
        if ok:
            return data2

    # Fallback
    return FALLBACK


# ---------- Streamlit UI ----------
def main():
    load_dotenv()  # loads .env into environment variables

    st.set_page_config(page_title="AI Customer Support Classifier (Gemini)", page_icon="🤖", layout="centered")
    st.title("🤖 AI Customer Support Analyzer (Gemini)")
    st.write("Enter a customer message. The app returns category, sentiment, and a professional auto-reply.")

    # API key check (nice UX)
    if not (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")):
        st.warning(
            "API key not found. Set GEMINI_API_KEY in your environment or in a .env file. "
            "Example: GEMINI_API_KEY=your_key"
        )

    with st.expander("✅ Allowed labels (task rules)", expanded=False):
        st.markdown("**Categories:** " + ", ".join(ALLOWED_CATEGORIES))
        st.markdown("**Sentiments:** " + ", ".join(ALLOWED_SENTIMENTS))

    message = st.text_area(
        "Customer Message",
        height=140,
        placeholder="e.g., I haven't received my order yet. Can you check the delivery status?",
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        analyze = st.button("Analyze Message", type="primary", use_container_width=True)
    with col2:
        clear = st.button("Clear", use_container_width=True)

    if clear:
        st.rerun()

    if analyze:
        if not message.strip():
            st.error("Please enter a message first.")
            return

        with st.spinner("Processing with Gemini..."):
            result = call_gemini(message.strip())

        st.success("Done!")

        st.subheader("Results")
        st.markdown(f"**Category:** {result['category']}")
        st.markdown(f"**Sentiment:** {result['sentiment']}")
        st.text_area("Auto-Reply", value=result["reply"], height=110)

        # Optional: show raw JSON for evaluators
        with st.expander("Show JSON output"):
            st.code(json.dumps(result, indent=2), language="json")


if __name__ == "__main__":
    main()
