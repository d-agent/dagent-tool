from pydantic import BaseModel
from typing import Optional, List, Dict


class Requirement(BaseModel):
    description: str
    preferred_llm_provider: Optional[str] = None
    max_agent_cost: Optional[float] = None
    max_total_agent_cost: Optional[float] = None
    skills: Optional[List[str]] = None
    streaming: bool = False
    is_multi_agent_system: bool = False


class ToolInput(BaseModel):
    requirement: Requirement
    text: str
    api_key: Optional[str] = None
    cookies: Optional[Dict] = None

