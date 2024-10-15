import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']

model = ChatOpenAI(model='gpt-3.5-turbo')
wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(lang='pt'))


# criando o agente
agente_execute = create_python_agent(llm=model, tool=wikipedia_tool, verbose=True)

prompt_template = PromptTemplate(
    input_variables=['query'],
    template="""
            Pesquise na web sobre {query} e forneça um resumo sobre o assunto.
            Responda tudo em português brasileiro
    """,
)

query = 'Palmeiras'

prompt = prompt_template.format(query=query)

response = agente_execute.invoke(prompt)

print(response.get('output'))
