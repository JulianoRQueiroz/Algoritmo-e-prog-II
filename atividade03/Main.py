# Construa agora um algoritmo para implementação de um Pilha. Lembrando que na Pilha o último 
# elemento adicionado, será o primeiro elemento removido.

from Pilha import Pilha

pilha = Pilha()

while True:
    e = input('''
    0  - Finlizar programa
    01 - Adicionar valores na pilha
    02 - Imprimir valores da pilha
    03 - Remover ultimo valor da pilha
    Escolha: \n
    ''')
    if e == '0':
        break
    if e == '1':
        valor = input("Digite um valor: ")
        pilha.adicionar( valor )
    if e == '2':
        pilha.imprimir()
    if e == '3':
        pilha.remover()
        print('-> Ultimo valor removido.')

        

