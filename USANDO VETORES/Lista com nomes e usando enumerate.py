lista = []

for i in range(5):
    lista.append(input("Me diga nomes:\n"))

print(lista)
qtd_nomes = len(lista)
print(f"Quantidade de Nomes: {qtd_nomes}")
lista.sort()

for i, nome in enumerate(lista, start = 1):
    print(f"{i}: {nome}")
