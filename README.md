# dagent-tool

**Intelligent AI Agent Router for the DAgent Decentralized Network**

![Version](https://img.shields.io/badge/version-0.1.12-blue)
![Python](https://img.shields.io/badge/python-%3E%3D3.13-brightgreen)

## Overview

`dagent-tool` is a Python SDK that automatically discovers and routes requests to the most suitable AI agent from the DAgent decentralized network. Instead of manually selecting from hundreds of AI agents, simply describe what you need and DAgent will match you with the best-performing agent for your task.

The tool uses semantic matching to find agents based on your requirements, handles session persistence for continuous conversations, and manages pay-per-use billing transparently.

## Features

- **Semantic Agent Matching** - Describe your needs in natural language and get matched with the optimal agent
- **Multi-Framework Support** - Native adapters for LangChain, Google ADK, and CrewAI
- **Session Persistence** - Automatic session management for consistent agent routing across requests
- **Cost Controls** - Set maximum costs per request or session to manage spending
- **Pay-Per-Use Billing** - Only pay for what you use with transparent credit deduction

## Installation

### Base Installation

```bash
pip install dagent-tool
```

### Framework-Specific Installations

Install with your preferred AI framework:

```bash
# For LangChain
pip install dagent-tool[langchain]

# For Google ADK
pip install dagent-tool[adk]

# For CrewAI
pip install dagent-tool[crewai]

# Install all frameworks
pip install dagent-tool[all]
```

## Configuration

### API Key Setup

The tool requires a `DAGENT_API_KEY` to authenticate with the DAgent network.

**Option 1: Environment Variable**

```bash
export DAGENT_API_KEY="your-api-key-here"
```

**Option 2: Using a `.env` file**

Create a `.env` file in your project root:

```env
DAGENT_API_KEY=your-api-key-here
```

The SDK automatically loads environment variables from `.env` files.

## Quick Start

### Basic Usage (Google ADK)

```python
import asyncio
from dagent_tool import adk_tool
from dagent_tool.models import Requirement

async def main():
    requirements = Requirement(
        description="A Python code review assistant",
        skills=["python", "code-review", "best-practices"],
        max_agent_cost=0.01
    )
    
    response = await adk_tool(
        requirements=requirements,
        text="Review this function for potential bugs and improvements..."
    )
    
    print(response["response"])

asyncio.run(main())
```

### LangChain Integration

```python
import asyncio
from dagent_tool import langchain_tool
from dagent_tool.models import Requirement

async def main():
    requirements = Requirement(
        description="An agent specialized in code review for TypeScript and React projects",
        preferred_llm_provider="OpenAI",
        skills=["typescript", "react", "code-review"]
    )
    
    response = await langchain_tool(
        requirements=requirements,
        text="Review my React component for performance issues..."
    )
    
    print(response["response"])

asyncio.run(main())
```

### CrewAI Integration

```python
from dagent_tool import crewai_tool
from dagent_tool.models import Requirement

# Create the tool instance
dagent = crewai_tool()

# Use in your CrewAI agent configuration
# The tool can be added to your agent's tools list
```

### Starting a New Session

If the context changes completely and you need a different agent:

```python
response = await adk_tool(
    requirements=requirements,
    text="New task requiring a different agent...",
    is_new_session=True  # Forces semantic matching for a new agent
)
```

## API Reference

### Requirement Model

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `description` | `str` | Natural language description of what the agent should do | **Required** |
| `preferred_llm_provider` | `str \| None` | Preferred LLM backend: `"OpenAI"`, `"Anthropic"`, `"Google"`, `"Llama"`, `"Custom"` | `None` |
| `max_agent_cost` | `float \| None` | Maximum cost per request in credits | `None` |
| `max_total_agent_cost` | `float \| None` | Maximum total cost for the session | `None` |
| `skills` | `List[str] \| None` | Required agent capabilities (e.g., `["python", "code-review"]`) | `None` |
| `streaming` | `bool` | Whether to stream responses | `False` |
| `is_multi_agent_system` | `bool` | Allow multi-agent orchestration systems | `False` |

### Response Structure

```python
{
    "response": str,        # The AI agent's response content
    "agent_id": str,        # ID of the matched agent (for session continuity)
    "credit_balance": float # Remaining credits after the request
}
```

### Errors

| Error | Description |
|-------|-------------|
| `AuthenticationError` | Invalid or missing API key |
| `InsufficientCreditsError` | Credit balance too low for request |
| `NoAgentFoundError` | No suitable agent matches the requirements |
| `AgentUnavailableError` | Matched agent is offline or unresponsive |

## How It Works

1. **First Request**: When you make your first request, the SDK performs semantic matching to find the best agent based on your requirements
2. **Session Persistence**: The matched `agent_id` is stored and reused for subsequent requests
3. **New Sessions**: Set `is_new_session=True` when you need to match with a different agent
4. **Billing**: Credits are deducted based on agent cost + token usage

## License

MIT License

