from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade , numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade )
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
       print('Numero de marchas: ' , self.numMarchas)
       print('Bagageiro: ' , self.bagageiro)
        