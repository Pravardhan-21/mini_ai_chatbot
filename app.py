import os
import streamlit as st
from groq import Groq

# --- Reuse config straight from the CLI chatbot file ---
from main import MODEL, SYSTEM_PROMPT

st.set_page_config(page_title="Simple Chatbot", page_icon="💬")
st.title("💬 Simple Chatbot")

# --- API key: env var first (same as the CLI script checks), else a text box ---
api_key = os.environ.get("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")
if not api_key:
    api_key = st.text_input("Enter your Groq API key:", type="password")
if not api_key:
    st.info("Please provide a Groq API key to start chatting.")
    st.stop()

client = Groq(api_key=api_key)

# --- Keep conversation in session state ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# --- Display chat history (skip the system message) ---
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
user_input = st.chat_input("Type a message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"Error: {e}"

        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})