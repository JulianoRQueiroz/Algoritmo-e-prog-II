# Construa um algoritmo que peça ao usuário para informar o nome, a nota01 e a nota02 
# de um aluno. Guarde estas informações em um dicionário. Após, calcule a nota final
#  deste aluno [(nota01 + nota02) /2] e adicione ao dicionário. Ao final, 
# imprima todos os dados do dicionário.

dicionario = {}
lista = []

def cadastro():
    nomeAluno = input('Informe o nome do aluno: ')
    dicionario['Nome'] = nomeAluno

def notas():
    nota01 = float(input('Informe a nota01: '))
    lista.append(nota01)
    nota02 = float(input('Informe a nota02: '))
    lista.append(nota02)
    dicionario['Notas'] = lista


def calculoNota():
    notas = lista
    notaFinal = ( notas[0] + notas[1] ) / 2
    print('A nota final do aluno é: \n', notaFinal)


def imprimir():
    dicionario['Nota Final'] = calculoNota()
    print(dicionario)

menu = ''' \n\n\nMenu
    0 -  Finalizar
    1 -	Cadastrar alunos
    2 - Cadastrar notas
    3 - Cálculo notas
    4 - Imprimir dicionário
Escolha: '''


while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        print("\nCadastro alunos")
        cadastro()
    elif escolha == '2':
        print("\nNotas")
        notas()
    elif escolha == '3':
        print("\nCálculo da Notas")
        calculoNota()
    elif escolha == '4':
        print('\n Impressão dicionário')
        imprimir()

