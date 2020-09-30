from Lista import Lista

lista = Lista()

while True:
    e = input('''
    0  - Finlizar
    01 - Adiconar valores
    02 - Imprimir valores
    03 - Imprimir valores ordenados 
    04 - Imprimir valores inversos
    05 - Remover valor
    Escolha: \n
    ''')
    if e == '0':
        break
    if e == '1':
        valor = input("Digite um valor: ")
        lista.adicionar( valor )
    if e == '2':
        lista.imprimir()
    if e == '3':
        lista.imprimirOrdenado(valor)
    if e == '4':
        lista.imprimirInverso()
    if e == '5':
        lista.remover()