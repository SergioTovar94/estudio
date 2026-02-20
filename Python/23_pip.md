# ¿Qué es PIP?

pip es el gestor de paquetes oficial de Python.
Su nombre viene de “Pip Installs Packages”.

Con pip puedes:

- Instalar librerías externas
- Actualizarlas
- Eliminarlas
- Ver qué tienes instalado
- estionar versiones específicas

En otras palabras: es la herramienta que conecta tu proyecto con el ecosistema de librerías de Python.

## ¿Desde donde instala los paquetes?

Por defecto, pip instala desde:

🔹 Python Package Index (PyPI)

Es el repositorio oficial de paquetes Python. Ahí están librerías como:

- pandas
- numpy
- requests
- polars
- ydata-profiling
- etc.

Comandos más importantes

Te dejo los que más vas a usar en tu día a día 👇

📦 Instalar un paquete
pip install pandas

📌 Instalar una versión específica
pip install pandas==2.2.0

🔄 Actualizar un paquete
pip install --upgrade pandas

❌ Desinstalar
pip uninstall pandas

📋 Ver lo que tienes instalado
pip list

📄 Generar archivo requirements.txt
pip freeze > requirements.txt

📥 Instalar desde requirements.txt
pip install -r requirements.txt

Esto es clave cuando trabajas en proyectos como el tuyo de análisis electoral.
