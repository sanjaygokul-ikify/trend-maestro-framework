class MaestroException(Exception):
    pass

class AgentNotFoundException(MaestroException):
    def __init__(self, agent_id: str):
        super().__init__(f"Agent {agent_id} not found")

class TaskNotFoundException(MaestroException):
    def __init__(self, task_id: str):
        super().__init__(f"Task {task_id} not found")