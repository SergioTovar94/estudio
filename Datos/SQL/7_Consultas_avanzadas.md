# Consultas avanzadas

## CASE

Es como un if/else dentro de SQL

```SQL
SELECT nombre,
  CASE
    WHEN edad >= 18 THEN 'Adulto'
    ELSE 'Menor'
  END as tipo
FROM usuarios;
```

CASE → inicia la lógica

WHEN → condición

THEN → resultado si se cumple

ELSE → opcional (si no cumple)

END → termina

## Check

Es una restricción (constraint) en la tabla

```SQL
CREATE TABLE usuarios (
  edad INT CHECK (edad >= 0)
);
```

# Subconsultas

```SQL
SELECT *
FROM ventas
WHERE cliente_id IN (
  SELECT id FROM clientes WHERE pais = 'CO'
);
```
