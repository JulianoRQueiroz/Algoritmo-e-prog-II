from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel

menu = ''' \n\nMenu
    Escolha um tipo de Veículo
    0 - DADOS DO VEICULO
    1 - BICICLETA
    2 - AUTOMOVEL
    2 - MOTO
    3 - CARRO
    4 - IMPRIMIR INFORMAÇÕES DO VEICULO
Escolha: '''

   

while True:
    escolha = input(menu)
    if escolha == '0':
        marca = input('Informe a marca do veículo: ')
        qtdRodas = int(input('Informe a quantidade de rodas do Veículo: '))
        modelo = input('Informe o modelo do veículo: ')
        velocidade = float(input('Informe a velocidade do veículo: '))
        veiculo = Veiculo(marca, qtdRodas,modelo, velocidade)
    elif escolha == '1':
        numMarchas = int(input('Informe o número de marchas: '))
        bicileta = numMarchas
        bagageiro =  input('Possui bagageiro (S/N): ')
        bicileta = bagageiro
        bicileta = Bicicleta(marca, qtdRodas, modelo, velocidade,numMarchas, bagageiro)
    elif escolha == '4':  
        bicileta.imprimirInformacoes()
    
       