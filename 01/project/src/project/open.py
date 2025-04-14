from agents import Agent, Runner
import os
import asyncio

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"]="MY OPENAI KEY"

async def main():
    agent = Agent(name="Ai Assistant", instructions="You have to give answers in only roman urdu")

    while True:
        prompt = input("Enter prompt: ")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        response = await Runner.run(agent, prompt)
        print("Assistant:", response.final_output)

# Run the async function using asyncio
asyncio.run(main())