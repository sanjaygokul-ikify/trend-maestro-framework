import unittest
from maestro_framework.core import Agent, Task, Engine
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        orchestrator = Orchestrator()
        agent = Agent('agent1')
        task = Task('task1', 'type1', 'result1', 'visualization1')
        orchestrator.register_agent('agent1', agent)
        orchestrator.assign_task('task1', 'agent1', task)
        orchestrator.complete_task('task1')
        self.assertNotIn('task1', orchestrator.engine.tasks)
        self.assertNotIn('task1', orchestrator.engine.agents['agent1'].tasks)