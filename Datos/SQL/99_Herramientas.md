# El Optimizador de Consultas (Query Optimizer)

El planificador/optimizador es el "cerebro" de PostgreSQL. Su trabajo es encontrar la manera más eficiente de ejecutar una consulta SQL. No ejecuta la consulta para ver cuánto tarda, sino que estima el coste de diferentes estrategias (escaneo secuencial, uso de diferentes índices, tipos de joins, etc.) y elige la de menor coste.

Para realizar estas estimaciones, el optimizador se basa en dos fuentes principales de información:

## Estadisticas de tabla

Información a nivel de tabla como el número aproximado de filas (reltuples) y el número de páginas de disco que ocupa (relpages).

## Estadísticas de columna

pg_stats es una vista más amigable que muestra datos como:

- null_frac: Fracción de valores nulos.
- n_distinct: Número estimado de valores distintos.
- most_common_vals (MCV) y most_common_freqs: Los valores más frecuentes y su frecuencia. Esencial para estimar la selectividad de condiciones de igualdad.
- histogram_bounds: Límites que dividen los datos en grupos de aproximadamente el mismo tamaño. Fundamental para estimar la selectividad de condiciones de rango (ej. WHERE precio > 100).
- correlation: Mide la correlación entre el orden físico de las filas en el disco y el orden lógico de los valores de la columna. Un valor cercano a 1 indica que los valores están ordenados físicamente de la misma manera que lógicamente.

Para ver el plan que ha elegido el optimizador, usamos EXPLAIN. EXPLAIN ANALYZE ejecuta la consulta y muestra el plan junto con los tiempos y filas reales, permitiéndonos comparar la estimación con la realidad y diagnosticar problemas

## Muestreo aleatorio vs Correlación física

¿Cómo recopila PostgreSQL las estadísticas? Lo hace mediante un proceso llamado ANALYZE (que puede ejecutarse manualmente o mediante el proceso autovacuum).

Para llenar las vistas pg_stats, PostgreSQL no lee toda la tabla (sería prohibitivo en tablas grandes). En su lugar, realiza un muestreo aleatorio de filas. El tamaño de esta muestra está controlado por la variable default_statistics_target (por defecto, 100). Un valor más alto significa una muestra más grande y estadísticas más precisas, a costa de un ANALYZE más lento

Ahora bien, una vez que las estadísticas están en su lugar, el optimizador las usa para tomar decisiones. Un factor crucial es la correlation

### Correlación

Alta correlación (cercana a 1 o -1): Significa que las filas con valores similares en la columna indexada están físicamente cerca en el disco. Si el optimizador decide usar un índice para una consulta de rango, asumirá que las lecturas de disco serán secuenciales (más baratas, seq_page_cost).

Baja correlación (cercana a 0): Significa que los valores están dispersos aleatoriamente por el disco. Si se usa el índice, cada fila recuperada probablemente requerirá una lectura aleatoria (más cara, random_page_cost). En este caso, para un rango grande, el optimizador podría preferir un escaneo secuencial completo a usar el índice, ya que las lecturas aleatorias serían demasiado costosas

Por lo tanto, aunque la construcción de las estadísticas se basa en un muestreo aleatorio, la información que proporcionan, especialmente la correlación, le dice al optimizador cómo están ordenados los datos en el mundo real (el disco). No es que el optimizador haga un nuevo muestreo en el momento de la consulta, sino que confía en la "foto instantánea" que ANALYZE tomó mediante ese muestreo aleatorio.

## ¿Como estima el optimizador?

- Para igualdad: Si el valor buscado está en most_common_vals, la selectividad es su frecuencia asociada. Si no, se asume una frecuencia baja basada en los valores menos comunes.
- Para rangos: El optimizador utiliza histogram_bounds. Si el límite inferior de tu consulta cae dentro de un "bucket" del histograma, se interpola linealmente para estimar cuántos buckets se cubren
- Para patrones: Si el patrón no está anclado al inicio, las estadísticas tradicionales son de poca ayuda y PostgreSQL a menudo recurre a valores por defecto "hardcodeados" (ej. 0.5% de las filas)
