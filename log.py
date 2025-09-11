from agents import Agent, ModelSettings, RunConfig, Runner, function_tool, enable_verbose_stdout_logging
from play_ground.config import model_config
enable_verbose_stdout_logging()


                #    Tool Get the priority results in no joke

@function_tool
def fetch_weather(location: str) -> str:
    """Fetches the current weather for a given location."""
    # Dummy implementation for illustration purposes
    return f"The current weather in {location} is sunny with a temperature of 25°C."


agent: Agent = Agent(
    name="agent",
    instructions="You are a helpful assistant.\n You must answer all parts of the user's query. Use tools if necessary.",
    model=model_config,
    tools=[fetch_weather],
    tool_use_behavior="stop_on_first_tool",
)
result: Runner = Runner.run_sync(
    agent, "Tell me a short joke and also the weather in Karachi.", max_turns=3
)
print(result.final_output)
