# Google BigQuery

Google BigQuery es un almacén de datos (data warehouse) empresarial, "serverless" (sin servidor) y de alto rendimiento en la nube de Google Cloud. Permite analizar grandes volúmenes de datos (petabytes) utilizando SQL a una velocidad muy rápida. Es totalmente gestionado, lo que elimina la necesidad de administrar infraestructura.

Una base de datos relacional mantiene relaciones. En BigQuery se encarga de guardar grandes volúmenes de datos más que las relaciones.

Cobra bajo demanda, depende de lo que hagamos dentro de ella. Para hacer pruebas con tablas de pocos datos y procesamiento básico el cobro no es elevado. Da unos créditos gratuitos en Google Cloud.
Funciona por proyectos.

## Características y beneficios clave

- Arquitectura Serverless: No requiere configurar servidores, aprovisionar recursos ni gestionar bases de datos, lo que permite enfocarse en el análisis de datos.
- Velocidad de consulta: Utiliza BigQuery BI Engine y procesamiento paralelo para analizar terabytes en segundos y petabytes en minutos.
- SQL Estándar: Emplea SQL familiar para consultar conjuntos de datos, lo que facilita la adopción.
- Almacenamiento y Cómputo Separados: Permite escalar y pagar el almacenamiento y el procesamiento por separado, lo que optimiza costos.
- Machine Learning Integrado (BigQuery ML): Permite crear y ejecutar modelos de aprendizaje automático directamente en la consola usando consultas SQL.
- Integración: Se conecta nativamente con otras herramientas de Google Cloud (como Google Cloud Storage, Dataflow, VertexAI) y herramientas de visualización como Looker y Data Studio.

## ¿Para qué sirve?

BigQuery es ideal para el análisis de logs, eventos, datos de ventas y la creación de informes detallados de inteligencia empresarial (BI), siendo utilizado desde startups hasta empresas de Fortune 500

## Particionamiento y Clustering (el "índice" de BigQuery)

### Particionamiento

Divide una tabla en segmentos basados en una columna (normalmente una fecha).

```SQL
CREATE TABLE mydataset.eventos
PARTITION BY DATE(fecha_evento)
AS SELECT ...
```

- Las particiones permiten que las consultas con WHERE sobre esa columna lean solo las particiones necesarias.
- Tipos: partición por tiempo (DATE, TIMESTAMP) o por rango (INTEGER).

### Clustering

Ordena físicamente los datos dentro de cada partición según una o más columnas.

```SQL
CREATE TABLE mydataset.eventos
PARTITION BY DATE(fecha_evento)
CLUSTER BY usuario_id, categoria
AS SELECT ...
```

- Mejora consultas que filtran por las columnas de clustering.
- Se usa junto con particionamiento para maximizar rendimiento.

## JSON en BigQuery

Si tienes un campo con JSON, BigQuery ofrece funciones para extraer valores.

| Función                             | Descripción                                            |
| ----------------------------------- | ------------------------------------------------------ |
| JSON_EXTRACT(json, '$.path')        | Devuelve el valor como JSON (puede ser objeto o array) |
| JSON_EXTRACT_SCALAR(json, '$.path') | Devuelve el valor como STRING (para datos escalares)   |
| JSON_QUERY(json, '$.path')          | Similar a JSON_EXTRACT                                 |
| JSON_VALUE(json, '$.path')          | Similar a JSON_EXTRACT_SCALAR                          |

Ejemplo práctico:

Supongamos una tabla eventos con columna datos (JSON). Queremos extraer el campo usuario.id y accion.

```SQL
SELECT
  JSON_EXTRACT_SCALAR(datos, '$.usuario.id') AS user_id,
  JSON_EXTRACT_SCALAR(datos, '$.accion') AS accion,
  COUNT(*) AS eventos
FROM eventos
WHERE JSON_EXTRACT_SCALAR(datos, '$.accion') = 'compra'
GROUP BY user_id, accion;
```

Si tienes un array dentro del JSON, puedes usar UNNEST para expandirlo.

```SQL
SELECT
  JSON_EXTRACT_SCALAR(item, '$.producto') AS producto,
  COUNT(*) AS ventas
FROM eventos,
UNNEST(JSON_EXTRACT_ARRAY(datos, '$.items')) AS item
GROUP BY producto;
```

## Tablas Externas

BigQuery puede consultar datos directamente desde archivos en Cloud Storage (CSV, JSON, Parquet, Avro) sin cargarlos.

```SQL
CREATE TABLE mydataset.eventos
PARTITION BY DATE(fecha_evento)
AS SELECT ...
```

## Optimización

- Filtra lo antes posible: usa WHERE sobre columnas particionadas/clusterizadas.
- Evita SELECT \*: especifica solo las columnas que necesitas.
- Reduce el volumen de datos: si solo necesitas un rango de fechas, filtra por esa partición.
- Usa LIMIT en exploración: para pruebas rápidas.
- Materializa resultados intermedios: con tablas temporales o vistas materializadas si la misma lógica se usa repetidamente.
