import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()  # local dev

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
    """Create OpenAI client at runtime, works for Streamlit and local."""
    api_key = None
    if "OPENAI_API_KEY" in os.environ:
        api_key = os.environ["OPENAI_API_KEY"]
    else:
        # Only access Streamlit secrets inside interactive session
        try:
            api_key = st.secrets["general"]["OPENAI_API_KEY"]
        except:
            pass

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Use .env (local) or Streamlit Secrets (cloud)."
        )
    return OpenAI(api_key=api_key)


def chatbot(user_input, kb=None):
    # 1️⃣ Try knowledge base first
    if kb:
        for q, a in kb.items():
            if q.lower() in user_input.lower():
                return a

    # 2️⃣ Try LLM if KB has no match
    try:
        return llm_response(user_input)
    except Exception as e:
        # 3️⃣ Fallback if LLM fails (e.g., quota exceeded)
        return "Mama is tired now! I cannot think properly. Try asking something else or check your question in my wisdom database."
