import os
from dotenv import load_dotenv
from crewai import LLM
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = LLM(
    model="mistral/mistral-large-latest",
    temperature=0.7,
    api_key=os.getenv("MISTRAL_API_KEY"),
)


__all__ = ["llm"]