import os

from dotenv import load_dotenv
from groq import Groq
from openai import OpenAI

load_dotenv()

# usando OPENAI
client = OpenAI(api_key=os.environ['API_KEY'])
# usando GROQ
client_grop = Groq(api_key=os.environ['GROQ_API_KEY'])
