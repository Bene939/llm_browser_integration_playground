from langchain_ollama import ChatOllama
from browser_use import Agent
import asyncio
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def main():
    llm = ChatOllama(model="llama2")
    test_response = llm.invoke("What is 2 + 2?")
    print("Test Response from LLM:", test_response)
    
    agent = Agent(
        task="Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
