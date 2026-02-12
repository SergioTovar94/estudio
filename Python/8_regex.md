# Regex

Hace referencia a expresiones regulares, es una forma de buscar, validar o modificar texto usando patrones.

Sirve para:

- Validar emails, teléfonos, contraseñas
- Buscar palabras específicas
- Extraer partes de un texto
- Reemplazar texto de forma inteligente

Ejemplo mental:
“Quiero encontrar todos los números dentro de un texto”

## El módulo re

En Python, todo regex vive en el módulo re.

`import re`

## Metacaracteres

### Literales y Escape

| Símbolo | Significado                  |
| ------- | ---------------------------- |
| `\`     | Escapa caracteres especiales |

### Clases de Caracteres

| Símbolo  | Significado                                     |
| -------- | ----------------------------------------------- |
| `.`      | Cualquier carácter excepto salto de línea       |
| `[...]`  | Conjunto de caracteres (cualquiera dentro)      |
| `[^...]` | Conjunto negado (cualquiera excepto los dentro) |
| `\d`     | Cualquier dígito (0-9)                          |
| `\D`     | Cualquier no-dígito                             |
| `\w`     | Carácter de palabra (letras, dígitos, \_)       |
| `\W`     | Carácter que no es de palabra                   |
| `\s`     | Espacio en blanco                               |
| `\S`     | No-espacio en blanco                            |

### Cuantificadores

| Símbolo | Significado                                |
| ------- | ------------------------------------------ |
| `*`     | 0 o más repeticiones del carácter anterior |
| `+`     | 1 o más repeticiones del carácter anterior |
| `?`     | 0 o 1 repetición del carácter anterior     |
| `{n}`   | Exactamente n repeticiones                 |
| `{n,}`  | n o más repeticiones                       |
| `{n,m}` | Entre n y m repeticiones                   |

### Anclas (Posición)

| Símbolo | Significado                 |
| ------- | --------------------------- |
| `^`     | Inicio de la cadena o línea |
| `$`     | Fin de la cadena o línea    |

### Grupos y Captura

| Símbolo | Significado     |
| ------- | --------------- |
| `(...)` | Grupo o captura |

### Alternancia (Decisión)

| Símbolo | Significado     |
| ------- | --------------- |
| `\|`    | O (alternancia) |

## Métodos de re

| Método          | Descripción                                   | Ejemplo                                        |
| --------------- | --------------------------------------------- | ---------------------------------------------- |
| `re.match()`    | Busca al inicio de la cadena                  | `re.match(r'\d+', '123abc')` → Match           |
| `re.search()`   | Busca en cualquier parte de la cadena         | `re.search(r'\d+', 'abc123')` → Match          |
| `re.findall()`  | Retorna lista de todas las coincidencias      | `re.findall(r'\d+', 'a1b2c3')` → ['1','2','3'] |
| `re.finditer()` | Retorna iterador de objetos Match             | `re.finditer(r'\d+', 'a1b2')` → iterador       |
| `re.sub()`      | Reemplaza coincidencias por un texto          | `re.sub(r'\d+', 'X', 'a1b2')` → 'aXbX'         |
| `re.split()`    | Divide la cadena por coincidencias del patrón | `re.split(r'\d+', 'a1b2c')` → ['a','b','c']    |
| `re.compile()`  | Compila un patrón para reutilizarlo           | `patron = re.compile(r'\d+')` → patrón         |
