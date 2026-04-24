# Test script for DirectPromptAgent class

from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

# Instantiate the DirectPromptAgent
direct_agent = DirectPromptAgent(openai_api_key)

# Send the prompt and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

# The DirectPromptAgent uses the general knowledge built into the GPT-3.5-turbo model.
# It does not rely on any external documents, databases, or retrieval systems.
# The answer comes purely from the LLM's pre-trained internal knowledge acquired during training.
print(
    "\nKnowledge source: This response was generated using the GPT-3.5-turbo model's "
    "built-in general knowledge from its training data. No external documents, "
    "retrieval systems, or additional context were provided to the agent."
)
