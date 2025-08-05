#calculadora simples

num = []*2
conta = ''

print("--- Calculadora ---")
for i in range(2):
    num.append(float(input("Me diga dois números pra fazer uma conta\n")))

opera = input("Me diga qual a operação que será: (*, /, + ou -)")

if opera == '+':
    conta = num[0] + num[1]
elif opera == '-':
    conta = num[0] - num[1]
elif opera == '/':
    conta = num[0] / num[1]
elif opera == '*':
    conta = num[0] * num[1]
else:
    print("Operação Inválida")

print(conta)
