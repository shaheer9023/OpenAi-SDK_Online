from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
import os
import asyncio
set_tracing_disabled(disabled=True)
os.environ["GEMNI_API_KEY"] = 
key = os.environ["GEMNI_API_KEY"]

client=AsyncOpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",


)
model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=client,
)
async def UrduBot():

    agent=Agent(
    name="Urdu ChatBot",
    instructions="You are a Urdu Chatbot you only have to answer in roman urdu user can ask questions in other languages but you only have to answer in Roman Urdu",
    model=model,
)
    return(agent)


