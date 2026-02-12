# Definición

Los archivos Markdown, identificados por la extensión .md o .markdown, son documentos de texto plano que utilizan una sintaxis ligera para aplicar formato (negrita, encabezados, listas) sin necesidad de editores especiales. Son altamente legibles, convertibles a HTML y ampliamente usados en repositorios de código (GitHub), documentación técnica y sitios web.

## Características Principales y Sintaxis

**Texto Plano**: Se pueden crear y editar con cualquier editor de texto básico (Notepad, TextEdit, Vim).
**Formato Sencillo**:

- **Encabezados**: Se usan almohadillas, p.ej., # H1, ## H2.
- **Énfasis**: Asteriscos para cursiva (_texto_) o negrita (**texto**).
- **Listas**: Guiones (-), asteriscos (\*) o números (1.).
- **Enlaces**: [Texto](URL).
- **Código**: Acentos graves (`código`).
  **Conversión**: Se renderizan fácilmente a HTML para visualización web.

## ¿Dónde se utilizan?

**GitHub/GitLab**: Archivos README.md que describen repositorios.
**Generadores de Sitios Estáticos**: Jekyll, Hugo, etc..
**Notas y Documentación**: Obsidian, Notion, StackEdit.
**Correo Electrónico**: Extensiones para escribir correos con formato usando Markdown.

## Bloques de código

También permite encapsular texto para que sea reconocido como bloques de código.
Cuando se escribe:

```python

```

Se le está indicando al renderizador que es código en ese lenguaje y se le pide resaltarlo en esa sintáxis. Eso se llama syntax highlighting.

### ¿Qué lenguajes se pueden usar?

Permite lenguajes de programación, comandos CLI, Web, Datos SQL, DevOps.

**Python**

````markdown
```python
print("Hola mundo")
```
````

Generará

```python
print("Hola mundo")
```

**JavaScript**

````markdown
```javascript
console.log("Hola mundo");
```
````

Generará

```javascript
console.log("Hola mundo");
```

**TypeScript**

````markdown
```typescript
console.log("Hola mundo");
```
````

Generará

```typescript
console.log("Hola mundo");
```

**Java**

````markdown
```java
public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
    }
}
```
````

Generará

```java
public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
    }
}
```

**C**

````markdown
```c
#include <stdio.h>
int main() {
    printf("Hola mundo\n");
    return 0;
}
```
````

Generará

```c
#include <stdio.h>
int main() {
    printf("Hola mundo\n");
    return 0;
}
```

**C++**

````markdown
```cpp
#include <iostream>
int main() {
    std::cout << "Hola mundo" << std::endl;
    return 0;
}
```
````

Generará

```cpp
#include <iostream>
int main() {
    std::cout << "Hola mundo" << std::endl;
    return 0;
}
```

**go**

````markdown
```go
package main
import "fmt"
func main() {
    fmt.Println("Hola mundo")
}
```
````

Generará

```go
package main
import "fmt"
func main() {
    fmt.Println("Hola mundo")
}
```

**Rust**

````markdown
```rust
fn main() {
    println!("Hola mundo");
}
```
````

Generará

```rust
fn main() {
    println!("Hola mundo");
}
```

### CLI

**Bash**

````markdown
```bash
echo "Hola mundo"
```
````

Generará

```bash
echo "Hola mundo"
```
