''' Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em
R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45. '''

carteira = float(input("Insira quanto de dinheiro voce tem na carteira: "))
dol = carteira / 3.45
print("Com {}R$ na carteira voce podera comprar {:.2f}US$".format(carteira, dol))