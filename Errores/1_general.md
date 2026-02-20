# 1. ¿Qué es realmente el manejo de errores?

En Python, manejar errores significa controlar lo que pasa cuando algo falla, en vez de dejar que el programa se rompa de forma desordenada.

En Python eso se hace con:

```Python
try:
    # código que puede fallar
except:
    # qué hacer si falla
```

Pero eso es solo la superficie. Lo importante es cuándo, dónde y por qué hacerlo.

# 2. Regla de oro

- No uses manejo de errores para controlar lógica normal.
- Úsalo solo cuando algo realmente puede fallar por razones externas o impredecibles.

# 3. Cuándo SÍ usar manejo de errores

## Cuando algo depende del mundo externo

Ejemplos:

- Leer archivos
- Conectarse a una API
- Base de datos
- Parsear datos
- Input del usuario

```Python
try:
df = pl.read_csv(path)
except FileNotFoundError:
print(f"No existe el archivo: {path}")
```

Porque:

- El archivo puede no existir
- Puede estar corrupto
- Puede tener encoding raro
- Puede tener permisos restringidos

## Cuanto trabajas con datos que no controlas

## Cuando quieres transformar el error

# Cuando no usar manejo de errores

## Validar condiciones simples

## Except vacio

## No capturar excepciones generales

# Buenas prácticas

## Capturar lo más cerca del origen posible

## No ocultar errores

# Tipos de errores comunes

## Runtime error

Es una excepción genérica incluida en Python que significa Error en tiempo de ejecución. Es decir:

- No es un error de sintáxis
- No es un error detectado antes de correr el programa
- Es un error que ocurre mientras el programa está ejecutándose

```Markdown
BaseException
 └── Exception
      └── RuntimeError
```

RuntimeError es una subclase de Exception.

## Errores de valores y tipos

### Value error

Valor válido en tipo pero incorrecto en contenido

### Type Error

Tipo incorrecto

## Errores matemáticos

### ZeroDivisionError

División por cero

### OverflowError

Número demasiado grande

## Errores de acceso

### Index error

Índice fuera de rango

### Key error

Clave inexistente en el diccionario

### Attribute error

Objeto no contiene el atributo

## Errores de archivos y sistema

### FileNotFoundError

Archivo no existe.

### PermissionError

No tienes permisos.

### IsADirectoryError

Intentas abrir carpeta como archivo.

## Errores de importación

### ImportError

### ModuleNotFoundError

## Errores de iteración

### StopIteration

Se usa internamente en iteradores.

## Errores de aserción

### AssertionError

assert x > 0

## Errores más generales

### RuntimeError

Problema general de ejecución.

### NotImplementedError

Cuando una función aún no está implementada.
