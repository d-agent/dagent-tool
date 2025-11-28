from .core import run_api
from .adapters.adk import adk_tool

# Lazy imports for adapters with optional dependencies
def __getattr__(name: str):
    if name == "langchain_tool":
        from .adapters.langchain import langchain_tool
        return langchain_tool
    if name == "crewai_tool":
        from .adapters.crewai import crewai_tool
        return crewai_tool
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "run_api",
    "adk_tool",
    "langchain_tool",
    "crewai_tool",
]

