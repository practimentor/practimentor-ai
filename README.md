# PractiMentor — Servicio de IA

Procesamiento de currículos en PDF, extracción de texto, recomendaciones y consulta sobre un corpus curado. Python con FastAPI. El modelo de lenguaje se usa siempre detrás de la interfaz propia `ProveedorLLM`, de modo que el proveedor sea configurable.

Parte del proyecto **PractiMentor**, plataforma web de empleabilidad con inteligencia artificial para estudiantes universitarios (curso Herramientas de Desarrollo, UTP). Documentación y decisiones: [`practimentor-platform`](https://github.com/practimentor/practimentor-platform).

## Qué no le corresponde

No decide permisos: recibe solicitudes ya autorizadas por `practimentor-api-core`. No cambia el perfil del usuario sin una acción confirmada.

## Cómo ejecutarlo

```bash
uv sync
uv run pytest
uv run uvicorn app.main:app --reload    # GET /health
```

## Cómo contribuir

Lee [`CONTRIBUTING.md`](CONTRIBUTING.md).
