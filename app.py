import streamlit as st
from openai import OpenAI
import os

# สร้าง OpenAI client ด้วย API key จาก environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Chat with GPT-4", page_icon="🤖")
st.title("🤖 Chat with GPT-4")

# กล่องรับข้อความจากผู้ใช้
user_input = st.text_input("💬 Ask something")

# เมื่อผู้ใช้กรอกข้อความ
if user_input:
    try:
        # ส่งข้อความไปยัง GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        # แสดงผลลัพธ์ที่ได้จาก GPT
        st.markdown("**🧠 GPT-4 says:**")
        st.success(response.choices[0].message.content)

    except Exception as e:
        st.error(f"❌ Error: {e}")
