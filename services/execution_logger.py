import json
import sqlite3

from pathlib import Path
from datetime import datetime


class ExecutionLogger:

    def __init__(self):

        Path("data").mkdir(
            exist_ok=True
        )

        self.db_path = (
            "data/execution_logs.db"
        )

        self._initialize_database()

    def _initialize_database(
        self
    ):

        connection = sqlite3.connect(
            self.db_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS execution_logs (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT NOT NULL,

                session_id TEXT,

                username TEXT,

                endpoint TEXT,

                question TEXT,

                plan TEXT,

                history_count INTEGER,

                agents TEXT,

                response_length INTEGER,

                prompt_tokens INTEGER,

                completion_tokens INTEGER,

                total_tokens INTEGER,

                estimated_cost REAL
            )
            """
        )

        connection.commit()

        connection.close()

    def log_execution(
        self,
        session_id,
        question,
        plan,
        history_count,
        agent_results,
        response,
        username=None,
        endpoint=None,
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        estimated_cost=0.0
    ):

        connection = sqlite3.connect(
            self.db_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO execution_logs
            (
                timestamp,
                session_id,
                username,
                endpoint,
                question,
                plan,
                history_count,
                agents,
                response_length,
                prompt_tokens,
                completion_tokens,
                total_tokens,
                estimated_cost
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.utcnow().isoformat(),
                session_id,
                username,
                endpoint,
                question,
                json.dumps(plan),
                history_count,
                json.dumps(
                    [
                        result["agent"]
                        for result in agent_results
                    ]
                ),
                len(response),
                prompt_tokens,
                completion_tokens,
                total_tokens,
                estimated_cost
            )
        )

        connection.commit()

        connection.close()

    def get_logs(
        self
    ):

        connection = sqlite3.connect(
            self.db_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                timestamp,
                session_id,
                username,
                endpoint,
                question,
                plan,
                history_count,
                agents,
                response_length,
                prompt_tokens,
                completion_tokens,
                total_tokens,
                estimated_cost
            FROM
                execution_logs
            ORDER BY
                id DESC
            """
        )

        rows = cursor.fetchall()

        connection.close()

        return [
            {
                "timestamp": row[0],
                "session_id": row[1],
                "username": row[2],
                "endpoint": row[3],
                "question": row[4],
                "plan": json.loads(
                    row[5]
                ),
                "history_count": row[6],
                "agents": json.loads(
                    row[7]
                ),
                "response_length": row[8],
                "prompt_tokens": row[9],
                "completion_tokens": row[10],
                "total_tokens": row[11],
                "estimated_cost": row[12]
            }
            for row in rows
        ]
