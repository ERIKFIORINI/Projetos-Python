import random
num = [0]*10
pares = []
impar = []

for i in range(10):
    num[i] = random.randint(1, 10)
for numeros in num:
    if numeros % 2 == 0:
        pares.append(numeros)
    if numeros % 2 != 0:
        impar.append(numeros)

impar.sort()