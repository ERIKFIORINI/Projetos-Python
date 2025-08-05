#1. Mostrar a matriz
#2. Mostrar apenas os valores pares
#3. Mostrar a soma dos elementos de cada linha
#4. Mostrar a média de cada coluna
#5. Sair

import random
import numpy as np

matriz = []
matriz = np.random.randint(0, 50,(4, 4))
op = -1

while op != 5:
    op = int(input("\nQual opção deseja?"))
    
    match op:
        case 1:
            for linha in matriz:
                print(' '.join(f"{num:4}" for num in linha))
                
        case 2:
            print("Os números pares são:")
            for linha in matriz:
                    for num in linha:
                        if num % 2 == 0:
                            print(f"{num}", end=' ')
        
        case 3:
            print("A soma das linhas é respectivamente:")
            somas = []
            somalinha = 0
            for i in range(4):
                somalinha = sum(matriz[i])
                somas.append(somalinha)
            print(somas)
            
        case 4:
            somatotal = []
            mediacolunas = []
            media = 0
            for i in range(4):
                somacoluna = 0
                for j in range(4):
                    somacoluna += matriz[j][i]
                somatotal.append(somacoluna)
            
            for i in range(4):
                media += somatotal[i] / 4
                mediacolunas.append(media)
            print(f"{mediacolunas}")
        
        case 5:
            print("Saindo..")
        
        case _:
            print("Inválido")
