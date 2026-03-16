# Balanceador de carga

Un balanceador es un intermediario.

Recibe todas las requests y las distribuye entre varios servidores.

Ejemplo:

```
Cliente → Balanceador → Servidor A
                        → Servidor B
                        → Servidor C
```

Su función:

- Distribuir tráfico
- Evitar sobrecargar un solo servidor
- Detectar servidores caídos
- Mejorar disponibilidad

Ejemplos reales:

- NGINX
- HAProxy
- Balanceadores de AWS
