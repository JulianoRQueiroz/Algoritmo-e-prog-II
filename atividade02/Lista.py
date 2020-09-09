'''
• Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função 
para inserir elementos, uma para imprimir os elementos na ordem que foram inseridos e uma 
função para imprimir os elementos na ordem inversa a que foram inseridos. '''
from elementos import ElementoOrdenado
from elementos import ElmentoInverso

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0 

    def __len__(self):
        return self.tamanho

    def adicionarOrdenado(self, valor1):
        if self.inicio:
            aux = self.inicio
            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = ElementoOrdenado(valor1)
        else:
            self.inicio = ElementoOrdenado(valor1)
        self.tamanho = self.tamanho + 1

    def adicionarInverso(self, valor2):
        if self.inicio:
            aux = self.inicio
            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = ElmentoInverso(valor2)
        else:
            self.inicio = ElmentoInverso(valor2)
        self.tamanho = self.tamanho + 1
    
    def imprimirOrdenado(self):
        aux = self.inicio
        while(aux):
            print(aux.elementos.sort(), '\n')
            aux = aux.proximo
    def imprimirInverso(self):
        aux = self.inicio
        while(aux):
            print(aux.elementos.sort(reversed), '\n')
            aux = aux.proximo