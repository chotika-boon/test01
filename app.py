import streamlit as st
from openai import OpenAI
import os

# Init OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ตั้งชื่อหน้าเว็บ
st.set_page_config(page_title="💬 GPT-4 Chat", page_icon="🤖")
st.title("💬 GPT-4 Chatbot")

# สร้างตัวแปร session_state สำหรับเก็บประวัติ
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# แสดงประวัติการสนทนา
for msg in st.session_state.messages[1:]:  # ข้าม system
    role = "🧑‍💻 You" if msg["role"] == "user" else "🤖 GPT-4"
    st.chat_message(role).write(msg["content"])

# กล่องรับข้อความใหม่
user_input = st.chat_input("Ask something...")

if user_input:
    # เพิ่มข้อความผู้ใช้ลงประวัติ
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("🧑‍💻 You").write(user_input)

    # เรียก GPT-4 ตอบกลับ
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages
        )
        assistant_reply = response.choices[0].message.content

        # เพิ่มคำตอบ GPT ลงประวัติ
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        st.chat_message("🤖 GPT-4").write(assistant_reply)

    except Exception as e:
        st.error(f"❌ Error: {e}")
