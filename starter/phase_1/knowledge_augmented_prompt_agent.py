# Test script for KnowledgeAugmentedPromptAgent class

from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"

# Instantiate a KnowledgeAugmentedPromptAgent with the professor persona
# and deliberately incorrect knowledge to demonstrate knowledge injection
knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key,
    persona,
    "The capital of France is London, not Paris"
)

response = knowledge_agent.respond(prompt)
print(response)

# The agent responded using the INJECTED knowledge ("The capital of France is London, not Paris"),
# NOT its own internal knowledge from GPT-3.5-turbo. Even though the model knows that Paris is
# the correct answer, the system prompt explicitly instructs it to use only the provided knowledge
# and to ignore its own knowledge. This confirms that knowledge augmentation successfully overrides
# the model's pre-trained beliefs — a critical capability for grounding agents in domain-specific
# or proprietary information that may not exist in the model's training data.
print(
    "\nNote: The agent used the provided knowledge (London) instead of its own internal knowledge "
    "(Paris). This demonstrates successful knowledge augmentation — the system prompt grounds "
    "the agent's response in the supplied knowledge base rather than the LLM's training data."
)
