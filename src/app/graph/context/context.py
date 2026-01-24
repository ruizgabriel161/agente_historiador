
from dataclasses import dataclass



@dataclass(kw_only=True, frozen=True,repr=True,slots=True)
class Context:
    """Classe de contexto."""
...