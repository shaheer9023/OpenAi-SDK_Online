from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
import os
import asyncio
# from Chatbot import UrduBot
set_tracing_disabled(disabled=True)
key=os.environ["GEMINI_API_KEY"]="MY GEMINI KEY"

client=AsyncOpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

)

model=OpenAIChatCompletionsModel(
    model="gemini-2.5-pro-exp-03-25",
    openai_client=client,


)
async def UrduBot(prompt):

    agent=Agent(
    name="Urdu ChatBot",
    instructions="You are a Urdu Chatbot you only have to answer in roman urdu user can ask questions in other languages but you only have to answer in Roman Urdu",
    model=model,
)
    result=await Runner.run(agent,prompt)
    return(result.final_output)

if __name__ == "__main__":
    prompt = input("enter prompt : ")
    asyncio.run(UrduBot(prompt))