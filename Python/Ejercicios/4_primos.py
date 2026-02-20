def es_primo(x)->bool:
    if x < 2:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

for y in range (2,60):
    if es_primo(y):
        print(y)
