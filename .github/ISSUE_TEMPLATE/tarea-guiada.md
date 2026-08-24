---
name: Tarea guiada
about: Tarea con alcance acotado para trabajar con un agente de IA (Antigravity o Claude Code)
title: ''
labels: ''
assignees: ''
---

## Objetivo
Una frase. Qué debe existir cuando termines.

## Archivos que SÍ debes tocar
-

## Archivos que NO debes tocar bajo ninguna circunstancia
- Todo lo demás. Si crees que necesitas otro archivo, comenta en este issue antes de tocarlo.

## Ejemplo a seguir
Copia el patrón exacto de una función ya existente en `app/`.

## Criterios de aceptación
- [ ]
- [ ]

## Cómo verificar antes de abrir el Pull Request
```bash
uv run pytest
uv run ruff check .
```

## Reglas
- No agregar ni actualizar dependencias sin avisar.
- No modificar el limitador de peticiones ni la lógica de reintentos.
- Si algo no está claro, pregunta en este issue en vez de improvisar.
