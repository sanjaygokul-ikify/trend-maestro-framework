from maestro_framework.core import Engine
from maestro_framework.core.types import Agent, Task

class Orchestrator:
    def __init__(self):
        self.engine = Engine()

    def register_agent(self, agent_id: str, agent: 'Agent') -> None:
        try:
            self.engine.register_agent(agent_id, agent)
        except Exception as e:
            print(f"Error registering agent {agent_id}: {e}")

    def assign_task(self, task_id: str, agent_id: str, task: 'Task') -> None:
        try:
            self.engine.assign_task(task_id, agent_id, task)
        except Exception as e:
            print(f"Error assigning task {task_id} to agent {agent_id}: {e}")

    def complete_task(self, task_id: str) -> None:
        try:
            self.engine.complete_task(task_id)
        except Exception as e:
            print(f"Error completing task {task_id}: {e}")

    def remove_agent(self, agent_id: str) -> None:
        try:
            self.engine.remove_agent(agent_id)
        except Exception as e:
            print(f"Error removing agent {agent_id}: {e}")