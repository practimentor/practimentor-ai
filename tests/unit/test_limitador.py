import pytest

from app.llm.limitador import LimitadorDeTasa


class Reloj:
    def __init__(self):
        self.t = 0.0
        self.esperas: list[float] = []

    def ahora(self):
        return self.t

    def dormir(self, segundos):
        self.esperas.append(segundos)
        self.t += segundos


def test_no_espera_dentro_del_limite():
    reloj = Reloj()
    limitador = LimitadorDeTasa(2, reloj.ahora, reloj.dormir)
    limitador.esperar_turno()
    limitador.esperar_turno()
    assert reloj.esperas == []


def test_espera_hasta_liberar_la_ventana_al_superar_el_limite():
    reloj = Reloj()
    limitador = LimitadorDeTasa(2, reloj.ahora, reloj.dormir)
    limitador.esperar_turno()
    reloj.t = 10
    limitador.esperar_turno()
    limitador.esperar_turno()
    assert reloj.esperas == [50]


def test_rechaza_un_limite_invalido():
    with pytest.raises(ValueError):
        LimitadorDeTasa(0)
