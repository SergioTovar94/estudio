# ¿Qué es Polars?

Polars es una librería de análisis de datos para Python (y Rust) diseñada para ser:

⚡ Extremadamente rápida
🧠 Eficiente en memoria
🧵 Paralela por defecto
🗂 Basada en Apache Arrow

Es una alternativa moderna a pandas, pensada para datasets grandes y pipelines de datos más robustos.

¿Por qué nació Polars?

Porque pandas:

- No es paralela por defecto.
- Puede consumir mucha memoria.
- Se vuelve lenta con datasets grandes (millones de filas).

Polars fue construida en Rust, lo que le da:

- Mayor rendimiento.
- Mejor control de memoria.
- Ejecución multihilo automática.

## DataFrame

import polars as pl

```Python
df = pl.DataFrame({
    "nombre": ["Ana", "Luis", "Carlos"],
    "edad": [25, 30, 22]
})
```

## Lazy vs Eager

Polars tiene dos modos:

🔹 Eager (ejecuta inmediatamente)

```Python
df.filter(pl.col("edad") > 23)
```

Se ejecuta en el momento.

🔹 Lazy (modo optimizado)

```Python
df.lazy().filter(pl.col("edad") > 23).collect()
```

Aquí no ejecuta inmediatamente.
Primero construye un plan de ejecución optimizado, luego lo ejecuta con .collect()

Este enfoque permite:

- Reordenar operaciones
- Eliminar cálculos innecesarios
- Leer solo columnas necesarias (projection pushdown)
- Filtrar antes de cargar todo (predicate pushdown)

## Sintaxis moderna basada en expresiones

En Polars no trabajas tanto con operaciones fila por fila.

Trabajas con expresiones declarativas:

```Python
df.select([
    pl.col("edad") * 2,
    pl.col("nombre")
])
```

## Dataframe

Un DataFrame en Polars es una tabla de datos que ya está cargada en memoria y lista para ejecutarse inmediatamente.

## Lazyframe

Un LazyFrame es algo diferente. No ejecuta nada inmediatamente. Es más bien un plan de ejecución pendiente.

```Python
df = pl.scan_csv("datos.csv")

resultado = (
    df
    .filter(pl.col("edad") > 18)
    .select(["nombre", "edad"])
)
```

Hasta aquí no ha pasado nada. Solo se ha construido un plan lógico. Solo cuando haces:

```Pyton
resultado.collect()
```

Se ejecuta todo.

⚡ Diferencia conceptual profunda

### DataFrame (Eager)

- Ejecuta paso a paso.
- Cada línea transforma datos reales.
- Más simple mentalmente.
- Puede ser menos eficiente en pipelines grandes.

### LazyFrame (Lazy)

- Construye un plan completo.
- Optimiza antes de ejecutar.
- Ejecuta todo junto al final.
- Mucho más eficiente para pipelines grandes.

## Funciones globales de Polaras

| Función             | Descripción                           | Ejemplo                                       |
| ------------------- | ------------------------------------- | --------------------------------------------- |
| `pl.read_csv()`     | Lee un CSV en modo eager              | `df = pl.read_csv("datos.csv")`               |
| `pl.scan_csv()`     | Lee un CSV en modo lazy               | `df = pl.scan_csv("datos.csv")`               |
| `pl.read_parquet()` | Lee archivo Parquet                   | `df = pl.read_parquet("datos.parquet")`       |
| `pl.concat()`       | Concatena DataFrames                  | `pl.concat([df1, df2])`                       |
| `pl.col()`          | Referencia una columna en expresiones | `pl.col("edad") > 18`                         |
| `pl.lit()`          | Crea un valor literal en expresión    | `pl.lit(1)`                                   |
| `pl.when()`         | Expresión condicional                 | `pl.when(pl.col("edad") > 18).then("Adulto")` |
| `pl.sum()`          | Expresión de suma                     | `df.select(pl.sum("ventas"))`                 |
| `pl.mean()`         | Expresión de promedio                 | `df.select(pl.mean("edad"))`                  |
| `pl.Series()`       | Crear una Series manualmente          | `pl.Series("edad", [1,2,3])`                  |

## Métodos sobre objetos Dataframe y LazyFrame

| Método            | Tipo de objeto        | Descripción                       | Ejemplo                                              |
| ----------------- | --------------------- | --------------------------------- | ---------------------------------------------------- |
| `.select()`       | DataFrame / LazyFrame | Selecciona columnas o expresiones | `df.select("edad")`                                  |
| `.filter()`       | DataFrame / LazyFrame | Filtra filas                      | `df.filter(pl.col("edad") > 18)`                     |
| `.with_columns()` | DataFrame / LazyFrame | Añade o modifica columnas         | `df.with_columns((pl.col("edad")+1).alias("edad2"))` |
| `.drop()`         | DataFrame             | Elimina columnas                  | `df.drop("edad")`                                    |
| `.rename()`       | DataFrame             | Renombra columnas                 | `df.rename({"edad": "age"})`                         |
| `.group_by()`     | DataFrame / LazyFrame | Agrupa datos                      | `df.group_by("ciudad").count()`                      |
| `.join()`         | DataFrame / LazyFrame | Une DataFrames                    | `df1.join(df2, on="id")`                             |
| `.sort()`         | DataFrame / LazyFrame | Ordena datos                      | `df.sort("edad")`                                    |
| `.collect()`      | LazyFrame             | Ejecuta el plan lazy              | `df.lazy().select(...).collect()`                    |
| `.head()`         | DataFrame             | Muestra primeras filas            | `df.head(5)`                                         |
