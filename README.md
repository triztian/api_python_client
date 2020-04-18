# API.datos.gob.mx - cliente de python

Script base para la consulta de datos al API de: 

  * https://api.datos.gob.mx/v2

## Installación

```bash
pip install --user datosgobmx
```

## Uso

### Como librería

```python
import datosgobmx.client as api

# Retorna una lista de _Endpoints_
# https://api.datos.gob.mx/v2/api-catalog
#
# Cada _Endpoint_ tiene la siguiente estructura, los contenidos de cada endpoint
# serán distintos:
#
# {
#   "_id": "5cccf090e2705c193281f0aa",
#   "variables": [
#     "_id",
#     "ocid",
#     "releases",
#     "compiledRelease"
#   ],
#   "count": 300265,
#   "url": "https://api.datos.gob.mx/v2/Records",
#   "endpoint": "Records"
# }
api_catalog = api()
```

Otro ejemplo, para obtener una lista the URLs y endpoints disponibles en la 
segunda página del catalogo puedes realizar lo siguiente.

```python
import datosgobmx.client as api

for endpoint in api(query={'page': 2}):
	print(endpoint['url'], endpoint['endpoint'])
```

> NOTA: El método `api` toma un segundo parametro `query` que es un diccionario
> opcional.
> Tiene el formato de query descrito en https://github.com/mxabierto/api#filtros

El REST API v2 esta descrito en el siguiente enlace, esto incluye
los objetos JSON retornados por los endpoints:

  * [API v2](https://github.com/mxabierto/api)

### Como script independiente

Si no se tiene acceso a `pip`, uno puede copiar el script `datosgobmx/client.py`
a su computadora y directorio de preferencia y ejecutarlo de la siguiente 
manera:

```bash
python3 client.py
```

---

## Licencia
Software libre, puede ser redistribuido bajo los términos especificados en nuestra [licencia](https://datos.gob.mx/libreusomx).

## Sobre México Abierto
En México Abierto creamos mecanismos de innovación y colaboración entre ciudadanos y gobierno con herramientas digitales, para	impulsar el desarrollo del país.
