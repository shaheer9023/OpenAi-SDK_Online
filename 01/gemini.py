from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import os
import asyncio

# Setting environment variable
key = os.environ["GEMINI_API_KEY"] = "my gemini key"
set_tracing_disabled(True)

# Creating AsyncOpenAI client
client = AsyncOpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Creating OpenAI model
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-pro-exp-03-25",
    openai_client=client,
)

# Main async function
async def main():
    # Creating Agent
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful AI Assistant",
        model=model,
    )

    # Infinite prompt loop
    while True:
        prompt = input("Enter prompt: ")
        if prompt.lower() == "exit":
            print("Good Bye!")
            break

        response = await Runner.run(agent, prompt)
        print("Assistant:", response.final_output)

# Run the main function
asyncio.run(main())
