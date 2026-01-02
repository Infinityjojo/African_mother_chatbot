import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

def llm_response(user_input):
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

print("API KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)
