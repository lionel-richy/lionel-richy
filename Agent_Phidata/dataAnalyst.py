from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os
import json
from phi.tools.duckduckgo import DuckDuckGo
from phi.agent.duckdb import DuckDbAgent

load_dotenv()
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

data_analyst = DuckDbAgent(
    model=Groq(id="qwen-2.5-32b"),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
                }
            ]
        }
    ),
    markdown=True,
)
data_analyst.print_response(
    "Show me a histogram of ratings. "
    "Choose an appropriate bucket size but share how you chose it. "
    "Show me the result as a pretty ascii diagram",
    stream=True,
)
    

