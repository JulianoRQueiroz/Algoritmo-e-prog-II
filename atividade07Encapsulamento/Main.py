from Pessoa import Pessoa
from Fisica import Fisica


menu = ''' \n\nMenu
    0 - Finalizar
    1 -	Cadastrar Cliente
    2 - Imprimir Dados do Cliente
    3 - Cadastro Pessoa Física
    4 - Imprimir IMC Pessoa Física
    5 - 
    6 -
Escolha: '''


while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
       print(' ---- Cadastro do Cliente --- \n')
       codigo = int(input('Digite o codigo do cliente: '))
       nome = input('Digite nome do cliente: ')
       endereco =  input('Digite o endereco do cliente: ')
       telefone = int(input('Digite o telefone do cliente: '))
       pessoa = Pessoa(codigo, nome, endereco, telefone)
       
    elif escolha == '2':
        print(' ---- Dados do Cliente --- \n')
        pessoa.imprimirNome()
        pessoa.imprimirTelefone()
    elif escolha == '3':
       print(' ---- Cadastro Pessoa Física --- \n')
       cpf = int(input('Digite o cpf do cliente: '))
       fisica = cpf
       idade = int(input('Digite a idade do cliente: '))
       fisica = idade
       peso = float(input('Digite o peso do cliente: '))
       fisica = peso
       altura = float(input('Digite a altura do cliente: '))
       fisica = altura
       fisica = Fisica(codigo, nome, endereco, telefone, cpf, idade, peso, altura)
    elif escolha == '4':
        print(' ---- Dados do Cliente --- \n')
        fisica.imprimiCpf()
        fisica.calculaIMC(peso, altura)
    elif escolha == '5':
      pass
    elif escolha == '6':
        pass
    