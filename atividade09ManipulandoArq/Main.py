# Construir um algoritmo que permite que o usuário informe uma lista de produtos para serem comprados 
# em um supermercado ( lista de compras). Os nomes dos produtos devem ser salvos em um arquivo 
# de texto e a lista poderá ser modificada sempre que o usuário quiser.

#encoding='utf-8'

import os

lista_produtos = []

menu = ''' \n\n\nMenu
    0-  Finalizar
    1-	Cadastrar produtos
    2 - Salvar em arquivo de texto 
    3 - Modificar no arquivo de texto
Escolha: '''


def cadastar_mercadoria():
    produtos = input('Informe o nome do produto: ')
    lista_produtos.append(produtos)
 
def salvar_txt():
    txt = open("texto01" , "a")
    txt.writelines(lista_produtos)
    txt.close()
    
    txt = open("texto01", "r")
    print(txt.read())

def modificar_txt():
    print('... Produtos cadastrados')
    for produtos in lista_produtos:
        print(produtos)
    if os.path.exists("texto01"):
        os.remove("texto01")
        print('Arquivo removido')
    else: 
        print("Arquivo não encontrado")


while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        print("\nCadastro produtos")
        cadastar_mercadoria()
    elif escolha == '2':
        print("\nProduto da lista salvo em texto")
        salvar_txt()
    elif escolha == '3':
        print("\nProdutos modificados")
        modificar_txt()
