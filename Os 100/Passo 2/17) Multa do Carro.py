''' Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba 
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida. '''

vel = int(input("Insira a velocidade em que o carro estava: "))

if vel > 85:
    acvel = (vel - 85) * 5
    velac = vel - 85
    print("A multa que o carro ira levar por estar {}Km/h acima do limite de velocida de sera de \033[0;31mR${}\033[0;0m! ".format(velac, acvel))
else:
    print("O carro nao ultrapassou o limite de velocidade.")
