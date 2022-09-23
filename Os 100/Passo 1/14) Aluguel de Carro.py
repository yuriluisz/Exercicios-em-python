'''A locadora de carros precisa da sua ajuda para cobrar seus serviços.
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço
total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado. '''

dias = int(input("Insira o numero de dias em que voce alugou o carro: "))
km = float(input("Insira o KM rodado durando o aluguel do carro: "))

Diaria = dias * 90
kmRodado = km * 0.20
total = Diaria + kmRodado

print("Com um aluguel de {} dias e com {}Km rodados, o custo total sera de {:.2f}R$".format(dias, km, total))