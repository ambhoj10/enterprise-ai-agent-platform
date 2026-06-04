from fastapi import APIRouter

from orchestrator.agent_router import AgentRouter

from agents.knowledge_agent import KnowledgeAgent
from agents.devops_agent import DevOpsAgent
from agents.cloudops_agent import CloudOpsAgent
from agents.documentation_agent import DocumentationAgent

from models.chat import ChatRequest

router = APIRouter()

agent_router = AgentRouter()

knowledge_agent = KnowledgeAgent()
devops_agent = DevOpsAgent()
cloudops_agent = CloudOpsAgent()
documentation_agent = DocumentationAgent()


@router.post("/agent/chat")
def chat(
    request: ChatRequest
):

    question = request.question

    selected_agent = agent_router.route(
        question
    )

    if selected_agent == "devops":
        return devops_agent.execute(
            question
        )

    if selected_agent == "cloudops":
        return cloudops_agent.execute(
            question
        )

    if selected_agent == "documentation":
        return documentation_agent.execute(
            question
        )

    return knowledge_agent.execute(
        question
    )
