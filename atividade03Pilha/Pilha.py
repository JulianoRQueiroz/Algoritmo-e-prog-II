# Construa agora um algoritmo para implementação de um Pilha. Lembrando que na Pilha o último 
# elemento adicionado, será o primeiro elemento removido.

from No import No

class Pilha:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def adicionar(self, dado):
        no = No(dado)

        if self.tamanho == 0:
            self.inicio = no
            self.fim = no 
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def imprimir(self):
        texto = ""
        if self.tamanho == 0:
            texto = "Pilha fazia"
        else:
            aux = self.inicio 
            while(aux):
                texto = texto + str(aux.dado) + " - "
                aux = aux.proximo
                
            print(texto)

    def remover(self):
        if self.inicio != None:
            assert self.inicio, "Impossível remover valor de pilha vazia."
            self.inicio = self.inicio.proximo

       



