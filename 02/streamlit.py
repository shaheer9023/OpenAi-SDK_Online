import streamlit as st
from Chatbot import UrduBot
import asyncio
st.title("AI Urdu ChatBot")
user_input=st.text_input("Enter Your Prompt Here ")
if st.button("Enter"):
    response=asyncio.run(UrduBot(user_input))
    st.write(response)
