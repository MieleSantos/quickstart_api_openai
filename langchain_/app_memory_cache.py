import os

from dotenv import load_dotenv
from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

# from langchain_community.cache import InMemoryCache
from langchain_openai import OpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']

model = OpenAI()
# usando cache na memoria
# set_llm_cache(InMemoryCache())

# usando cache no banco de dados
set_llm_cache(SQLiteCache(database_path='openai_cache.db'))


prompt = 'me diga quem foi Alan Turing'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2}')
