# 👩🏾‍🍼 African Mother Chatbot

*A Hybrid Rule-Based + LLM Conversational AI built with Python &
Streamlit*

------------------------------------------------------------------------

## 📌 Project Overview

The **African Mother Chatbot** is a culturally inspired conversational
AI that mimics the personality of an African mother --- **strict,
loving, humorous, frugal, and deeply spiritual**.

The chatbot combines: - A **rule-based semantic similarity engine**
grounded in a curated knowledge base - A **Large Language Model (LLM)**
fallback for open-ended or unseen queries

This hybrid approach ensures: - Cultural authenticity\
- Fast and cost-efficient responses\
- Flexibility in handling diverse user inputs

------------------------------------------------------------------------

## 🎯 Key Features

-   🧠 Hybrid intelligence (rule-based + LLM)
-   📚 JSON-based cultural knowledge base
-   🧹 Text preprocessing and similarity matching
-   👩🏾‍🍼 Strong African mother personality enforcement
-   💬 Streamlit chat interface
-   🔐 Secure API key handling via environment variables

------------------------------------------------------------------------

## 🧠 System Architecture

User Input\
→ Text Preprocessing\
→ Semantic Similarity Matching (Rule-based)\
→ Confidence Check\
→ Knowledge Base Response **or** LLM Response\
→ Final Output

------------------------------------------------------------------------

## 📁 Project Structure

    african_mother_chatbot/
    │
    ├── african_mother_knowledge_base.json
    ├── app.py
    ├── chatbot.py
    ├── preprocess.py
    ├── llm.py
    ├── requirements.txt
    ├── .env            # (not committed)
    └── README.md

------------------------------------------------------------------------

## 📦 Knowledge Base

The chatbot relies on a structured JSON file containing: - Persona
definition - Core traits - Categorized responses (discipline, education,
food, money, faith, safety) - Proverbs and example intents

This file serves as the chatbot's **cultural memory**.

------------------------------------------------------------------------

## 🧹 Text Preprocessing

Includes: - Lowercasing - Punctuation removal - Stop-word removal -
Tokenization

------------------------------------------------------------------------

## 🤖 LLM Integration

-   Uses OpenAI (`gpt-4o-mini`)
-   Enforced via a system prompt to maintain African mother tone
-   Handles open-ended and unseen queries

### 🔐 API Key Security

The API key is never hard-coded and is loaded from environment
variables.

------------------------------------------------------------------------

## 🖥️ Streamlit Interface

-   Simple chat UI
-   Session-based conversation history
-   Loading spinner during response generation

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### Clone Repository

``` bash
git clone https://github.com/your-username/african-mother-chatbot.git
cd african-mother-chatbot
```

### Create Virtual Environment

``` bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate    # Windows
```

### Install Dependencies

``` bash
pip install -r requirements.txt
```

### Set API Key

Create a `.env` file:

    OPENAI_API_KEY=your-api-key-here

------------------------------------------------------------------------

## ▶️ Run the App

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## ⚠️ Limitations

-   Keyword-based similarity (no embeddings)
-   Requires internet for LLM responses
-   No long-term memory
-   English-focused with limited pidgin
-   Not for medical or mental health advice

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Sentence embeddings (FAISS)
-   Mood slider (strict ↔ caring)
-   Pidgin language toggle
-   Persistent memory
-   Local LLM fallback
-   Deployment to Streamlit Cloud

------------------------------------------------------------------------

## 📚 Learning Outcomes

-   Hybrid chatbot design
-   NLP preprocessing
-   Prompt engineering
-   Secure API usage
-   Streamlit development
-   Cultural AI design

------------------------------------------------------------------------

## 📜 License

Educational and research use only.
