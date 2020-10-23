from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, qtdFuncionario):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual
        self.qtdFuncionario = qtdFuncionario

    def imprimiCnpj(self):
        print('CNPJ: ' , self.cnpj)
    
    def emitirNotaFiscal(self):
       print('Codigo: ', self.codigo)
       print('Nome: ', self.nome)
       print('CNPJ: ' , self.cnpj)
       print('Número da inscrição estadual: ' , self.inscricaoEstadual)
       print('Quantidade de funcionários: ' , self.qtdFuncionario)