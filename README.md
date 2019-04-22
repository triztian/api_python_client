# API.datos.gob.mx - cliente de python

## Uso
Script base para la consulta de datos al API de https://api.datos.gob.mx/v2

Puedes ejecutar el script con: `python3 client.py`

Tambien puedes instalarlo directamente con pip: `pip install datosgobmx`

Para utilizarlo, puedes primero importar la librería con: `import datosgobmx.client as api`
y luego hacer llamadas tipo `api.api("endpoint", {"page": 2})`, el segundo parámetro opcional, tiene el formato de query descrito en https://github.com/mxabierto/api#filtros

## Despliegue en PyPI

Tomado de https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

```
pip install twine
python setup.py sdist
twine upload dist/*
```

## Licencia
Software libre, puede ser redistribuido bajo los términos especificados en nuestra [licencia](https://datos.gob.mx/libreusomx).

## Sobre México Abierto
En México Abierto creamos mecanismos de innovación y colaboración entre ciudadanos y gobierno con herramientas digitales, para	impulsar el desarrollo del país.
