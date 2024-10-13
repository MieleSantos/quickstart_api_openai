from config import client_grop

chat_completion = client_grop.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': 'me fale sobre o groq',
        }
    ],
    model='llama3-8b-8192',
)

print(chat_completion.choices[0].message.content)
