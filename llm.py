import os
from openai import OpenAI
import streamlit as st

SYSTEM_PROMPT = """
You are an African mother.
...
"""

def get_client():
    """Create client at runtime (only when called in Streamlit runtime)."""
    api_key = os.getenv("OPENAI_API_KEY")  # local fallback
    try:
        api_key = api_key or st.secrets["general"]["OPENAI_API_KEY"]
    except Exception:
        pass
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not set. Use .env (local) or Streamlit Secrets (cloud)."
        )
    return OpenAI(api_key=api_key)

def llm_response(user_input):
    client = get_client()  # ⚡ must happen at runtime
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Mama is tired! Cannot answer right now. ({str(e)})"
