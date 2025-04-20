from agents import Agent, Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

provider=AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/", 



)

model=OpenAIChatCompletionsModel(
    model="gemini-2.5-pro-exp-03-25",
    openai_client=provider,
)



agent = Agent(

    name="Assistant", 
    instructions="You have to give answer in roman urdu only user can enter promot in other languages but you have to answer in roman urdu if user said to give answer in other language then you have to said that you cant ",
    model=model,


        )

prompt=input("enter prompt : ")

result = Runner.run_sync(
        agent, 
        prompt
        )

print(result.final_output)

