from agents import Agent, ModelSettings, RunConfig, Runner, function_tool, enable_verbose_stdout_logging
from play_ground.config import model_config
enable_verbose_stdout_logging()

@function_tool(is_enabled=False)
def get_system_time() -> str:
    """This tool retrieves the user's account status and plan details."""
    return "The current time is 4:23 PM."
agent :Agent = Agent(
    name = "Account Agent", 
    instructions = "You are an account manager. Your job is to fetch account status. Don't halucinate reply 100% truth if dont try to make up anything b your self",
    model = model_config,
    tools = [get_system_time],
    model_settings = ModelSettings(tool_choice = "required")
)

result = Runner.run_sync(
    agent, 
    "I need to know my account status. uid=09344", 
    run_config=RunConfig(
        model=model_config,
    )
)
print(result.final_output)