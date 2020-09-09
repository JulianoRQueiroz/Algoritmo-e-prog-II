from Lista import Lista

lista = Lista()
# print('Tamanho da Lista: ' + str(lista.tamanho))

lista.adicionar(3, 7)
# print('Tamanho da Lista: ' + str(lista.tamanho))

while True:
    e = input('''
    0  - Finlizar
    01 - Adiconar valores
    02 - Imprimir valores ordenados 
    03 - Imprimir valores inversos
    ''')
    if e == '0':
        break
    if e == '1':
        lista.adicionar(input('Digite um valor: '))
    if e == '2':
        lista.imprimiOrdenado()
    if e == '3':
        lista.imprimirInverso()

#     valor1 = input('Digite um valor: ')
#     valor2 = input('Digite um valor: ')

# listaOrdenada.adicionarOrdenado(valor1)
# listaInversa.adicionarInverso(valor2)