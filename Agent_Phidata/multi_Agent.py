from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground, serve_playground_app
import uvicorn
from dotenv import load_dotenv



load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    #model=OpenAIChat(id="GPT-4o mini"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
     #model=OpenAIChat(id="GPT-4o mini"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    #model=OpenAIChat(id="GPT-4o mini"),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    storage=SqlAgentStorage(table_name="agent_team", db_file="agents.db"),
    add_history_to_messages=True,
    show_tool_calls=True,
    markdown=True,
)

#agent_team.print_response("Summarize analyst recommendations and share the latest news for SAP", stream=True)

app = Playground(agents=[finance_agent, web_agent, agent_team]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)