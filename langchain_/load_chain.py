import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import CSVLoader, PyMuPDFLoader, TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']


model = ChatOpenAI(model='gpt-3.5-turbo')


loader = TextLoader('langchain_\\data\\base_conhecimento.txt')

loader = PyMuPDFLoader('langchain_\\data\\base_conhecimento.pdf')
loader = CSVLoader('langchain_\\data\\base_conhecimento.csv')

documents = loader.load()

prompt_base_conhecimento = PromptTemplate(
    input_variables=['contexto', 'pergunta'],
    template="""
            Use o seguinte contexto para responder à pergunta.
            Responda apenas com base nas infomrações fornecidas.
            Não utilize informações externas ao contexto:
            Contexto: {contexto}
            Pergunta: {pergunta}
        """,
)

chain = prompt_base_conhecimento | model | StrOutputParser()

response = chain.invoke({
    'contexto': '\n'.join(doc.page_content for doc in documents),
    'pergunta': 'Qual óleo de motor devo usar?',
})

print(response)
