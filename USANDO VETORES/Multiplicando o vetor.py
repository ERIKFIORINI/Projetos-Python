#Desenvolva um algoritmo que leia um conjunto de 15 números inteiros e armazene-os em um vetor A. 
Após a leitura dos dados o algoritmo deve multiplicar todos os números do vetor A por 3 
e armazenar o resultado em um segundo vetor B. No final, mostrar o conteúdo dos 2 vetores.

contage = 0
num_multi = []
num = [0]*3
print("Diga 3 números:")
for i in range(3):
    contage +=1
    num[i] = int(input(f"{contage}: "))
for numeros in num:    
    if numeros != num:
        num_multi.append(numeros * 3)

print(f"Seus números é {num}")
print(f"O triplo dos números é: {num_multi}")
