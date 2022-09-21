'''Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2metros quadrados. '''

Largura = float(input("Insira a Largura da Parede: "))
Altura = float(input("Insira a Altura da Parede: "))

Area = Largura * Altura
Tinta = Area / 2

print("Para uma Area de {} metros, sera nescessario {} Litros de tinta.".format(Area, Tinta))