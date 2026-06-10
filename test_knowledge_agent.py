from agents.knowledge_agent import (
    KnowledgeAgent
)

agent = KnowledgeAgent()

result = agent.execute(
    "How does the multi-agent architecture work?"
)

print(result["response"])
