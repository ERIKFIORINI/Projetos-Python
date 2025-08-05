#Elabore um algoritmo que leia valores inteiros para um vetor com 10 números e calcule a diferença 
entre as posições que maior e o menor elemento existentes ocupam.

num = [0]*5
print("Diga 5 números:")
for i in range(5):
    num[i] = int(input())
    
menor = min(num)
maior = max(num)
dife = maior - menor
posicao_maior = num.index(maior)
posicao_menor = num.index(menor)
difere_posicao = posicao_maior - posicao_menor
print(f"O maior é {maior}, menor {menor} e a diferença é {dife}")
print(f"A diferença de posições do maior pro menor é de {difere_posicao}")
