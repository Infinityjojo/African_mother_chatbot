import streamlit as st
from llm import llm_response
from chatbot import chatbot, load_knowledge_base

# ----------------------------
# Load knowledge base
# ----------------------------
kb = load_knowledge_base("african_mother_data.json")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="👩🏾‍🍼 African Mother Chatbot", page_icon="👩🏾‍🍼")
st.title("👩🏾‍🍼 African Mother Chatbot")
st.write(
    "Talk to Mama! She will give you advice, scold you, and sprinkle some African wisdom 😉"
)

# Maintain session history
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# User input
# ----------------------------
user_input = st.text_input("What do you want to tell Mama?")

# ----------------------------
# Send button
# ----------------------------
if st.button("Send") and user_input:
    with st.spinner("Mama is thinking..."):
        # 1️⃣ Try knowledge base first
        reply = chatbot(user_input, kb)

        # 2️⃣ If no relevant KB response, fallback to LLM
        if not reply:
            reply = llm_response(user_input)

        # Save in session history
        st.session_state.history.append({"user": user_input, "mama": reply})

        # Display chat
        for chat in st.session_state.history[::-1]:  # show latest first
            st.markdown(f"**You:** {chat['user']}")
            st.markdown(f"**Mama:** {chat['mama']}\n---")
