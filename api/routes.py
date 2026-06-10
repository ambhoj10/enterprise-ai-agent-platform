from fastapi import (
    APIRouter,
    Header,
    HTTPException
)

from services.cost_service import (
    CostService
)

from orchestrator.agent_router import AgentRouter

from orchestrator.multi_agent_executor import (
    MultiAgentExecutor
)

from agents.planner_agent import (
    PlannerAgent
)

from services.response_synthesizer import (
    ResponseSynthesizer
)

from services.memory_service import (
    MemoryService
)

from services.execution_logger import (
    ExecutionLogger
)

from services.metrics_service import (
    MetricsService
)

from security.auth_service import (
    AuthService
)

from agents.knowledge_agent import KnowledgeAgent
from agents.devops_agent import DevOpsAgent
from agents.cloudops_agent import CloudOpsAgent
from agents.documentation_agent import DocumentationAgent

from models.chat import ChatRequest
from models.auth import LoginRequest

router = APIRouter()

# --------------------------------------------------
# Components
# --------------------------------------------------

agent_router = AgentRouter()

knowledge_agent = KnowledgeAgent()
devops_agent = DevOpsAgent()
cloudops_agent = CloudOpsAgent()
documentation_agent = DocumentationAgent()

planner_agent = PlannerAgent()

multi_agent_executor = (
    MultiAgentExecutor()
)

response_synthesizer = (
    ResponseSynthesizer()
)

memory_service = (
    MemoryService()
)

execution_logger = (
    ExecutionLogger()
)

metrics_service = (
    MetricsService()
)

auth_service = (
    AuthService()
)

cost_service = (
    CostService()
)

# --------------------------------------------------
# Helpers
# --------------------------------------------------

def extract_token(
    authorization: str
):

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Missing token"
        )

    if not authorization.startswith(
        "Bearer "
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid token format"
        )

    return authorization.replace(
        "Bearer ",
        ""
    )


def validate_authenticated_user(
    authorization: str
):

    token = extract_token(
        authorization
    )

    payload = (
        auth_service.verify_token(
            token
        )
    )

    return payload

# --------------------------------------------------
# Authentication
# --------------------------------------------------

@router.post("/auth/login")
def login(
    request: LoginRequest
):

    demo_users = {

        "admin": {
            "password": "admin123",
            "role": "admin"
        },

        "developer": {
            "password": "developer123",
            "role": "developer"
        },

        "viewer": {
            "password": "viewer123",
            "role": "viewer"
        }
    }

    user = demo_users.get(
        request.username
    )

    if (
        not user
        or
        user["password"]
        != request.password
    ):

        return {
            "error":
            "Invalid credentials"
        }

    token = (
        auth_service
        .create_access_token(
            request.username,
            user["role"]
        )
    )

    return {

        "access_token":
            token,

        "token_type":
            "bearer",

        "role":
            user["role"]
    }

# --------------------------------------------------
# Single-Agent Endpoint
# --------------------------------------------------

@router.post("/agent/chat")
def chat(
    request: ChatRequest,
    authorization: str | None = Header(
        default=None,
        alias="Authorization"
    )
):

    validate_authenticated_user(
        authorization
    )

    question = request.question

    selected_agent = (
        agent_router.route(
            question
        )
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

# --------------------------------------------------
# Multi-Agent Endpoint
# --------------------------------------------------
@router.post("/orchestrator/chat")
def orchestrator_chat(
    request: ChatRequest,
    authorization: str | None = Header(
        default=None,
        alias="Authorization"
    )
):

    user_payload = (
        validate_authenticated_user(
            authorization
        )
    )

    username = (
        user_payload.get(
            "sub"
        )
    )

    question = request.question

    session_id = request.session_id

    history = (
        memory_service.get_history(
            session_id
        )
    )

    conversation_context = "\n".join(

        (
            f"{message['role']}: "
            f"{message['content']}"
        )

        for message in history[-6:]
    )

    memory_service.add_message(
        session_id,
        "user",
        question
    )

    plan = (
        planner_agent.create_plan(
            question
        )
    )

    agent_results = (
        multi_agent_executor.execute(
            question,
            plan,
            conversation_context
        )
    )

    final_response = (
        response_synthesizer.synthesize(
            question,
            agent_results
        )
    )

    response_text = (
        final_response["response"]
    )

    prompt_tokens = (
        final_response["prompt_tokens"]
    )

    completion_tokens = (
        final_response["completion_tokens"]
    )

    total_tokens = (
        final_response["total_tokens"]
    )

    estimated_cost = (
        cost_service.calculate_cost(
            prompt_tokens,
            completion_tokens
        )
    )

    memory_service.add_message(
        session_id,
        "assistant",
        response_text
    )

    execution_logger.log_execution(
        session_id=session_id,
        question=question,
        plan=plan,
        history_count=len(
            memory_service.get_history(
                session_id
            )
        ),
        agent_results=agent_results,
        response=response_text,
        username=username,
        endpoint="/orchestrator/chat",
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        total_tokens=total_tokens,
        estimated_cost=estimated_cost
    )

    return {

        "session_id":
            session_id,

        "plan":
            plan,

        "history_count":
            len(
                memory_service.get_history(
                    session_id
                )
            ),

        "response":
            response_text,

        "prompt_tokens":
            prompt_tokens,

        "completion_tokens":
            completion_tokens,

        "total_tokens":
            total_tokens,

        "estimated_cost":
            estimated_cost
    }
# --------------------------------------------------
# Logs (Admin Only)
# --------------------------------------------------

@router.get("/orchestrator/logs")
def get_execution_logs(
    authorization: str | None = Header(
        default=None,
        alias="Authorization"
    )
):

    token = extract_token(
        authorization
    )

    auth_service.authorize(
        token,
        [
            "admin"
        ]
    )

    return (
        execution_logger
        .get_logs()
    )

# --------------------------------------------------
# Metrics (Admin + Developer)
# --------------------------------------------------

@router.get("/orchestrator/metrics")
def get_metrics(
    authorization: str | None = Header(
        default=None,
        alias="Authorization"
    )
):

    token = extract_token(
        authorization
    )

    auth_service.authorize(
        token,
        [
            "admin",
            "developer"
        ]
    )

    logs = (
        execution_logger
        .get_logs()
    )

    return (
        metrics_service.get_metrics(
            logs
        )
    )
