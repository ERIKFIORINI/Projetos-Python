letr = "S"
qtd_total = 0
qtd_1 = 0
qtd_2 = 0
qtd_3 = 0
qtd_idade = 0
mediaidade = 0
ensino1 = 0
ensino2 = 0
ensino3 = 0
conta1 = 0
conta2 = 0
conta3 = 0

while letr != "N":
    qtd_total += 1
    canal = input("Canal de TV que assiste mais: 1-Globo, 2-SporTV, 3-Outra.\n")
    stre = input("Canal de streaming que assiste mais: 1-Netflix, 2-Disney, 3-Outra.\n")
    idade = int(input("Qual a sua idade?\n"))
    nivel_inst = input("Nível de instrução: 1 – Ensino fundamental, 2- Ensino médio, 3- Ensino superior\n")
    
    if canal == "1":
        qtd_1 += 1
    if canal == "2":
        idadesport =+ idade
        qtd_idade += 1
        qtd_2 += 1
    if canal == "3":
        qtd_3 += 1
        
    if nivel_inst == "1":
        ensino1 += 1
    if nivel_inst == "2":
        ensino2 += 1
    if nivel_inst == "3":
        ensino3 += 1
        
    letr = input("Deseja continuar? S/N ").upper()
print("---- Relatório ----")
if qtd_1 > qtd_2 and qtd_1 > qtd_3:
    print("O canal mais assisto é a Globo")
elif qtd_2 > qtd_1 and qtd_2 > qtd_3:
    print("O canal mais assistido é SporTV")
else:
    print("Outro canal é mais assistido")

if qtd_2 > 0:
    mediaidade = idadesport / qtd_idade    
    print(f"A média de idade que assitem SporTV é de {mediaidade} anos")
    
if ensino1 > 0:
    conta1 = (ensino1 * 100) / qtd_total
    print(f"Percentual de Pessoas com Ensino Fundamental é {conta1:.2f}%")
if ensino2 > 0:
    conta2 = (ensino2 * 100) / qtd_total
    print(f"Percentual de Pessoas com Ensino Médio é {conta2:.2f}%")
if ensino3 > 0:
    conta3 = (ensino3 * 100) / qtd_total
    print(f"Percentual de Pessoas com Ensino Superior é {conta3:.2f}%")