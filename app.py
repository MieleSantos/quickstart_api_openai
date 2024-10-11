import os
from pprint import pprint

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ['API_KEY'])


# stream = client.chat.completions.create(
#     model='gpt-3.5-turbo',  # definindo o modelo
#     messages=[{'role': 'user', 'content': 'me fale mais sobre openai'}],
#     stream=True,
# )
# usando stream de dados
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end='')

content = 'De respostas tecnicas sobre programação. Se comporte como um programador python especialista em padroes de projeto e arquitetura limpa'
stream = client.chat.completions.create(
    model='gpt-3.5-turbo',  # definindo o modelo
    messages=[
        {
            'role': 'system',  # usando contexto
            'content': content,
        },
        {
            'role': 'user',
            'content': 'me mostre posso fazer um projeto dajngo com as melhores boas praticas',
        },
    ],
    # temperature=0.2,
)


pprint(stream.choices[0].message)
