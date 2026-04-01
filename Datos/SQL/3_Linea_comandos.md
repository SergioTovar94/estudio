# PSQL

psql es el cliente de línea de comandos para interactuar con la base de datos.

## Qué permite hacer

- Ejecutar SQL
- Administrar bases de datos
- Automatizar tareas
- Ver estructura (tablas, índices, etc.)

## Conexión

psql -U usuario -d basedatos

| Parámetro | Significado   |
| --------- | ------------- |
| `-U`      | Usuario       |
| `-d`      | Base de datos |
| `-h`      | Host          |
| `-p`      | Puerto        |

## Metacomandos PSQL

Son comandos propios de PSQL

## Comandos básicos

## Backup

Generar backup

```SQL
pg_dump -U postgres mi_db > backup.sql
```

Restaurar

```SQL
psql -U postgres -d mi_db < backup.sql
```
