lista1 = []
lista2 = []

for i in range(3):
    lista1.append(int(input("Lista 1: diga números:\n")))
for i in range(3):
    lista2.append(int(input("Lista 2: diga números:\n")))


print(lista1)
print(lista2)


lista1.extend(lista2)
media = sum(lista1) / len(lista1)
lista1.sort()
print(lista1)
print(f"A média é {media:.2f}.")
