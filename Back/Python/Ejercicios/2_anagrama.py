
palabra = "Anita lava la tina"
palabra = "".join(palabra.lower().split())
inversa = ""

for x in palabra:
    inversa=x+inversa
print(palabra, inversa)

if (palabra==inversa):
    print ("Es anagrama")
else:
    print ("No es anagrama")