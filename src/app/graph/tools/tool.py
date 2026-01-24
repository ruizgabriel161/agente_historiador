from langchain_core.tools import tool

from app.graph.context.context import Context
from langchain.tools import ToolRuntime


@tool()
async def query(runtime: ToolRuntime[Context]):
    """
    query Tool para executar o sql criado pela LLM

    Args:
        payload (Dict[str, Any]): payload json 
        runtime (Context): Context da aplicação.

    Raises:args
        ValueError: _description_

    Returns:
        list[str] | str: resultado da query.
    """
...