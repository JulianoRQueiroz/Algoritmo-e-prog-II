from Retangulo import Retangulo

largura = int(input('Informe a largura: ')) 
altura = int(input('Informe o comprimento: ')) 

retangulo = Retangulo(largura, altura)
area = retangulo.calcularArea()

print(" O caluculo da área do retangulo é: " + str(area))
