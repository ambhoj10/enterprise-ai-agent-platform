from agents.planner_agent import (
    PlannerAgent
)

planner = PlannerAgent()

question = (
    "Explain the architecture and show related GitHub information"
)

plan = planner.create_plan(
    question
)

print(plan)
