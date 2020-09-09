'''
• Construa o algoritmo em Python de uma lista duplamente encadeada que possui uma função 
para inserir elementos, uma para imprimir os elementos na ordem que foram inseridos e uma 
função para imprimir os elementos na ordem inversa a que foram inseridos. '''

class Elemento:
    def __init__(self, valor1, valor2):
        self.elementosOrdenados = valor1
        self.elementosInversos = valor2
        self.proximo = None

   


    