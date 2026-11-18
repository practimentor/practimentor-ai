from app.config import Configuracion


def test_valores_por_defecto():
    c = Configuracion.desde_entorno({})
    assert c.proveedor_llm == "gemini"
    assert c.limite_por_minuto == 10
    assert c.reintentos_maximos == 4


def test_lee_variables_de_entorno():
    c = Configuracion.desde_entorno(
        {"LLM_PROVIDER": "otro", "LLM_RATE_LIMIT_PER_MINUTE": "3", "LLM_MAX_RETRIES": "1"}
    )
    assert (c.proveedor_llm, c.limite_por_minuto, c.reintentos_maximos) == ("otro", 3, 1)
