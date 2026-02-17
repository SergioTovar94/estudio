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
