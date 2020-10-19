from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

menu = ''' \n\nMenu
    0 - Finalizar
    1 -	Cadastrar  dados do aluno
    2 - Imprimir cadastro do aluno
    3 - Cadastar ano do aluno no Ensino médio
    4 - Imprimir dados do Aluno do Ensino medio
    5 - Cadastar ano do Aluno na Graduação
    6 - Imprimir dados do Aluno da Graduação
Escolha: '''


while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
       nome = input('Digite o nome do aluno: ')
       matricula = int(input('Digite o número da matricula: '))
       codigo =  int(input('Digite o código do aluno: '))
       aluno = Aluno(nome, codigo, matricula)
       
    elif escolha == '2':
        print(' ---- Dados do Aluno --- \n')
        aluno.imprimir()
    elif escolha == '3':
       ano = input('Informe o ano do aluno: ')
       alunoEnsinoMedio = ano
       alunoEnsinoMedio = AlunoEnsinoMedio(nome, codigo, matricula, ano)
    elif escolha == '4':
        print(' ---- Dados do Aluno do Ensino Médio --- \n')
        alunoEnsinoMedio.imprimirEnsinoMedio()
    elif escolha == '5':
       semestre = input('Informe o semestre do aluno: ')
       alunoGraduacao = semestre
       alunoGraduacao = AlunoGraduacao(nome, codigo, matricula, semestre)
    elif escolha == '6':
        print(' ---- Dados do Aluno da Graduação --- \n')
        alunoGraduacao.imprimirGraduacao()
    