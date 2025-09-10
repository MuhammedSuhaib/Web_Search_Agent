from agents import Agent, Runner
from play_ground.config import model_config
agent: Agent = Agent(name='agent',instructions="You are a helpful assistant.",model=model_config,)
result: Runner = Runner.run_sync(agent, "reply in short",max_turns=1)
print(result.final_output)
