from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimiCpf(self):
        print('CPF: ' , self.cpf)
    
    def calculaIMC(self, peso, altura):
        self.altura = altura
        self.peso = peso 
        imc = peso/ (altura * altura) 
        print(f'O IMC da Pesso física é:{imc:.3f}' )
    
    
        
        


