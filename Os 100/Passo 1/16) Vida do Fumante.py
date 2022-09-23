'''Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos
ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro.
Calcule quantos dias de vida um fumante perderá e exiba o total em dias. '''

cigarros = int(input("Insira quantos cigarros voce costuma fumar por dia: "))
anos = int(input("Insira a quantos anos voce fuma: "))

cano = (cigarros * 365)
cjf = cano * anos
perdeu = cjf * 10

perdido = perdeu / 1440

print("Voce perdera \033[0;31m{}\033[0;0m dias e \033[0;31m{:.2f}\033[0;0m minutos de vida!".format(anos, perdido))