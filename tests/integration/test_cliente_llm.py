from app.config import Configuracion
from app.llm.cliente import ClienteLLM
from app.llm.falso import ProveedorFalso
from app.llm.limitador import LimitadorDeTasa
from app.llm.proveedor import ErrorLimiteDeTasa


def test_cliente_reintenta_y_devuelve_la_respuesta(monkeypatch):
    monkeypatch.setattr("app.llm.reintento.time.sleep", lambda s: None)
    proveedor = ProveedorFalso([ErrorLimiteDeTasa(), "hola"])
    config = Configuracion("falso", 10, 3)
    cliente = ClienteLLM(proveedor, config, LimitadorDeTasa(10))
    assert cliente.generar("saluda") == "hola"
    assert proveedor.llamadas == 2
