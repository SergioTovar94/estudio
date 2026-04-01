# CTEs

Un CTE (Common Table Expression) es como una tabla temporal con nombre que defines dentro de una consulta SQL para hacerla más clara, organizada y fácil de mantener.

Se crea usando la palabra clave WITH.

```SQL
WITH clientes_activos AS (
    SELECT *
    FROM clientes
    WHERE activo = true
)
SELECT *
FROM clientes_activos;
```

- clientes_activos es el CTE
- No existe en la base de datos, solo vive durante la consulta

## ¿Por qué usar CTE?

- Mejor legibilidad: separa lógica
- Reutilización dentro de la misma consulta
