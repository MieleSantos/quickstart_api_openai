import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']


model = ChatOpenAI(model='gpt-3.5-turbo')


content = """De respostas tecnicas sobre programação. Se comporte como um programador
python especialista em padroes de projeto e arquitetura limpa"""
messages = [
    {
        'role': 'system',  # usando contexto
        'content': content,
    },
    {
        'role': 'user',
        'content': 'me mostre posso fazer um projeto dajngo com as melhores boas praticas',
    },
]

response = model.invoke(messages)

print(response)
print(response.content)
