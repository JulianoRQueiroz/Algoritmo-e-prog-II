class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.telefone = telefone

    def imprimirNome(self):
        print('Nome: ' , self.nome)
    
    def imprimirTelefone(self):
        print('Telefone: ' , self.telefone)