# Sistemas Gestores de Bases de Datos

## Relacionales

Funcionan con modelos relacionales, tablas. La relación entre tablas es a partir de llaves y usan SQL.

Ventajas:

- Alta consisdencia ACID
- Estructura clara
- Muy confiables

Desventajas:

- Menos flexibles: debe hacerse Alter Table
- Escalan horizontalmente: los datos están relacionados mediante llaves. Separar puede romper relaciones.

### PostgreSQL

PostgreSQL es potente porque soporta funciones avanzadas como funciones de ventana, CTEs, JSON y tipos personalizados. Esto permite trabajar tanto con datos estructurados como semi-estructurados. Sin embargo, esa potencia implica mayor complejidad en administración, ya que requiere tuning, configuración de memoria e índices, y entender cómo el query planner ejecuta las consultas para optimizar el performance.

Ventajas: Potente y completo. Soporta JSON, buen rendimiento en consultas complejas.
Desventajas: Puede ser más pesado de administrar. No es más simple.
Usos: Backend robusto, analítica, data engeneering.

### MySQL

Ventaja: Fácil de usar, popular y buen rendimiento en lectura.
Desventaja: Menos potente que SQL. Menos flexible en features avanzadas.
Usos: Aplicaciones web y Startups.

### Microsoft SQL Server

Ventajas: Integración con ecosistema microsoft.
Desventajas: Licencia costosa
Usos: Empresas grandes

### Oracla Database

Ventajas: Robusto. Alto rendimiento. Escalabilidad empresarial.
Desventajas: Costoso y complejo.
Usos: Bancos, sistemas típicos.

### SQLite

Ventajas: Ligero, no requiere servidor.
Desventajas: No escala, limitado.
Usos: Apps móviles, prototipos.

Los sistemas relacionales son menos flexibles porque requieren un esquema definido, lo que garantiza consistencia pero limita cambios. Además, escalan peor horizontalmente debido a las relaciones entre datos y las transacciones ACID.
En cuanto a motores, PostgreSQL destaca por su potencia y flexibilidad, MySQL por su simplicidad, y otros como SQL Server u Oracle se usan más en entornos empresariales. La elección depende del caso de uso. Hoy en día muchas arquitecturas combinan SQL y NoSQL según la necesidad.

## NoSQL

Ventajas:
Desventajas:
Usos:

### Mongo DB

## Analídicos (Data Warehouse)

### Google BigQuery

## Data Lakes

### Amazon S3

### Google Cloud Storage

## Resumen

| Tipo           | Uso principal  | Ventaja clave        | Problema         |
| -------------- | -------------- | -------------------- | ---------------- |
| Relacional     | Transacciones  | Consistencia         | Escala           |
| NoSQL          | Big Data       | Flexibilidad         | Consistencia     |
| Data Warehouse | Analítica      | Velocidad en queries | No transaccional |
| Data Lake      | Almacenamiento | Bajo costo           | Desorden         |
| NewSQL         | Híbrido        | Balance              | Complejidad      |
