import os

from dotenv import load_dotenv
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']

model = ChatOpenAI(model='gpt-3.5-turbo')
python_repl = PythonREPL()

# tranforma função python em uma Tool
python_repl_tool = Tool(
    name='Python REPL',
    description='É um shell python. Use isso para executar código Python.'
    + ' Execute apenas códigos python válidos.Se você precisar obter o retorno'
    + ' do código,use a função "print(...)".',
    func=python_repl.run,
)


# criando o agente
agente_execute = create_python_agent(llm=model, tool=python_repl_tool, verbose=True)

prompt_template = PromptTemplate(
    input_variables=['query'],
    template="""
            Resolva o problema: {query}
    """,
)

query = 'quero uma função de fibonacci com o resultado'

prompt = prompt_template.format(query=query)

response = agente_execute.invoke(prompt)

print(response.get('output'))
