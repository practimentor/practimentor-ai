from app.config import Configuracion
from app.llm.limitador import LimitadorDeTasa
from app.llm.proveedor import ProveedorLLM
from app.llm.reintento import reintentar_con_espera_exponencial


class ClienteLLM:
    def __init__(self, proveedor: ProveedorLLM, configuracion: Configuracion, limitador: LimitadorDeTasa | None = None) -> None:
        self._proveedor = proveedor
        self._configuracion = configuracion
        self._limitador = limitador or LimitadorDeTasa(configuracion.limite_por_minuto)

    def generar(self, prompt: str) -> str:
        def llamar() -> str:
            self._limitador.esperar_turno()
            return self._proveedor.generar(prompt)

        return reintentar_con_espera_exponencial(llamar, self._configuracion.reintentos_maximos)
