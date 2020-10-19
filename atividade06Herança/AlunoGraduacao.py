from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, nome, codigo, matricula, semestre):
        Aluno.__init__(self, nome, codigo, matricula)
        self.semestre = semestre

    def imprimirGraduacao(self):
        print('Nome: ' , self.nome)
        print('Código: ', self.codigo)
        print('Matrícula: ', self.matricula)
        print('Semestre: ', self.semestre)