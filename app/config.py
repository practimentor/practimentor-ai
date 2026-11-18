import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Configuracion:
    proveedor_llm: str
    limite_por_minuto: int
    reintentos_maximos: int

    @classmethod
    def desde_entorno(cls, entorno: dict[str, str] | None = None) -> "Configuracion":
        origen = os.environ if entorno is None else entorno
        return cls(
            proveedor_llm=origen.get("LLM_PROVIDER", "gemini"),
            limite_por_minuto=int(origen.get("LLM_RATE_LIMIT_PER_MINUTE", "10")),
            reintentos_maximos=int(origen.get("LLM_MAX_RETRIES", "4")),
        )
