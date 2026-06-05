from maestro_framework.core import Engine
from maestro_framework.core.types import Agent, Task

class Orchestrator:
    def __init__(self):
        self.engine = Engine()

    def register_agent(self, agent_id: str, agent: Agent) -> None:
        self.engine.register_agent(agent_id, agent)

    def assign_task(self, task_id: str, agent_id: str, task: Task) -> None:
        self.engine.assign_task(task_id, agent_id, task)

    def complete_task(self, task_id: str) -> None:
        self.engine.complete_task(task_id)