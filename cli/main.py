import argparse
from services.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', choices=['register', 'assign', 'complete'])
    parser.add_argument('--agent-id')
    parser.add_argument('--task-id')
    parser.add_argument('--task-type')
    parser.add_argument('--result')
    parser.add_argument('--visualization')

    args = parser.parse_args()

    orchestrator = Orchestrator()

    if args.action == 'register':
        agent = maestro_framework.core.Agent(args.agent_id)
        orchestrator.register_agent(args.agent_id, agent)
    elif args.action == 'assign':
        task = maestro_framework.core.Task(args.task_id, args.task_type, args.result, args.visualization)
        orchestrator.assign_task(args.task_id, args.agent_id, task)
    elif args.action == 'complete':
        orchestrator.complete_task(args.task_id)
