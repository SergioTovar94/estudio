# Formularios

Un formulario es un mecanismo para enviar datos del usuario al servidor

Ejemplo clásico:

- Login
- Registro
- Buscador
- Comentarios

```HTML
<form action="/login" method="POST">
  <input type="text" name="usuario" />
  <input type="password" name="clave" />
  <button type="submit">Enviar</button>
</form>
```

## <form>

| Atributo       | ¿Para qué sirve?                                 | Ejemplo                                |
| -------------- | ------------------------------------------------ | -------------------------------------- |
| `action`       | URL a donde se enviarán los datos                | `<form action="/login">`               |
| `method`       | Método HTTP (`GET` o `POST`)                     | `<form method="POST">`                 |
| `enctype`      | Tipo de codificación (ej. para subir archivos)   | `<form enctype="multipart/form-data">` |
| `autocomplete` | Activa/desactiva autocompletado                  | `<form autocomplete="off">`            |
| `novalidate`   | Desactiva validaciones automáticas del navegador | `<form novalidate>`                    |
| `id`           | Identificador único                              |                                        |
| `class`        | Aplicar estilos                                  |                                        |

## <textarea>

| Atributo      | ¿Para qué sirve?            | Ejemplo                                 |
| ------------- | --------------------------- | --------------------------------------- |
| `name`        | Nombre del campo            | `<textarea name="mensaje">`             |
| `rows`        | Número de filas visibles    | `<textarea rows="4">`                   |
| `cols`        | Número de columnas visibles | `<textarea cols="50">`                  |
| `placeholder` | Texto guía                  | `<textarea placeholder="Escribe aquí">` |
| `required`    | Campo obligatorio           |                                         |
| `maxlength`   | Límite de caracteres        |                                         |
| `disabled`    | Desactiva el campo          |                                         |
| `readonly`    | Solo lectura                |                                         |
| `id`          | Identificador               |                                         |
| `class`       | Estilos                     |                                         |

## <select>

| Atributo   | ¿Para qué sirve?                    | Ejemplo                |
| ---------- | ----------------------------------- | ---------------------- |
| `name`     | Nombre del campo                    | `<select name="pais">` |
| `multiple` | Permite seleccionar varias opciones | `<select multiple>`    |
| `required` | Campo obligatorio                   |                        |
| `disabled` | Desactiva el select                 |                        |
| `size`     | Número de opciones visibles         | `<select size="4">`    |
| `id`       | Identificador                       |                        |
| `class`    | Estilos                             |                        |

## <option>

| Atributo   | ¿Para qué sirve?          | Ejemplo                                |
| ---------- | ------------------------- | -------------------------------------- |
| `value`    | Valor enviado al servidor | `<option value="co">Colombia</option>` |
| `selected` | Marca opción por defecto  | `<option selected>`                    |
| `disabled` | Desactiva la opción       |                                        |

## <label>

| Atributo | ¿Para qué sirve?                | Ejemplo                 |
| -------- | ------------------------------- | ----------------------- |
| `for`    | Vincula con el `id` de un input | `<label for="usuario">` |
| `id`     | Identificador                   |                         |
| `class`  | Estilos                         |                         |
