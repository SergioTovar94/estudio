# Configuración del proyecto

Vite → herramienta que crea y ejecuta el proyecto rápido

React → librería para construir la interfaz

npm → gestor de paquetes de Node

Axios o fetch → para hablar con tu API backend

# Estructura del proyecto

mi_proyecto/
│
├── backend/
│ ├── manage.py
│ ├── api/
│ └── ...
│
└── frontend/

mkdir frontend
cd frontend

npm create vite@latest .

create: comando que ejecuta generadores de proyectos.

Eliges:

- React
- JavaScript
- No a usar vite 8 beta
- Si a Install npm and start now: para que isntale todas las dependencias del proyecto y levante el servidor de desarrollo
  Luego:

cd frontend
npm install
npm run dev

¿Cómo se conectan?

El backend corre en:

http://localhost:8000

El frontend corre en:

http://localhost:5173

React hace peticiones al backend usando:

fetch("http://localhost:8000/api/pacientes/")
