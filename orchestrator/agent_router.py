class AgentRouter:

    def route(
        self,
        question: str
    ):

        question = question.lower()

        # DevOps Agent

        if any(
            keyword in question
            for keyword in [
                "pipeline",
                "deployment",
                "github",
                "repository",
                "repo",
                "issue",
                "issues",
                "pull request",
                "pull requests",
                "workflow",
                "workflows",
                "actions",
                "devops",
                "ci/cd",
                "build"
            ]
        ):
            return "devops"

        # CloudOps Agent

        if any(
            keyword in question
            for keyword in [
                "azure",
                "cloud",
                "monitoring",
                "cost",
                "cost optimization",
                "infrastructure",
                "app service",
                "aks",
                "kubernetes",
                "virtual machine",
                "vm"
            ]
        ):
            return "cloudops"

        # Documentation Agent
        # Used for generating documentation,
        # not for answering architecture questions.

        if any(
            keyword in question
            for keyword in [
                "document",
                "documentation",
                "runbook",
                "sop",
                "procedure",
                "guide",
                "generate document",
                "create document",
                "write documentation"
            ]
        ):
            return "documentation"

        # Default

        return "knowledge"
