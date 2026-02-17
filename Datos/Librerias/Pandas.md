# Pandas

En 2008, AQR Capital Management comenzó a desarrollar pandas . A finales de 2009, ya era de código abierto y hoy cuenta con el apoyo activo de una comunidad de personas con ideas afines en todo el mundo que aportan su valioso tiempo y energía para hacer posible el código abierto de pandas . Gracias a todos nuestros colaboradores .

# ¿Qué es un Dataframe

Un DataFrame es una tabla de datos en memoria y tiene:

- Filas → registros (ej: una persona, una votación, una venta)
- Columnas → variables (edad, nombre, votos, fecha…)
- Índice → identificador de cada fila

| índice | nombre | edad | ciudad   |
| ------ | ------ | ---- | -------- |
| 0      | Ana    | 25   | Bogotá   |
| 1      | Luis   | 30   | Cali     |
| 2      | Carlos | 22   | Medellín |

# ¿Qué lo hace diferente de una lista o diccionario?

Podrías guardar eso como:

```Python
[
  {"nombre": "Ana", "edad": 25},
  {"nombre": "Luis", "edad": 30}
]
```

Pero un DataFrame:

- Está optimizado para operar columnas completas
- Permite cálculos vectorizados
- Tiene funciones estadísticas integradas
- Está diseñado para análisis de datos

## Estructuras de datos

### Dataframe

Tabla bidimensional (filas y columnas)

### Series

Una columna individual

df["Edad"]

Un DataFrame es básicamente un conjunto de Series alineadas por índice.

# Métodos de Pandas

| Método          | Descripción                    | Ejemplo                       |
| --------------- | ------------------------------ | ----------------------------- |
| `head()`        | Muestra las primeras filas     | `df.head(5)`                  |
| `tail()`        | Muestra las últimas filas      | `df.tail(3)`                  |
| `info()`        | Información sobre el DataFrame | `df.info()`                   |
| `describe()`    | Estadísticas descriptivas      | `df.describe()`               |
| `shape`         | Dimensiones (filas, columnas)  | `df.shape`                    |
| `columns`       | Nombres de las columnas        | `df.columns`                  |
| `dtypes`        | Tipos de datos de cada columna | `df.dtypes`                   |
| `isnull()`      | Detecta valores nulos          | `df.isnull()`                 |
| `fillna()`      | Rellena valores nulos          | `df.fillna(0)`                |
| `drop()`        | Elimina filas o columnas       | `df.drop('edad', axis=1)`     |
| `sort_values()` | Ordena por columna             | `df.sort_values('edad')`      |
| `groupby()`     | Agrupa datos                   | `df.groupby('ciudad').sum()`  |
| `merge()`       | Une DataFrames                 | `pd.merge(df1, df2, on='id')` |
| `loc[]`         | Selecciona por etiqueta        | `df.loc[0, 'nombre']`         |
| `iloc[]`        | Selecciona por posición        | `df.iloc[0, 1]`               |

# Funciones Globales de Pandas

| Pd.   | Función         | Descripción                | Ejemplo                                              |
| ----- | --------------- | -------------------------- | ---------------------------------------------------- |
| `pd.` | `read_csv()`    | Lee archivo CSV            | `pd.read_csv('datos.csv')`                           |
| `pd.` | `read_excel()`  | Lee archivo Excel          | `pd.read_excel('datos.xlsx')`                        |
| `pd.` | `read_json()`   | Lee archivo JSON           | `pd.read_json('datos.json')`                         |
| `pd.` | `read_sql()`    | Lee datos de base de datos | `pd.read_sql(query, conexión)`                       |
| `pd.` | `DataFrame()`   | Crea un DataFrame          | `pd.DataFrame({'col1': [1, 2]})`                     |
| `pd.` | `Series()`      | Crea una Series            | `pd.Series([1, 2, 3])`                               |
| `pd.` | `concat()`      | Concatena DataFrames       | `pd.concat([df1, df2])`                              |
| `pd.` | `merge()`       | Une DataFrames             | `pd.merge(df1, df2, on='id')`                        |
| `pd.` | `pivot_table()` | Crea tabla pivote          | `pd.pivot_table(df, values='venta', index='ciudad')` |
| `pd.` | `to_csv()`      | Guarda CSV                 | `df.to_csv('salida.csv')`                            |
| `pd.` | `to_excel()`    | Guarda Excel               | `df.to_excel('salida.xlsx')`                         |
| `pd.` | `to_json()`     | Guarda JSON                | `df.to_json('salida.json')`                          |
