# Construa um algoritmo para implementar a classe Retângulo que possui os atributos: altura e largura.
# A classe deve ter os seguintes métodos:
# ○ Método construtor
# ○ Método que calcula a área do retângulo ( altura * largura) e retorna o resultado
# ○ Método que imprime os valores dos atributos da classe.

class Retangulo:
    def __init__(self):
        self.altura = None
        self.largura = None
    
    def altura(self, altura):
        altura = self.altura(altura) 

    def altura(self, largura):
        largura = self.largura(largura)

    def calculaArea(self, altura, largura):
        calculaArea = altura * largura
        return calculaArea

while True:
    e = input('''
    0  - Finlizar
    01 - Adicionar altura
    02 - Adicionar largura
    03 - Calaculo do retângulo
    Escolha: \n
    ''')
    if e == '0':
        break
    if e == '1':
        altura = float(input("Digite um valor para altura: "))
        Retangulo.altura(altura)
    if e == '2':
        largura = float(input("Digite um valor para largura: "))
        Retangulo.largura(altura)
    if e == '3':
        Retangulo.calculaArea()

resultado = Retangulo()

