# Índices

Un índice en una base de datos es una estructura de datos que mejora la velocidad de las operaciones de recuperación de datos a costa de espacio en disco y un mantenimiento extra en las escrituras.

Su funcionamiento es análogo al índice de un libro: en lugar de hojear todo el libro (la tabla completa) para encontrar un tema específico, consultas el índice, que te dice exactamente en qué página (la ubicación en disco) está ese tema. Esto permite un acceso extremadamente rápido a los registros.

Sin embargo, los índices no son gratis. Cada vez que insertas, actualizas o eliminas una fila en una tabla indexada, el índice también debe actualizarse, lo que puede ralentizar estas operaciones. Además, ocupan un espacio de almacenamiento considerable.

# Cuando no usar índices

La decisión de crear índices en tablas con muchas escrituras (inserciones, actualizaciones, eliminaciones) es un equilibrio clásico entre rendimiento de lectura y rendimiento de escritura.

Tablas con muchas lecturas y pocas escrituras: Los índices son casi siempre beneficiosos. Por ejemplo, un catálogo de productos que se lee constantemente pero se actualiza pocas veces al día.

Tablas con muchas escrituras y pocas lecturas: Puede que los índices no merezcan la pena, ya que el overhead ralentizaría las escrituras sin aportar un beneficio significativo.

Tablas con equilibrio (típico en aplicaciones OLTP): Se usan índices, pero de forma estratégica. Se indexan solo las columnas que realmente se utilizan en las búsquedas, joins y filtros frecuentes. Un índice innecesario es un lastre.

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

# Tipos de índices

## Árbol B

El predeterminado y más versátil. Ideal para la mayoría de los casos. Perfecto para consultas de igualdad y rango, y para ordenar resultados.

Un árbol b es un árbol de búsqueda balanceado. Cada nodo puede tener múltiples claves y múltiples hijos. Todos los nodos hoja están al mismo nivel.

### Insersión

Si el el nodo está lleno, se divide.
Antes de insertar, las claves se redistribuyen y la clave central sube al nodo padre.

## Hash

Optimizado para consultas de igualdad simples. Almacena un código hash del valor, lo que hace las búsquedas por = muy rápidas. No sirve para rangos.

## GIN

Especialista en datos compuestos donde un campo puede contener múltiples valores. Ideal para arrays, documentos jsonb y búsqueda de texto completo.

## GiST

Ofrecen una infraestructura para tipos de datos complejos y búsquedas personalizadas. Se usan para datos geométricos/espaciales (puntos, polígonos, etc.) y búsquedas de "nodos más cercanos".

## BRIN (Block Range INdex)

El campeón del espacio. Almacena resúmenes (mínimo y máximo) para rangos de bloques de la tabla. Es muy eficiente en tablas enormes donde los datos están fuertemente correlacionados con el orden físico (ej. una columna de timestamp que siempre aumenta).

## Índices Multicolumna

Indexan varias columnas para consultas que filtran por todas ellas

## Índices Parciales:

Solo indexan un subconjunto de filas de la tabla (por ejemplo, CREATE INDEX ... WHERE activo = true). Son más pequeños y rápidos
