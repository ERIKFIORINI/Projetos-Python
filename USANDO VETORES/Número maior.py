notas = [0]*10
notas_maiores = []

print("Diga a nota de 10 alunos:")
for i in range(10):
    notas[i] = float(input())
for nota in notas:
    if nota > 5:
        notas_maiores.append(nota)
    
print(notas_maiores)
