# Test script for AugmentedPromptAgent class

from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# Instantiate an AugmentedPromptAgent with the defined persona
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)

# Send the prompt to the agent and store the response
augmented_agent_response = augmented_agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

# Knowledge source: The AugmentedPromptAgent uses the LLM's (GPT-3.5-turbo) pre-trained general
# knowledge. It does not retrieve information from any external source or database — all factual
# content comes from the model's training data, just like the DirectPromptAgent.
#
# Effect of persona on the response: By injecting a system prompt that instructs the model to
# act as a college professor, the response is shaped in tone, structure, and style. The agent
# will begin its answer with "Dear students," and frame the answer in an academic, educational
# manner. The underlying fact (Paris is the capital of France) stays the same, but the delivery
# is filtered through the persona — demonstrating how a system prompt acts as a behavioral lens
# on top of the model's base knowledge without changing what the model fundamentally knows.
