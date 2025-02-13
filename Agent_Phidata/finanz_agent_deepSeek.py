from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools


load_dotenv()
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"], 
    show_tool_calls=True,  
    markdown=True,
)

agent.print_response("résumer et comparer les recommandations des analystes et les fondamentaux de SAP SE et de Daimler")