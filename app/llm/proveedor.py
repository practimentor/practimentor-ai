from typing import Protocol


class ErrorLimiteDeTasa(Exception):
    pass


class ProveedorLLM(Protocol):
    def generar(self, prompt: str) -> str: ...
