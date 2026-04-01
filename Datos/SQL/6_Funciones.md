# Tipos principales de funciones en SQL

## Funciones agregadas (aggregate)

Operan sobre múltiples filas

```SQL
COUNT(*)   -- contar
SUM(col)   -- suma
AVG(col)   -- promedio
MIN(col)
MAX(col)
```

```SQL
SELECT COUNT(*), AVG(edad)
FROM usuarios;
```

## Funciones escalares

Trabajan sobre una sola fila y devuelven un valor

```SQL
SELECT UPPER(nombre) FROM usuarios;
```

### Texto

```SQL
UPPER()
LOWER()
LENGTH()
```

### Números

```SQL
ROUND()
ABS()
```

### Fechas

```SQL
AGE()
NOW()
```

## Funciones de desplazamiento
