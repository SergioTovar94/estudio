# Funciones de ventana

Las funciones de ventana (window functions) en SQL son funciones que te permiten hacer cálculos sobre un conjunto de filas relacionadas, sin agruparlas en una sola fila.

```SQL
SELECT
    empleado,
    salario,
    AVG(salario) OVER () AS salario_promedio
FROM empleados;
```

## Agregadas como ventana

- SUM()
- AVG()
- COUNT()
- MAX()
- MIN()

👉 Pero ahora con OVER()

## Funciones de ranking

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

## Funciones de desplazamiento

- LAG() → fila anterior
- LEAD() → fila siguiente
