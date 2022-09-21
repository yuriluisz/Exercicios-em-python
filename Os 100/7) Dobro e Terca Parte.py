'''Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
sua terça parte.
Ex:
Digite um número: 3.5
O dobro de 3.5 é 7.0
A terça parte de 3.5 é 1.16666 '''

num = float(input("Insira um numero qualquer: "))

dobro = num * 2
tpart = num / 3

print("O dobro do numero escolhido e: {}".format(dobro))
print("A terca parte do numero escolhido e: {:.3f}".format(tpart))