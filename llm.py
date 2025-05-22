import os
from dotenv import load_dotenv
# from openai import AzureOpenAI
from crewai import LLM

llm = LLM(
    model=os.getenv('AZURE_API_MODEL'),
    api_version=os.getenv('AZURE_API_VERSION'),
    temperature=0.7
)

__all__ = ["llm"]