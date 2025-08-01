letr = ""
num = int(input("Me diga um número:"))

while letr != "N":
    num = num * 2
    print(f"O dobro do seu número é: {num}")
    
    letr = input("Deseja continuar? S/N\n")