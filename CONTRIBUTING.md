# Desarrollo y contribuciones

## Ejecucion de pruebas

Para ejecutar las pruebas puede utilizar el comando desde la raíz del projecto:

```bash
python3 -m unittest tests.test_client
```

> NOTA: Se recomienda ejecutar la pruebas y verificar que sean exitosas antes
> de publicar a PyPI

## Despliegue en PyPI

Tomado de el artículo: 

  * [How to upload your python package to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)

```bash
pip install twine
python setup.py sdist
twine upload dist/*
```
