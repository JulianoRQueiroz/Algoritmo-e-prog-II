'''
• Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função 
para inserir elementos, uma para imprimir os elementos na ordem que foram inseridos e uma 
função para imprimir os elementos na ordem inversa a que foram inseridos. '''
from Elementos import Elemento

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = 0 
        self.tamanho = 0 

    def adicionar(self, valor):
        valor = Elemento(valor)
        if self.tamanho == 0:
            self.inicio = valor
            self.fim = valor
        else: 
            self.fim.proximo = valor 
            self.fim = valor
        self.tamanho += 1

    def imprimir(self):
        texto = ""
        if self.tamanho == 0:
            texto = "Não possui elementos!"
        else:
            aux = self.inicio
            while(aux):
                texto = texto + str(aux.elementos) + " - "
                aux = aux.proximo  
        print( texto )
    
    def imprimirOrdenado(self, valor):
        valor = Elemento(valor)
        if self.tamanho == 0:
            self.inicio = valor
            self.fim = valor
        else:
            while():
                valor = ''.join(sorted()) + ' - '
                aux = aux.proximo 
        print(valor)
        
    def imprimirInverso(self):
        aux = self.inicio
        valor = Elemento(valor)
        if self.tamanho == 0:
            self.inicio = valor
            self.fim = valor
        else:
            while():
                valor = ''.join(sorted(reversed)) + ' - '
                aux = aux.proximo 
        print(valor)
    
    def remover(self):
        if self.tamanho == 0:
            print("Elementos vazio!")
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1