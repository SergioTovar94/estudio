# Conceptos

## Cliente vs Servidor

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
