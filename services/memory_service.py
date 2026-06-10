import sqlite3
from pathlib import Path


class MemoryService:

    def __init__(self):

        Path("data").mkdir(
            exist_ok=True
        )

        self.db_path = (
            "data/memory.db"
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
            CREATE TABLE IF NOT EXISTS conversation_history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                session_id TEXT NOT NULL,

                role TEXT NOT NULL,

                content TEXT NOT NULL,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()

        connection.close()

    def add_message(
        self,
        session_id,
        role,
        content
    ):

        connection = sqlite3.connect(
            self.db_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO conversation_history
            (
                session_id,
                role,
                content
            )
            VALUES
            (?, ?, ?)
            """,
            (
                session_id,
                role,
                content
            )
        )

        connection.commit()

        connection.close()

    def get_history(
        self,
        session_id
    ):

        connection = sqlite3.connect(
            self.db_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                role,
                content
            FROM
                conversation_history
            WHERE
                session_id = ?
            ORDER BY
                id ASC
            """,
            (
                session_id,
            )
        )

        rows = cursor.fetchall()

        connection.close()

        return [
            {
                "role": row[0],
                "content": row[1]
            }
            for row in rows
        ]

    def clear_session(
        self,
        session_id
    ):

        connection = sqlite3.connect(
            self.db_path
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM
                conversation_history
            WHERE
                session_id = ?
            """,
            (
                session_id,
            )
        )

        connection.commit()

        connection.close()
