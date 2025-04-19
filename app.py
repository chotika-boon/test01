import openai

openai.api_key = 'YOUR_API_KEY'  # เปลี่ยนเป็น API key ของคุณ

def stream_chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        stream=True  # เปิดโหมด Streaming
    )

    for chunk in response:
        if 'choices' in chunk:
            delta = chunk['choices'][0]['delta']
            if 'content' in delta:
                print(delta['content'], end='', flush=True)

if __name__ == "__main__":
    user_prompt = input("You: ")
    print("ChatGPT: ", end='', flush=True)
    stream_chat(user_prompt)
