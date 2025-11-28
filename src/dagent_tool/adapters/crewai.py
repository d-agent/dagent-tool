from dagent_tool.core import run_api
from dagent_tool.models import Requirement

try:
    from crewai.tools import BaseTool
except ImportError:
    raise ImportError(
        "crewai is required for this adapter. "
        "Install it with: pip install dagent-tool[crewai]"
    )


class CrewAIDAgentTool(BaseTool):
    name: str = "dagent_network_tool"
    description: str = """DAgent Network Tool - Intelligent AI Agent Router.
    Automatically discovers and routes requests to the most suitable AI agent 
    from the DAgent decentralized network."""

    async def _run(self, requirements: Requirement, text: str, is_new_session: bool = False):
        return await run_api(requirements, text, is_new_session)


def crewai_tool():
    return CrewAIDAgentTool()

