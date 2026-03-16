# Primero: ¿Qué es un JOIN?

Un JOIN sirve para combinar filas de dos tablas usando una columna en común.

| Tipo  | Devuelve                       |
| ----- | ------------------------------ |
| INNER | Solo coincidencias             |
| LEFT  | Todo izquierda + coincidencias |
| RIGHT | Todo derecha + coincidencias   |
| FULL  | Todo de ambas                  |
| CROSS | Todo con todo                  |

# Índice

Un índice en base de datos es una estructura que permite buscar datos más rápido.

Cómo funciona por dentro:

La mayoría de bases usan algo llamado: B-Tree (árbol balanceado).

Los valores están organizados de forma ordenada. Permite búsqueda rápida (logarítmica)

## En qué columnas se indexa

Normalmente:

- Primary keys (automático)
- Foreign keys
- Campos que usas en WHERE
- Campos usados en JOIN
- Campos usados en ORDER BY

| Sin índice              | Con índice          |
| ----------------------- | ------------------- |
| Full scan               | Búsqueda rápida     |
| Lento en tablas grandes | Mucho más eficiente |
| Menos espacio           | Más espacio         |

## ACID

A: Atomicidad - Una transacción ocurre completamente o no ocurre.
C: Consistencia - La base pasa de un estado válido a otro estado válido.
I: Aislamiento - Transacciones concurrentes no se interfieren incorrectamente.
D: Durabilidad - Una vez confirmado el cambio, no se pierde aunque el sistema falle.

Esos principios son garantizados por motores como PostgreSQL.
La consistencia se logra con restricciones estructurales como primary key, foreing key, unique, check y not null.

| Propiedad    | Cómo se implementa               |
| ------------ | -------------------------------- |
| Atomicidad   | Logs + rollback                  |
| Consistencia | Constraints + reglas del esquema |
| Aislamiento  | Locks + MVCC                     |
| Durabilidad  | WAL + escritura en disco         |
