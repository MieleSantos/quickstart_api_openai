import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']

model = ChatOpenAI(model='gpt-3.5-turbo')

template = """
Traduza o texto do {idioma1} para o {idioma2}:
{texto}
"""

prompt_template = PromptTemplate.from_template(template=template)
texto = 'Boa tarde'
prompt = prompt_template.format(idioma1='português', idioma2='francês', texto=texto)


response = model.invoke(prompt)

print(response.content)
