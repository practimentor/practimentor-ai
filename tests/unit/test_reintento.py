import pytest

from app.llm.proveedor import ErrorLimiteDeTasa
from app.llm.reintento import reintentar_con_espera_exponencial


def test_devuelve_el_resultado_si_no_hay_error():
    assert reintentar_con_espera_exponencial(lambda: "ok", 3, dormir=lambda s: None) == "ok"


def test_reintenta_con_espera_exponencial_ante_limite_de_tasa():
    fallos = [ErrorLimiteDeTasa(), ErrorLimiteDeTasa()]
    esperas: list[float] = []

    def operacion():
        if fallos:
            raise fallos.pop()
        return "listo"

    assert reintentar_con_espera_exponencial(operacion, 4, 1.0, esperas.append) == "listo"
    assert esperas == [1.0, 2.0]


def test_propaga_el_error_al_agotar_los_reintentos():
    def operacion():
        raise ErrorLimiteDeTasa()

    with pytest.raises(ErrorLimiteDeTasa):
        reintentar_con_espera_exponencial(operacion, 2, dormir=lambda s: None)


def test_no_reintenta_otros_errores():
    llamadas = []

    def operacion():
        llamadas.append(1)
        raise ValueError("otro")

    with pytest.raises(ValueError):
        reintentar_con_espera_exponencial(operacion, 3, dormir=lambda s: None)
    assert len(llamadas) == 1
