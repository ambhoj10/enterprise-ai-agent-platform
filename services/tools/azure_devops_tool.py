from services.azure_devops_service import AzureDevOpsService


class AzureDevOpsTool:

    def __init__(self):

        self.azure_devops_service = (
            AzureDevOpsService()
        )

    def get_best_practices(self):

        return [
            "Use YAML pipelines",
            "Enable branch policies",
            "Implement CI/CD validation",
            "Use infrastructure as code",
            "Automate deployments",
            "Monitor build failures",
            "Review pipeline health regularly"
        ]

    def get_pipeline_summary(self):

        pipelines = (
            self.azure_devops_service.get_pipelines()
        )

        if pipelines["count"] == 0:
            return "No pipelines found."

        return "\n".join(
            pipeline["name"]
            for pipeline in pipelines["value"][:5]
        )

    def get_build_summary(self):

        builds = (
            self.azure_devops_service.get_builds()
        )

        if builds["count"] == 0:
            return "No builds found."

        return "\n".join(
            (
                f"{build['buildNumber']} - "
                f"{build['status']} - "
                f"{build.get('result')}"
            )
            for build in builds["value"][:5]
        )
