# Construa um algoritmo que possua uma tupla com os números escritos por 
# extenso de “zero” a “nove”. Peça ao usuário para digitar um nome de 0 a 9 e
# retorne a ele o número por extenso, sem usar estruturas condicionais (if e switch).

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

def extenso():
    nome = int(input('Digite um número de 0 a 9: '))
    for n in range(len(tupla)):
        n = tupla[nome]
    print('O número digitado é:' , tupla[nome] )

extenso()


