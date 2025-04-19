import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Chat with GPT")
user_input = st.text_input("Ask something:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    st.write(response.choices[0].message['content'])
