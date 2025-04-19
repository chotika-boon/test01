import streamlit as st
from openai import OpenAI
import os

# Init OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Config
st.set_page_config(page_title="GPT-4 Chat", page_icon="💬")
st.title("💬 GPT-4 - Single Chat Thread")

# Init session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Input prompt
prompt = st.chat_input("Type your message...")

# Display full chat history as conversation blocks
for i, msg in enumerate(st.session_state.chat_history[1:]):  # skip system
    is_user = msg["role"] == "user"
    with st.chat_message("🧑‍💻 You" if is_user else "🤖 GPT-4", avatar="👤" if is_user else "🧠"):
        st.markdown(msg["content"])

# When user sends a new message
if prompt:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("🧑‍💻 You", avatar="👤"):
        st.markdown(prompt)

    # Get GPT-4 response
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.chat_history
        )
        reply = response.choices[0].message.content

        # Add GPT reply to history
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

        with st.chat_message("🤖 GPT-4", avatar="🧠"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"❌ Error: {e}")
