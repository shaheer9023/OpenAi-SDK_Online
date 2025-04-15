import chainlit as cl
from Chatbot import UrduBot
# starter
@cl.on_chat_start
async def start():
    await cl.Message(content="I am Urdu Chatbot").send()
# UI of Chatbot
@cl.on_message
async def UI(message:cl.Message):
    prompt=message.content
    response=await UrduBot(prompt)
    await cl.Message(content=f"Assistant Response : \n {response}").send()