class AgentRouter:

    def route(
        self,
        question: str
    ):

        question = question.lower()

        # Documentation first
        if any(
            keyword in question
            for keyword in [
                "document",
                "documentation",
                "runbook",
                "architecture",
                "design",
                "sop",
                "procedure"
            ]
        ):
            return "documentation"

        # DevOps second
        if any(
            keyword in question
            for keyword in [
                "pipeline",
                "deployment",
                "github",
                "devops",
                "ci/cd",
                "build"
            ]
        ):
            return "devops"

        # CloudOps third
        if any(
            keyword in question
            for keyword in [
                "azure",
                "cloud",
                "monitoring",
                "cost",
                "infrastructure"
            ]
        ):
            return "cloudops"

        return "knowledge"
