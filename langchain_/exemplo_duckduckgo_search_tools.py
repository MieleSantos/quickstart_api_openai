import os

from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

os.environ['OPENAi_API_KEY'] = os.environ['API_KEY']

ddg_search = DuckDuckGoSearchRun()
search_result = ddg_search.run('palmeiras')
print(search_result)
