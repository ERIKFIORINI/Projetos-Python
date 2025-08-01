letr = ""
cont = 0
soma = 0
while letr != "N":
    num = float(input("Diga um número:\n"))
    soma += num
    cont += 1
    letr = input("Deseja continuar: (S/N) ".upper())


media = soma / cont
print(f"A média é: {media:.2f}")
