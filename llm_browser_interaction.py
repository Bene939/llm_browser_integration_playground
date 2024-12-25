from langchain_groq import ChatGroq
from browser_use import Agent
import asyncio
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def main():
    llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
    agent = Agent(
        task="Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())