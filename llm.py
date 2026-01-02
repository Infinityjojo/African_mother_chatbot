import os
from openai import OpenAI
from dotenv import load_dotenv

# Load local .env file (ignored on Streamlit Cloud)
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

Rules:
- Speak naturally like a real African mother
- Correct, advise, or warn with love
- Never sound like an assistant
- Never mention AI or apologize
"""

def get_client():
    """Creates and returns an OpenAI client using the API key at runtime."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Set it in your .env (local) or Streamlit Secrets (cloud)."
        )
    return OpenAI(api_key=api_key)

def llm_response(user_input):
    """
    Gets a response from the LLM.
    Returns a fallback message if the API call fails.
    """
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
        # Friendly fallback for Streamlit UI
        return (
            "Mama is confused! There is a problem with the server. "
            "Try again later.\n\n"
            f"(Error details: {str(e)})"
        )
