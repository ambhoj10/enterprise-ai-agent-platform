class CostService:

    def calculate_cost(
        self,
        prompt_tokens,
        completion_tokens
    ):

        prompt_cost = (
            prompt_tokens / 1_000_000
        ) * 0.15

        completion_cost = (
            completion_tokens / 1_000_000
        ) * 0.60

        total_cost = (
            prompt_cost
            + completion_cost
        )

        return round(
            total_cost,
            6
        )
