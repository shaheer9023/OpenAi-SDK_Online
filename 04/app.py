import chainlit as cl
from gemini import UrduBot
import asyncio
from agents import Agent,Runner
# starter
@cl.on_chat_start
async def start():
    cl.user_session.set("history",[])
    await cl.Message(content="I am Urdu Chatbot").send()
# UI of Chatbot
@cl.on_message
async def UI(message:cl.Message):
    history=cl.user_session.get("history")
    msg=cl.Message(content=f"Assistant Response 👇 \n")
    await msg.send()

    prompt=message.content
    history.append({"role":"user","content":prompt})

    # Streaming

    response=Runner.run_streamed(
        starting_agent=await (UrduBot()),
        input=history,
    )
    async for event in response.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                token = event.data.delta
                await msg.stream_token(token)
    history.append({"role": "assistant", "content": msg.content})

