from agents import Agent, Runner,enable_verbose_stdout_logging
from play_ground.config import model_config
enable_verbose_stdout_logging()
agent: Agent = Agent(name=1,instructions="You are a helpful assistant.",model=model_config)
result: Runner = Runner.run_sync(agent, "reply in short")
print(result.final_output)
