# ¿Qué es JPA?

JPA (Java Persistence API) es una especificación que permite trabajar con bases de datos usando objetos Java en lugar de SQL directo.

## Primero: diferencia clave

JPA NO es una librería, es una especificación.

Las implementaciones más comunes son:

- Hibernate (la más usada)
- EclipseLink

En Spring normalmente: Spring Data JPA usa Hibernate internamente

## Qué es Spring Data JPA

Es un módulo de Spring que:

- usa JPA
- crea repositorios automáticamente
- maneja consultas
- maneja transacciones

## Componentes

- Entity
- Repository

## Métodos automáticos

```Java
save()
findById()
findAll()
delete()
count()
```
