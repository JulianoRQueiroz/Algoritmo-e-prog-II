'''
• Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função 
para inserir elementos, uma para imprimir os elementos na ordem que foram inseridos e uma 
função para imprimir os elementos na ordem inversa a que foram inseridos. '''

class ElementoOrdenado:
    def __init__(self, valor1):
        self.elementos = valor1
        self.proximo = None

class ElmentoInverso:
    def __init__(self, valor2):
        self.elementos = valor2
        self.proximo = None