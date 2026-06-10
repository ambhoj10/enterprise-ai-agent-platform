from agents.planner_agent import (
    PlannerAgent
)

from orchestrator.multi_agent_executor import (
    MultiAgentExecutor
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

print("\nPlan:")
print(plan)

print("\nResults:")

for result in results:

    print(
        result["agent"]
    )
