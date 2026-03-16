# Formas de programar

## Según paradigma (como expresas el código)

### Programación imperativa

Le dices paso a paso cómo hacer algo.

Ejemplo clásico en Python:

```Python
for fila in filas:
    if fila.edad > 18:
        ...
```

Le estás diciendo exactamente qué hacer en cada paso.

### Programación declarativa

No dices cómo hacerlo. Dices qué resultado quieres.

Ejemplo tipo SQL:

```Python
SELECT nombre
FROM personas
WHERE edad > 18
```

## Según modelo de ejecución (concurrencia)

🔹 Síncrono

Bloquea mientras espera.

🔹 Asíncrono

No bloquea mientras espera.

## Según arquitectura

- Monolito
- Microservicios
- Cliente-servidor
- Serverless
- Hexagonal

## Según tipado

Según tipado

- Tipado estático
- Tipado dinámico
