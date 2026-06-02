import unittest
from maestro_framework.core import Agent, Task, Engine

class TestCore(unittest.TestCase):
    def test_register_agent(self):
        engine = Engine()
        agent = Agent('agent1')
        engine.register_agent('agent1', agent)
        self.assertIn('agent1', engine.agents)

    def test_assign_task(self):
        engine = Engine()
        agent = Agent('agent1')
        engine.register_agent('agent1', agent)
        task = Task('task1', 'type1', 'result1', 'visualization1')
        engine.assign_task('task1', 'agent1', task)
        self.assertIn('task1', engine.tasks)
        self.assertIn('task1', engine.agents['agent1'].tasks)

    def test_complete_task(self):
        engine = Engine()
        agent = Agent('agent1')
        engine.register_agent('agent1', agent)
        task = Task('task1', 'type1', 'result1', 'visualization1')
        engine.assign_task('task1', 'agent1', task)
        engine.complete_task('task1')
        self.assertNotIn('task1', engine.tasks)
        self.assertNotIn('task1', engine.agents['agent1'].tasks)