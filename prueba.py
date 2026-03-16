print(20*"=", "Listas", 20*"=")

lista = [1, 2, 3, 4]
print(type(lista))

## Inserción
lista.append(5)
print(lista)
## Borrado
print(lista.pop(3))
print (lista)
## Actualización
lista.insert(1, 0)
print(lista.insert(1, 0))
print(lista)
## Ordenación
print(sorted(lista))
print("Sin ordenar", lista)
lista.sort()
print("Ordenada", lista)
for i in lista:
    print("lista: ", i)
    
print(20*"=", "Tuplas", 20*"=")

tupla = (1, 2, 2,3, 2, "1", "2")
print(type(tupla), tupla)
print(tupla.count(2))
print(tupla.count("2"))
print(tupla.index(1))

for i in tupla:
    print("tupla: ", i)

## Inserción
# No es posible
## Borrado
# No es posible
## Actualización
# No es posible
## Ordenación
tupla = (1, 2, 2, 3, 2)

print(sorted(tupla))

print(20*"=", "Sets", 20*"=")
tupla = (1111, 3, 2, 2, 3, 5, 4, 22222222, 10, 9, 8)
print(tupla)
conjunto = set(tupla)
print(conjunto)
## Inserción
conjunto.add(12)
print(conjunto)
## Borrado
conjunto.remove(12)
print(conjunto)
## Actualización

## Ordenación
print(sorted(conjunto))
print(20*"=", "Diccionario", 20*"=")
diccionario = {"mesa": "madera"}
print(diccionario)
## Inserción
diccionario["mesa"] = "roble"
diccionario["computador"] = "hp"
print(diccionario)
## Borrado
print(diccionario.pop("mesa"))
print(diccionario)
## Actualización
diccionario.update({"sofa":"tela"})
print(diccionario)
## Ordenación

# Generadores

## Inserción
## Borrado
## Actualización