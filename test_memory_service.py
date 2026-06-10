from services.memory_service import (
    MemoryService
)

memory = MemoryService()

memory.add_message(
    "session-1",
    "user",
    "What agents exist?"
)

memory.add_message(
    "session-1",
    "assistant",
    "Knowledge Agent, DevOps Agent..."
)

history = memory.get_history(
    "session-1"
)

print(history)
