import logging
from typing import List, Dict
from .types import Agent, Task, Dashboard
from .exceptions import MaestroException

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.tasks: Dict[str, Task] = {}
        self.dashboards: Dict[str, Dashboard] = {}

    def register_agent(self, agent_id: str, agent: 'Agent') -> None:
        logger.info(f"Registering agent {agent_id}")
        if agent_id in self.agents:
            raise MaestroException(f"Agent {agent_id} already registered")
        self.agents[agent_id] = agent

    def assign_task(self, task_id: str, agent_id: str, task: 'Task') -> None:
        logger.info(f"Assigning task {task_id} to agent {agent_id}")
        if agent_id not in self.agents:
            raise MaestroException(f"Agent {agent_id} not found")
        if task_id in self.tasks:
            raise MaestroException(f"Task {task_id} already assigned")
        self.tasks[task_id] = task
        self.agents[agent_id].tasks.append(task_id)

    def complete_task(self, task_id: str) -> None:
        logger.info(f"Completing task {task_id}")
        if task_id not in self.tasks:
            raise MaestroException(f"Task {task_id} not found")
        task = self.tasks[task_id]
        for agent_id, agent in self.agents.items():
            if task_id in agent.tasks:
                agent.tasks.remove(task_id)
        del self.tasks[task_id]

    def aggregate_task(self, task_id: str) -> str:
        logger.info(f"Aggregating task {task_id}")
        if task_id not in self.tasks:
            raise MaestroException(f"Task {task_id} not found")
        task = self.tasks[task_id]
        # Perform aggregation logic here
        return task.result

    def visualize_task(self, task_id: str) -> str:
        logger.info(f"Visualizing task {task_id}")
        if task_id not in self.tasks:
            raise MaestroException(f"Task {task_id} not found")
        task = self.tasks[task_id]
        # Perform visualization logic here
        return task.visualization

    def remove_agent(self, agent_id: str) -> None:
        logger.info(f"Removing agent {agent_id}")
        if agent_id not in self.agents:
            raise MaestroException(f"Agent {agent_id} not found")
        del self.agents[agent_id]