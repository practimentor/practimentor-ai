import time
from collections.abc import Callable

from app.llm.proveedor import ErrorLimiteDeTasa


def reintentar_con_espera_exponencial[T](
    operacion: Callable[[], T],
    reintentos_maximos: int,
    espera_inicial: float = 1.0,
    dormir: Callable[[float], None] = time.sleep,
) -> T:
    espera = espera_inicial
    for intento in range(reintentos_maximos + 1):
        try:
            return operacion()
        except ErrorLimiteDeTasa:
            if intento == reintentos_maximos:
                raise
            dormir(espera)
            espera *= 2
    raise AssertionError("inalcanzable")
