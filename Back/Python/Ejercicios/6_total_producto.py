ventas = [
    ("camara", 2),
    ("microfono", 3),
    ("camara", 1)
]

# Tengo una lista de productos vendidos y quiero calcular el total por producto.

total_por_producto = {}

for producto, valor in ventas:
    if producto not in total_por_producto:
        total_por_producto[producto] = 0
    total_por_producto[producto] += valor
    
print (total_por_producto)