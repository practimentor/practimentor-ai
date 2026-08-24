# AGENTS.md — utp-agent-api-rag

Servicio de agente del proyecto **utp-agent**. Python con FastAPI.
Responsable: **Nicolás**.

## Si alguien se presenta por primera vez

Cuando el usuario diga algo como "hola, soy Nicolás":

1. Lee `docs/onboarding.md` del repo `utp-agent-platform` y ubica su sección.
2. Verifica qué le falta instalar ejecutando: `python --version`, `uv --version`,
   `git --version`.
3. Guíalo instalando **una herramienta a la vez**, esperando que confirme antes
   de seguir. No le des todos los comandos de golpe.
4. Cuando el entorno esté listo, pídele el número de issue asignado y trabaja
   solo dentro de lo que ese issue autoriza.
5. Si algo no está en el issue, detente y dile que comente en el issue.

## Git lo ejecuta la persona, no tú

No ejecutes `git add`, `commit`, `push`, `pull`, `merge`, `rebase`, `reset` ni
`checkout` por tu cuenta. Puedes leer con `status`, `log`, `diff` y `show`.

Cuando haga falta una operación de escritura, **no digas "haz commit"**. Escribe
el comando exacto y completo, listo para copiar, con el mensaje de commit ya
redactado, y explica en una línea qué hace:

```bash
git add app/tools/buscar_materiales.py
git commit -m "feat(rag): agregar herramienta de busqueda en materiales"
git push
```

Solo ejecútalos tú si la persona te lo pide explícitamente.

## Comandos

El proyecto todavía no está creado — se hace en el Sprint 1.

```bash
uv sync                              # instalar dependencias
uv run uvicorn app.main:app --reload # levantar la API en http://localhost:8000
uv run pytest                        # pruebas
uv run ruff check .                  # lint
```

## Qué hace este servicio

Es el **agente**. Recibe una pregunta ya autorizada, decide por sí mismo qué
herramientas usar para buscar evidencia en los documentos del curso, y redacta
una respuesta **citando documento y página**.

No es un RAG de un solo paso: usa *function calling*, así que el modelo decide
cuántas búsquedas hacer y cuándo tiene evidencia suficiente.

Herramientas que se le exponen:

| Herramienta | Qué hace |
|---|---|
| `buscar_en_materiales` | Busca fragmentos relevantes en los documentos del curso |
| `listar_documentos` | Lista los documentos disponibles de un curso |
| `obtener_pagina` | Devuelve el texto completo de una página específica |

## Qué NO le corresponde

- **No decide permisos.** Recibe peticiones ya autorizadas por
  `utp-agent-api-academic` y siempre trabaja con `tenant_id` y `course_id`.
- **No inventa.** Si no encontró evidencia, debe decirlo. Hay una verificación en
  código: si respondió sin haber llamado a `buscar_en_materiales`, se rechaza.

## Dependencias clave

- **FastAPI** y **Pydantic**
- **Qdrant** como base vectorial
- **MinIO** en local, Azure Blob en la nube
- Proveedor de IA **detrás de una interfaz propia** (`ProveedorLLM`,
  `ProveedorEmbeddings`). Por defecto Gemini en capa gratuita; intercambiable.

## Límites de la capa gratuita

Embeddings: 100 peticiones/min. Generación: 15/min. **Indexar un PDF grande
falla con error 429 si no hay control de ritmo.** Cualquier código que llame al
proveedor debe pasar por el limitador y reintentar con espera exponencial.

## Convenciones

**Estrategia de ramificación: GitHub Flow con ramas personales.** `main` es la
única rama permanente compartida y siempre debe quedar ejecutable. No existe rama
`develop`. Cada integrante trabaja en su rama propia `dev/<nombre>`, que **no se
borra** al fusionar. Antes de cada tarea nueva se trae `main` a la rama propia.
Un Pull Request **por tarea**, con `Closes #NN`. Detalle completo en el ADR
2026-08-23-02 del repo `utp-agent-platform`.

- Tu rama: `dev/nicolas`. Nunca trabajes sobre `main`
- Rutas versionadas: `/api/v1/...`
- Tipado estricto con anotaciones de tipo en todas las funciones públicas
- Commits convencionales con ámbito `rag`: `feat(rag): ...`

## Prohibido sin confirmación explícita

- No acoplar la lógica directamente a un proveedor de IA: todo pasa por las
  interfaces.
- No agregar ni actualizar dependencias.
- No modificar el limitador de peticiones ni la lógica de reintentos.
- No modificar workflows de `.github/`.
- No escribir claves de API en el código ni en archivos versionados.
- Si crees que necesitas hacer algo de esta lista, detente y comenta en el issue.
