# Join

Primero: ¿Qué es un JOIN?

Un JOIN sirve para combinar filas de dos tablas usando una columna en común.

| Tipo  | Devuelve                       |
| ----- | ------------------------------ |
| INNER | Solo coincidencias             |
| LEFT  | Todo izquierda + coincidencias |
| RIGHT | Todo derecha + coincidencias   |
| FULL  | Todo de ambas                  |
| CROSS | Todo con todo                  |

## Inner Join

Devuelve solo coincidencias. Solo filas donde ambas tablas tienen relación

```SQL
SELECT u.nombre, o.total
FROM usuarios u
JOIN ordenes o
ON u.id = o.usuario_id;
```

## Left Join

Devuelve todo de la izquierda + coincidencias

```SQL
SELECT u.nombre, o.total
FROM usuarios u
LEFT JOIN ordenes o
ON u.id = o.usuario_id;
```

Quiero todos los usuarios, tengan o no órdenes. Si no hay coincidencia → NULL

## Right Join

Igual que LEFT, pero al revés

```SQL
SELECT u.nombre, o.total
FROM usuarios u
RIGHT JOIN ordenes o
ON u.id = o.usuario_id;
```

## FULL JOIN

Devuelve todo

```SQL
SELECT u.nombre, o.total
FROM usuarios u
FULL JOIN ordenes o
ON u.id = o.usuario_id;
```
