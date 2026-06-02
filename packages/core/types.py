from typing import List, Dict

class Agent:
    def __init__(self, agent_id: str):
        self.agent_id: str = agent_id
        self.tasks: List[str] = []

class Task:
    def __init__(self, task_id: str, task_type: str, result: str, visualization: str):
        self.task_id: str = task_id
        self.task_type: str = task_type
        self.result: str = result
        self.visualization: str = visualization

class Dashboard:
    def __init__(self, dashboard_id: str):
        self.dashboard_id: str = dashboard_id
        self.tasks: List[str] = []