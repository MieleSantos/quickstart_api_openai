import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']


model = ChatOpenAI(model='gpt-3.5-turbo')

classification_chain = (
    PromptTemplate.from_template(
        """
            Classifique a pergunta do usuário em um dos seguintes setores:
            - Financeiro
            - Suporte Técnico
            - Outras Informações
            Pergunta: {pergunta}
        """
    )
    | model
    | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
        """
            Você é um especialista financeiro.
            Sempre responda às perguntas começando com "Bem-vindo ao Setor Financeiro".
            Responda à pergunta do usuário:
            Pergunta: {pergunta}
        """
    )
    | model
    | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
        """
        Você é um especialista em suporte técnico.
        Sempre responda às perguntas começando com "Bem-vido ao Suporte Técnico".
        Responda à perguntas do usuário:
        Pergunta: {pergunta}
    """
    )
    | model
    | StrOutputParser()
)

other_info_chain = (
    PromptTemplate.from_template(
        """
        Você é um assistente de informações gerais.
        Sempre responda às perguntas começando com "Bem-vindo as setor de Central de
        Infomações"
        Responda à perguntas do usuário:
        Pergunta: {pergunta}
        """
    )
    | model
    | StrOutputParser()
)


def router(classification):
    classification = classification.lower()

    if 'financeiro' in classification:
        return financial_chain
    elif 'técnico' in classification:
        return tech_support_chain
    else:
        return other_info_chain


pergunta = input('Qual a sua pergunta? ')

classification = classification_chain.invoke({'pergunta': pergunta})

response_chain = router(classification=classification)


reponse = response_chain.invoke({'pergunta': pergunta})
print(reponse)
