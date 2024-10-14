import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']

model = ChatOpenAI(model='gpt-3.5-turbo')

# prompt_template = PromptTemplate.from_template('Me fale sobre o carro {carro}.')

# runnable_sequsence = prompt_template | model | StrOutputParser()

# response = runnable_sequsence.invoke({'carro': 'astra 2011'})

# print(response)

runnable_sequsence = (
    PromptTemplate.from_template('Me fale sobre o carro {carro}')
    | model
    | StrOutputParser()
)


response = runnable_sequsence.invoke({'carro': 'astra 2011'})


print(response)
