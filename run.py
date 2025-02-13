import os

from dotenv import load_dotenv
load_dotenv()

print("Initializing tools...")
from tools import create_rag_response, analyze_rag_response, web_search

print("Initializing agent...")
from agent import initialize_agent_llm, construct_agent

print("Starting app...")
os.system("python app.py")
