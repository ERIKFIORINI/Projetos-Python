letr = ""
qtd_casado = 0
idademaior = 0
qtd_viuva = 0
idadeviuva = 0
mediaviuva = 0
conviventes = 0
qtd_total = 0
qtd_convivente = 0
conta = 0

while letr != "N":
    qtd_total += 1
    idade = int(input("Qual a idade da pessoa?\n"))
    est_civil = input("Qual o estado civil:\nC – casado\nS – solteiro\nV – viúvo\nD – divorciado\nT - convivente\n")
    if est_civil == "C":
        qtd_casado += 1
        
    if idade > idademaior and est_civil == "S":
        idademaior = idade
        
    if est_civil == "V":
        idadeviuva += idade
        qtd_viuva += 1
        
    if est_civil == "T":
        qtd_convivente += 1
        conta = (qtd_convivente * 100) / qtd_total
    
    letr = input("Deseja continuar: S/N \n")
if est_civil == "V":
    mediaviuva = idadeviuva / qtd_viuva
print("---- Relatório ----")
print(f"Quantidade de pessoas casadas:{qtd_casado}")
print(f"A idade da pessoa mais velha solteira é {idademaior} anos")
print(f"A média de idade das pessoas Viúvas é {mediaviuva:.1f} anos")
print(f"A porcentagem de pessoas conviventes em relação a todos é de {conta}%")
