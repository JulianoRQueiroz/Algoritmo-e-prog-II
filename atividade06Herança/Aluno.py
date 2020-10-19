#Construa um algoritimo para implementar a classe Aluno (código, nome, matrícula)
# A classe Aluno possui duas subclasses a classe AluEnsinoMedio(ano) e 
# AlunoGraduacao(semestre). As três classes possuem o método construtor e 
# também o método imprimir(), que imprime na tela os valores de todos os atributos
# da sua classe.

class Aluno:
    def __init__(self,nome,codigo, matricula):
        self.nome = nome
        self.codigo = codigo
        self.matricula = matricula
    
    def imprimir(self):
        print('Nome: ' , self.nome)
        print('Código: ', self.codigo)
        print('Matrícula: ', self.matricula)

    