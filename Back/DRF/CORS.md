🔧 Cómo se usa normalmente

1️⃣ Instalar:

pip install django-cors-headers

2️⃣ En settings.py:

INSTALLED_APPS = [
"corsheaders",
]

3️⃣ Agregar middleware:

MIDDLEWARE = [
"corsheaders.middleware.CorsMiddleware",
]

4️⃣ Permitir orígenes:

CORS_ALLOW_ALL_ORIGINS = True

o más seguro:

CORS_ALLOWED_ORIGINS = [
"http://localhost:5173",
]
