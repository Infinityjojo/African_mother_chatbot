import streamlit as st
from chatbot import chatbot, load_knowledge_base

st.set_page_config(
    page_title="African Mother Chatbot",
    page_icon="👩🏾‍🍼",
    layout="centered"
)

st.title("👩🏾‍🍼 African Mother Chatbot")
st.caption("Strict. Loving. Always Right.")

kb = load_knowledge_base()

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Talk to your mother 👀:")

if st.button("Send") and user_input:
    reply = chatbot(user_input, kb)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Mama", reply))

for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**👩🏾 Mama:** {msg}")
