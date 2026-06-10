from agents.planner_agent import (
    PlannerAgent
)

planner = PlannerAgent()

questions = [

    "How does the architecture work?",

    "Show GitHub pull requests",

    "Show Azure cost optimization recommendations",

    "Explain architecture and show GitHub information",

    "Explain architecture and provide Azure recommendations"
]

for question in questions:

    print(
        "\nQuestion:",
        question
    )

    print(
        "Plan:",
        planner.create_plan(
            question
        )
    )
