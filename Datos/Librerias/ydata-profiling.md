# ¿Qué es pandas-profiling?

pandas-profiling fue una librería muy popular en ciencia de datos para hacer análisis exploratorio automático (EDA).

Tú hacías algo así:

```Python
from pandas_profiling import ProfileReport

profile = ProfileReport(df)
profile.to_file("reporte.html")
```

Y automáticamente te generaba un reporte con:

- Estadísticas descriptivas
- Valores nulos
- Distribuciones
- Correlaciones
- Variables categóricas
- Detección de outliers
- Advertencias

Era súper útil para fase de Data Understanding en CRISP.

## ¿Qué pasó con pandas-profiling?

Fue renombrado y evolucionó.

Ahora se llama:

ydata-profiling

Es básicamente la versión moderna y mantenida del mismo proyecto.

No son dos librerías distintas activas.
YData Profiling es la continuación oficial.

# Constructor principal

Todo gira alrededor de:

```Python
from ydata_profiling import ProfileReport
profile = ProfileReport(df)
```

Pero casi nunca deberías usarlo sin parámetros.
Los más usados:

```Python
profile = ProfileReport(
    df,
    title="Perfil Congreso 2022",
    explorative=True,
    minimal=False
)
```

Parámetros importantes:

- title → Título del reporte.
- explorative=True → Activa análisis más profundo.
- minimal=True → Mucho más ligero (clave para datasets grandes).
- dark_mode=True → Solo visual.
- Para tus datasets grandes, minimal=True puede salvarte RAM.

# Métodos más utilizados

## to_file()

El más común.
`profile.to_file("reporte.html")`
Genera HTML interactivo.

Hay también en

### to_notebook_iframe(), to_json(), to_widgets()

## Atributos útiles

Después de crear el objeto:
`profile = ProfileReport(df)`

Se puede acceder a:
`profile.description_set`
Contiene estadísticas internas.
