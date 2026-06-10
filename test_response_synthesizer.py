from agents.planner_agent import (
    PlannerAgent
)

from orchestrator.multi_agent_executor import (
    MultiAgentExecutor
)

from services.response_synthesizer import (
    ResponseSynthesizer
)


question = (
    "Show GitHub pull requests"
)

planner = PlannerAgent()

plan = planner.create_plan(
    question
)

executor = (
    MultiAgentExecutor()
)

results = executor.execute(
    question,
    plan
)

print("\nExecution Plan:")
print(plan)

print("\nAgent Results:")
for result in results:

    print(
        result["agent"]
    )

synthesizer = (
    ResponseSynthesizer()
)

final_response = (
    synthesizer.synthesize(
        question,
        results
    )
)

print("\nFinal Response:\n")
print(final_response)
