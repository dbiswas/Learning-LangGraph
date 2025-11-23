# ################################################
# Sample LangGraph application demonstrating a simple greeting state machine.
# Install the following:
# uv pip install -U langgraph
# uv pip install -U langchain-anthropic
# uv pip install ipython
# uv pip install pygraphviz
# uv pip install grandalf
# uv pip install matplotlib
# ################################################
# Suppress Pydantic deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_core._api.deprecation")

from typing import Dict, TypedDict
# Framework that helps you design and implement state machines
from langgraph.graph import StateGraph, END
from IPython.display import Image, display


class AgentState(TypedDict):
    """State dictionary to hold the agent's message."""
    message: str


def greeting_node(state: AgentState) -> AgentState:
    """A simple node that sets a greeting message in the agent's state."""
    state["message"] = "Hello! " + state["message"] + " How can I assist you today?"
    return state


# Building Graph here
graph = StateGraph(AgentState)

# Add the greeting node to the graph
graph.add_node("greeter", greeting_node)

# Set the entry point for the graph
graph.set_entry_point("greeter")

# Add edge from greeter node to END to mark completion
graph.add_edge("greeter", END)

# Compile the graph into a runnable application
app = graph.compile()

result = app.invoke({"message": "Welcome to LangGraph!"})

print(result)

