import time
from collections import deque
from collections.abc import Callable


class LimitadorDeTasa:
    def __init__(
        self,
        limite_por_minuto: int,
        reloj: Callable[[], float] = time.monotonic,
        dormir: Callable[[float], None] = time.sleep,
    ) -> None:
        if limite_por_minuto < 1:
            raise ValueError("El límite por minuto debe ser al menos 1")
        self._limite = limite_por_minuto
        self._reloj = reloj
        self._dormir = dormir
        self._marcas: deque[float] = deque()

    def esperar_turno(self) -> None:
        ahora = self._reloj()
        while self._marcas and ahora - self._marcas[0] >= 60:
            self._marcas.popleft()
        if len(self._marcas) >= self._limite:
            espera = 60 - (ahora - self._marcas[0])
            self._dormir(espera)
            ahora = self._reloj()
            while self._marcas and ahora - self._marcas[0] >= 60:
                self._marcas.popleft()
        self._marcas.append(self._reloj())
