from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

agent = Agent(
    model=Groq(id="deepseek-r1-distill-qwen-32b")
)

agent.print_response("Ou est situé le cameroun ?")