# Test script for RoutingAgent class

from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a college professor"

# Define the Texas Knowledge Augmented Prompt Agent
knowledge = "You know everything about Texas"
texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Define the Europe Knowledge Augmented Prompt Agent
knowledge = "You know everything about Europe"
europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Define the Math Knowledge Augmented Prompt Agent
persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Instantiate the RoutingAgent
routing_agent = RoutingAgent(openai_api_key, {})

# Define the agents list with descriptions and callable functions
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x)
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x)
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_agent.respond(x)
    }
]

# Assign the agents to the routing agent
routing_agent.agents = agents

# Test routing with three different prompts and print results
print("=== Prompt 1: Tell me about the history of Rome, Texas ===")
print(routing_agent.route("Tell me about the history of Rome, Texas"))

print("\n=== Prompt 2: Tell me about the history of Rome, Italy ===")
print(routing_agent.route("Tell me about the history of Rome, Italy"))

print("\n=== Prompt 3: One story takes 2 days, and there are 20 stories ===")
print(routing_agent.route("One story takes 2 days, and there are 20 stories"))
