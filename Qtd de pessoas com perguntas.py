cont = 0
qtd_m = 0
qtd_f = 0
qtd_idade = 0
somaidade = 0
mediaidade = 0

qtd_pessoa = int(input("Quantas pessoas serão avaliadas?\n"))
while cont < qtd_pessoa:
    cont += 1
    idade = int(input("Qual a idade da pessoa?\n"))
    if idade > 0:
        qtd_idade += 1
    somaidade += idade
    mediaidade = somaidade / qtd_idade
    sexo = input("M - Masculino | F - Feminino\n")
    if sexo == "F":
        qtd_f += 1
    
    if sexo == "M" and idade >= 15 and idade <= 20:
        qtd_m += 1
        
print("---- Relatório ----")
print(f"A média de idade é {mediaidade:.1f} anos.")
print(f"A quantidade de pessoas do sexo feminino é {qtd_f} pessoas.")
print(f"Pessoas masculinas com idade entre 15 a 20 anos é {qtd_m} pessoas")