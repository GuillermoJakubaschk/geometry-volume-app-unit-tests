# Project description

Este proyecto implementa el cálculo del volumen de distintas figuras geométricas en Python y valida su correcto funcionamiento con pruebas unitarias.

---

# Project structure explanation

En el proyecto se calculan las siguientes figuras geométricas:

- Caja  
- Cono  
- Cilindro  
- Esfera  

La carpeta `geometry` contiene los módulos encargados de calcular el volumen de todas las figuras.  
La carpeta `tests` contiene las pruebas unitarias implementadas con `pytest`, las cuales nos permiten verificar el correcto funcionamiento de cada función.  
El archivo `main.py` funciona como el punto de entrada del proyecto, ya que desde ahí se pueden ejecutar los distintos códigos que se encuentran dentro de la carpeta `geometry`.

Cabe resaltar que se utiliza la librería `math`, la cual nos permite realizar cálculos matemáticos y aproximar mejores valores como el del π.

---

# How to run main.py

Para ejecutar el main, uso el siguiente comando desde la PowerShell de Windows:

```bash
python main.py
```
# How to run tests

Las pruebas unitarias ya estan implementadas si usamos `pytest` el cual nos facilita al momento de querer hacer las pruebas.

Desde la PowerShell de Windows, ejecuto el siguiente comando:

```bash
python -m pytest -v
```

# Dependencies

Únicamente se utiliza la siguiente dependencia:

- pytest

Para poder instalarla, se escribe de la siguiente manera:

```bash
pip install pytest
```
Y con esto técnicamente debería funcionar sin problemas.
