# Explicación y Uso del Scaffolding FastAPI + SQLModel

Este scaffolding está diseñado para generar automáticamente la estructura de un dominio en tu proyecto FastAPI usando SQLModel. A continuación se explica cómo funciona paso a paso y cómo usarlo.

---

## 1. Ejecución del script

Se ejecuta el archivo `scaffolding.py` mediante Python. Puede recibir flags opcionales para generar componentes específicos:

* `-models` → genera solo los modelos
* `-schemas` → genera solo los schemas
* `-repository` → genera solo el repository
* `-service` → genera solo el servicio
* `-router` → genera solo el router
* Sin flags → genera **todo**

### Ejemplos de uso:

```bash
python scaffolding.py           # Genera todo
python scaffolding.py -models    # Solo models
python scaffolding.py -service -router   # Solo service y router
python scaffolding.py -schemas -repository  # Solo schemas y repository
```

---

## 2. Decisión según flags

El script revisa los flags proporcionados:

* **Sin flags:** se generan todos los componentes: models, schemas, repository, service y router.
* **Con flags:** se generan únicamente los componentes indicados.

Esto permite flexibilidad para generar solo lo que se necesita sin tocar los demás archivos.

---

## 3. Verificación del dominio

El script pregunta por el nombre del dominio y verifica si ya existe la carpeta correspondiente en `app/domain/<dominio>`:

* **No existe:** se crea la carpeta y el archivo `__init__.py` para convertirla en un paquete Python.
* **Sí existe:** se sobrescriben únicamente los archivos que correspondan a los flags seleccionados.

Esto evita crear múltiples dominios con el mismo nombre y permite actualizar solo partes de un dominio existente.

---

## 4. Escritura de archivos

Según los flags (o todo si no hay flags), se escriben los siguientes archivos:

* `models.py` → define las clases SQLModel que representan la tabla en la base de datos.
* `schemas.py` → define los schemas Pydantic/SQLModel para validación y serialización.
* `repository.py` → contiene las operaciones CRUD básicas y funciones de filtrado sobre el modelo.
* `service.py` → lógica de negocio, interactúa con el repository y expone métodos para el router.
* `router.py` → define las rutas de FastAPI y las operaciones disponibles mediante endpoints REST.

---

## 5. Registro en main.py

Si se genera el **router**, el script agrega automáticamente en `app/main.py`:

* La línea de import del router: `from app.routers.<dominio> import router as <dominio>_router`
* La inclusión del router en la app: `app.include_router(<dominio>_router)`

Esto asegura que las rutas del nuevo dominio queden disponibles sin necesidad de editar manualmente `main.py`.

---

## 6. Resultado final

* Carpeta del dominio creada o actualizada en `app/domain/<dominio>`
* Archivos generados según flags o todo
* Router registrado automáticamente si corresponde
* Permite ejecución selectiva y evita sobreescribir archivos no deseados

---

## 7. Cómo usarlo paso a paso

1. **Abrir terminal** en la carpeta raíz del proyecto.
2. **Ejecutar el script** con Python:

   ```bash
   python scaffolding.py
   ```
3. **Ingresar el nombre del dominio** cuando el script lo pida.
4. **Elegir flags** si solo deseas generar componentes específicos, por ejemplo:

   ```bash
   python scaffolding.py -service -router
   ```
5. **Verificar que los archivos se hayan generado** dentro de `app/domain/<dominio>` y `app/routers/`.
6. **Router registrado automáticamente** en `main.py` si se generó.

Este flujo hace que agregar un nuevo dominio a tu proyecto sea rápido, consistente y seguro, con la flexibilidad de generar solo lo que necesites.
