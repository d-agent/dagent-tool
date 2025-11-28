from dagent_tool.core import run_api
from dagent_tool.models import Requirement

async def adk_tool(requirements: Requirement, text: str, is_new_session: bool = False):
    """
    DAgent Network Tool - Intelligent AI Agent Router
    
    Automatically discovers and routes requests to the most suitable AI agent from the 
    DAgent decentralized network. Uses semantic matching to find agents based on your 
    requirements, handles session persistence, and manages pay-per-use billing transparently.
    
    Instead of manually selecting from hundreds of AI agents, simply describe what you need 
    and DAgent will match you with the best-performing agent for your task.
    
    For the first request, if there is no agent_id in the cookies, then it will perform a semantic matching to find the best agent for the current scenario.
    If there is an agent_id in the cookies, then it will reuse the same agent for the current scenario.
    
    Args:
        requirements (Optional[dict]): Criteria for selecting the optimal AI agent.
            - description (str): Natural language description of what the agent should do.
              Example: "An agent specialized in code review for TypeScript and React projects"
            
            - preferred_llm_provider (Optional[str]): Preferred LLM backend.
              Options: "OpenAI", "Anthropic", "Google", "Llama", "Custom"
              Default: None (any provider)
            
            - max_agent_cost (Optional[float]): Maximum cost per request in credits.
              Default: None (no limit)
            
            - max_total_agent_cost (Optional[float]): Maximum total cost for the session.
              Default: None (no limit)
            
            - skills (Optional[List[str]]): Required agent capabilities.
              Example: ["code-review", "typescript", "security-analysis"]
              Default: None (inferred from description)
            
            - streaming (bool): Whether to stream responses.
              Default: False
            
            - is_multi_agent_system (bool): Allow multi-agent orchestration systems.
              Default: False
    
        text (str): The prompt or message to send to the matched AI agent.
        is_new_session (bool): Whether to start a new session If the context of current relavant agent completely changes and user want new agent to connect to enable this i.e, set it to True.

    Returns:
        dict: Agent response containing:
            - response (str): The AI agent's response content
            - agent_id (str): ID of the matched agent (for session continuity)
            - credit_balance (float): Remaining credits after the request
    
    Raises:
        AuthenticationError: Invalid or missing API key
        InsufficientCreditsError: Credit balance too low for request
        NoAgentFoundError: No suitable agent matches the requirements
        AgentUnavailableError: Matched agent is offline or unresponsive
    
    Example:
        >>> response = adk_tool(
        ...     requirements={
        ...         "description": "Code review assistant for Python",
        ...         "skills": ["python", "code-review", "best-practices"],
        ...         "max_agent_cost": 0.01
        ...     },
        ...     text="Review this function for potential bugs and improvements..."
        ... )
        >>> print(response["response"])
    
    Note:
        - First request performs semantic matching; subsequent requests reuse the matched agent
        - Session persists via agent_id cookie for consistent agent routing
        - Credits are deducted based on agent cost + token usage
        - is_new_session is used to start a new session if the context of current relavant agent completely changes and user want new agent to connect to enable this i.e, set it to True.

    """
    return await run_api(
        requirements,
        text,
        is_new_session,
    )
