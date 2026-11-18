class ProveedorFalso:
    def __init__(self, respuestas: list[object]) -> None:
        self._respuestas = list(respuestas)
        self.llamadas = 0

    def generar(self, prompt: str) -> str:
        self.llamadas += 1
        respuesta = self._respuestas.pop(0)
        if isinstance(respuesta, Exception):
            raise respuesta
        return str(respuesta)
