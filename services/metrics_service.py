class MetricsService:

    def get_metrics(
        self,
        logs
    ):

        total_requests = len(
            logs
        )

        total_sessions = len(
            set(
                log["session_id"]

                for log in logs
            )
        )

        knowledge_agent_calls = 0
        devops_agent_calls = 0
        cloudops_agent_calls = 0

        response_lengths = []

        requests_per_user = {}

        requests_per_endpoint = {}

        cost_per_user = {}

        total_prompt_tokens = 0

        total_completion_tokens = 0

        total_tokens = 0

        total_cost = 0.0

        for log in logs:

            response_lengths.append(
                log["response_length"]
            )

            prompt_tokens = (
                log.get(
                    "prompt_tokens",
                    0
                )
            )

            completion_tokens = (
                log.get(
                    "completion_tokens",
                    0
                )
            )

            request_tokens = (
                log.get(
                    "total_tokens",
                    0
                )
            )

            request_cost = (
                log.get(
                    "estimated_cost",
                    0.0
                )
            )

            total_prompt_tokens += (
                prompt_tokens
            )

            total_completion_tokens += (
                completion_tokens
            )

            total_tokens += (
                request_tokens
            )

            total_cost += (
                request_cost
            )

            username = log.get(
                "username"
            )

            if username:

                requests_per_user[
                    username
                ] = (
                    requests_per_user.get(
                        username,
                        0
                    ) + 1
                )

                cost_per_user[
                    username
                ] = round(
                    cost_per_user.get(
                        username,
                        0.0
                    )
                    + request_cost,
                    6
                )

            endpoint = log.get(
                "endpoint"
            )

            if endpoint:

                requests_per_endpoint[
                    endpoint
                ] = (
                    requests_per_endpoint.get(
                        endpoint,
                        0
                    ) + 1
                )

            for agent in log["agents"]:

                if agent == "Knowledge Agent":

                    knowledge_agent_calls += 1

                elif agent == "DevOps Agent":

                    devops_agent_calls += 1

                elif agent == "CloudOps Agent":

                    cloudops_agent_calls += 1

        average_response_length = 0

        if response_lengths:

            average_response_length = (
                sum(response_lengths)
                / len(response_lengths)
            )

        average_cost_per_request = 0

        if total_requests:

            average_cost_per_request = (
                total_cost
                / total_requests
            )

        return {

            "total_requests":
                total_requests,

            "total_sessions":
                total_sessions,

            "knowledge_agent_calls":
                knowledge_agent_calls,

            "devops_agent_calls":
                devops_agent_calls,

            "cloudops_agent_calls":
                cloudops_agent_calls,

            "average_response_length":
                round(
                    average_response_length,
                    2
                ),

            "total_prompt_tokens":
                total_prompt_tokens,

            "total_completion_tokens":
                total_completion_tokens,

            "total_tokens":
                total_tokens,

            "total_cost":
                round(
                    total_cost,
                    6
                ),

            "average_cost_per_request":
                round(
                    average_cost_per_request,
                    6
                ),

            "requests_per_user":
                requests_per_user,

            "cost_per_user":
                cost_per_user,

            "requests_per_endpoint":
                requests_per_endpoint
        }
