#Elabore um algoritmo que leia valores inteiros para um vetor com 10 números e 
calcule a diferença entre o maior e o menor elemento existente.

num = [0]*3
print("Diga 3 números:")
for i in range(3):
    num[i] = int(input())
    

menor = min(num)
alto = max(num)
dife = alto - menor
print(f"O maior é {alto}, menor {menor} e a diferença é {dife}")
