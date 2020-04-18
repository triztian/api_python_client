# Desarrollo y contribuciones

## Despliegue en PyPI

Tomado de el artículo: 

  * [How to upload your python package to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)

```bash
pip install twine
python setup.py sdist
twine upload dist/*
```