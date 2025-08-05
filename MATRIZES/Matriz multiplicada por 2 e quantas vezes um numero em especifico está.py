#Matriz multiplicada por 2 e quantas vezes um numero em especifico está

import random
import numpy as np

matriz = []
valor = []
numero = 0
zero = 0
op = []

for lin in range(3):
    linha = []
    for col in range(3):
        valor = int(input("Diga os valores pra colocar na matriz:"))
        linha.append(valor)
    matriz.append(linha)
    
for lin in range(3):
    for col in range(3):
        print(f"{matriz[lin][col]:4}", end=' ')
    op = matriz[:] * 2
    print()

quantidade = sum(linha.count(numero) for linha in matriz)
print(f"A quantidade de 0 na matriz é de: {quantidade}")

op = [[x * 2 for x in lin] for lin in matriz]

print("\nMatriz com valores multiplicados por 2:")
for lin in range(3):
    for col in range(3):
        print(f"{op[lin][col]:4}", end=' ')
    print()
