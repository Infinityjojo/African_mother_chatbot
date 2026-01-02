import streamlit as st
from chatbot import chatbot, load_knowledge_base
from llm import llm_response  # safe to import, but do not call yet

kb = load_knowledge_base("african_mother_knowledge_base.json")

st.title("👩🏾‍🍼 African Mother Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("What do you want to tell Mama?")

if st.button("Send") and user_input:
    with st.spinner("Mama is thinking..."):
        # Pass the function as argument to avoid module-level API call
        reply = chatbot(user_input, kb=kb, llm_fn=llm_response)
        st.session_state.history.append({"user": user_input, "mama": reply})

    for chat in st.session_state.history[::-1]:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**Mama:** {chat['mama']}\n---")
