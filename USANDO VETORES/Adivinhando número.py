#O computador deve sortear um número de 1 a 10, e o usuário deve tentar adivinhar.
#Dê dicas se o número estiver muito alto ou muito baixo, até que ele acerte.

import random
resp = ()
num = random.randint(1, 10)
print("Adivinhe o número de 1 á 10")

while resp != num:
    resp = int(input())
    if resp < num:
        print("Um pouco pra cima")
    elif resp > num:
        print("Um pouco pra baixo")
    else:
        print("Na mosca!")
