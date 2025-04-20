import chainlit as cl
from gemini import UrduBot
# starter
@cl.on_chat_start
async def start():
    cl.user_session.set("history",[])
    await cl.Message(content="I am Urdu Chatbot").send()
# UI of Chatbot
@cl.on_message
async def UI(message:cl.Message):
    history=cl.user_session.get("history")
    prompt=message.content
    history.append({"role":"user","content":prompt})
    response=await UrduBot(history)
    history.append({"role":"assistant","content":response})
    await cl.Message(content=f"Assistant Response 👇 \n {response}").send()
    