''' Atividade Aula01 - Revisão Métodos e Listas
• Construir um algoritmo que contenha 3 listas:

      • Nomes de produtos

      • Preços de cada produto

      • Quantidades de cada produto

• Construir uma função para imprimir um dos produtos da lista
e uma função para retirar um dos produtos das listas'''

lista_produtos = ['televisão']
lista_preco = [2000]
lista_quantidadeDeProdutos = [15]

menu = ''' \n\n\nMenu
    0-  Finalizar
    1-	Cadastrar produtos
    2 - Imprimir um produto 
    3 - Excluir produtos
Escolha: '''


def cadastar_mercadoria():
    produtos = input('Informe o nome do produto: ')
    lista_produtos.append(produtos)
    preco = float(input('Informe o preço do produto: '))
    lista_preco.append(preco)
    quantidadeDeProdutos = int(input('Informe a quantidade de produto: '))
    lista_quantidadeDeProdutos.append(quantidadeDeProdutos)
 

def imprimir_produtos():
    produtoLista = input('Informe o nome do produto: ')
    if produtoLista not in lista_produtos:
        input('-> Produto não consta na lista... [Enter]')
    else:
        print(f'-> O produto consta nossa lista. \n O produto informado é: {produtoLista}')
        
    
def excluir_produtos():
    print('... Produtos cadastrados')
    for produtos in lista_produtos:
        print(produtos)
    
    produtoEscolhido = input('Informe o nome do produto a ser excluído: ')
    if produtoEscolhido in lista_produtos:
        lista_produtos.remove(produtoEscolhido)
        input('-> Produto removido da lista. [Enter] ...')
    else:
        input(' -> Produto não encontra-se na lista')
    

while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        print("\nCadastro produtos")
        cadastar_mercadoria()
    elif escolha == '2':
        print("\nProduto da lista")
        imprimir_produtos()
    elif escolha == '3':
        print("\nExcluir produtos")
        excluir_produtos()