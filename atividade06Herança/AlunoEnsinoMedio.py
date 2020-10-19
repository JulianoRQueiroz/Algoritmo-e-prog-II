from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome, codigo,matricula, ano):
        Aluno.__init__(self, nome, codigo, matricula)
        self.ano = ano

    def imprimirEnsinoMedio(self):
        print('Nome: ' , self.nome)
        print('Código: ', self.codigo)
        print('Matrícula: ', self.matricula)
        print('Ano: ', self.ano)
