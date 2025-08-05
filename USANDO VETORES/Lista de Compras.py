#Lista de compras

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

lista = []
resp = 0

while resp != '5':

    print("--- Lista de compras ---")
    escolha = (input(('''
1 - Adicionar itens
2 - Ver Itens
3 - Remover Item
4 - Quantos itens tem
5 - Sair
''')))

    
    if escolha == '1':
        limpar_tela()
        qtd_item = int(input("Quantos itens serão?\n"))
        for i in range(qtd_item):
            lista.append(input("Qual o item?\n"))
    
    if escolha == '2':
        limpar_tela()
        print("\nLista")
        for i, lista in enumerate(lista, start=1):
            print(f"{i}. {lista}")
    print('\n')
    
    if escolha == '3':
        qtd_item = int(input("Quantos itens quer remover?"))
        for i in range(qtd_item):
            item = input("Qual item quer remover?")
            lista.remove(item)
            print(f"{item} Removido com sucesso!")
    
    if escolha == '4':
        print(f"Total de itens é {len(lista)}")
        
        
    elif escolha == '5':
        resp = '5
