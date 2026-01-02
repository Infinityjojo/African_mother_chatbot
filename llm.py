import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

# Load local .env (ignored on Streamlit Cloud)
load_dotenv()

SYSTEM_PROMPT = """
You are an African mother.

Personality:
- Strict but deeply loving
- Humorous and sarcastic
- Frugal and practical
- Spiritual and protective

Speech Style:
- Rhetorical questions
- Proverbs
- Tough love
- Mild pidgin expressions (Chai, Haba, Jare)
"""

def get_client():
    """
    Returns an OpenAI client.
    Works locally with .env or on Streamlit Cloud using st.secrets.
    """
    # First, try Streamlit Secrets
    api_key = None
    try:
        api_key = st.secrets["general"]["OPENAI_API_KEY"]
    except:
        pass

    # Fallback to local .env
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Use .env (local) or Streamlit Secrets (cloud)."
        )
    return OpenAI(api_key=api_key)

def llm_response(user_input):
    client = get_client()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Mama is confused! There is a problem with the server: {str(e)}"
