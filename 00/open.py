from agents import Agent, Runner
from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY



agent = Agent(
    name="Assistant", 
    instructions="You have to give answer in roman urdu only user can enter promot in other languages but you have to answer in roman urdu if user said to give answer in other language then you have to said that you cant "
    )

prompt=input("enter prompt : ")

result = Runner.run_sync(agent, prompt)
print(result.final_output)

