from maestro_framework.core import Engine

class Orchestrator:
    def __init__(self):
        self.engine = Engine()

    def register_agent(self, agent_id: str, agent):
        self.engine.register_agent(agent_id, agent)

    def assign_task(self, task_id: str, agent_id: str, task):
        self.engine.assign_task(task_id, agent_id, task)

    def complete_task(self, task_id: str):
        self.engine.complete_task(task_id)