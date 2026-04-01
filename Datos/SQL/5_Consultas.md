# Consultas básicas

## Condiciones lógicas

Sirven para agregar condicionales a las consultas

| Tipo comparador      | SQL                           |
| -------------------- | ----------------------------- |
| Igualdad             | `=   <>   !=`                 |
| Comparación numérica | `>   <   >=   <=`             |
| Rangos               | `BETWEEN 10 AND 20`           |
| Listas               | `IN ('CO', 'MX', 'AR') `      |
| Texto                | `LIKE '%A%'    -- contiene A` |
| Nulos                | `IS NOT NULL `                |
| Lógicos              | `AND OR NOT`                  |

## DDL: Data Definition Language

Crean o alteran la tabla.

### Create

```SQL
CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nombre TEXT,
  edad INT
);
```

## DML: Data Manipulation Language

### Insert

```SQL
INSERT INTO usuarios (nombre, edad)
VALUES ('Sergio', 25);
```

## Update

```SQL

```

## Delete

```SQL

```

## DQL: Data Query Language

Son el tipo de consultas que se realizan sobre tablas que ya están estructuradas. No modifican la estructura de las tablas.

### Select

```SQL
SELECT nombre, edad
FROM usuarios;
```

Trae columnas específicas

## Filtro Where

Filtra filas antes de cualquier agrupación

```SQL
SELECT *
FROM usuarios
WHERE pais = 'Colombia';
```

Condiciones simples (=, >, <, LIKE)

## Ordenamiento

```SQL
SELECT *
FROM usuarios
ORDER BY edad DESC;
```

Ordena el resultado final, puede ser costoso sin índice.

## Limitar resultados

```SQL
SELECT *
FROM usuarios
LIMIT 10;
```

# Consultas intermedias

## Gropup By

Agrupa filas con valores iguales

```SQL
SELECT pais, COUNT(*)
FROM usuarios
GROUP BY pais;
```

## Having

Filtra después del GROUP BY

```SQL
SELECT pais, COUNT(*)
FROM usuarios
GROUP BY pais
HAVING COUNT(*) > 100;
```

Diferencia clave

| WHERE            | HAVING        |
| ---------------- | ------------- |
| Antes de agrupar | Después       |
| Filtra filas     | Filtra grupos |

# Partes de una consulta típica

```SQL
SELECT columnas
FROM tabla
JOIN ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...
```

SELECT columnas
FROM tabla
JOIN ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...
