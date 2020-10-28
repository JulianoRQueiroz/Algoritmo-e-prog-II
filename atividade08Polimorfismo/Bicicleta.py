from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade , numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade )
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
    #    print('Marca: ', self.marca)
    #    print('qtdRodas: ', self.qtdRodas)
    #    print('Modelo: ' , self.modelp)
    #    print('Velocidade: ' , self.velocidade)
       print('Numero de marchas: ' , self.numMarchas)
       print('Bagageiro: ' , self.bagageiro)
        