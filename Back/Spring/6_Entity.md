# Entity

## Id

```Java
@Id
@GeneratedValue(strategy=GenerationType.IDENTITY)

```

### Strategy

```Java
GenerationType.AUTO // Elige la mejor estrategia según la base de datos
GenerationType.IDENTITY // Utiliza autoincremento en la base de datos
GenerationType.SEQUENCE // Utiliza secuencias de bases de datos
GenerationType.TABLE // Usa una tabla especial para generar IDs
```

## Fechas

| Tipo SQL                   | Tipo Java / Spring         | Anotación en JPA | Descripción                                        |
| -------------------------- | -------------------------- | ---------------- | -------------------------------------------------- |
| `DATE`                     | `java.time.LocalDate`      | `@Column`        | Solo fecha (año-mes-día)                           |
| `TIME`                     | `java.time.LocalTime`      | `@Column`        | Solo hora (hora:minuto:segundo)                    |
| `DATETIME` / `TIMESTAMP`   | `java.time.LocalDateTime`  | `@Column`        | Fecha y hora completas                             |
| `TIMESTAMP WITH TIME ZONE` | `java.time.OffsetDateTime` | `@Column`        | Fecha y hora con zona horaria (PostgreSQL, Oracle) |
