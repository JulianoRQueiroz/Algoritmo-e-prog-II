# Construa um algoritmo para implementar a classe Retângulo que possui os atributos: altura e largura.
# A classe deve ter os seguintes métodos:
# ○ Método construtor
# ○ Método que calcula a área do retângulo ( altura * largura) e retorna o resultado
# ○ Método que imprime os valores dos atributos da classe.

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcularArea(self):
        return self.altura * self.largura