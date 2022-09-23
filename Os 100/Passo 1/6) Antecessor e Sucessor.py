'''Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10 '''

num = int(input("Insira um numero: "))

if num == 0:
    print("O Sucessor de 0 e: \033[0;32m 1 \033[0;0m ")
else:
    somaA = num - 1
    somaS = num + 1
    print("O Antecessor de {} e: \033[0;32m{} \033[0;0m".format(num, somaA))
    print("O Sucessor de {} e: \033[0;32m{} \033[0;0m".format(num, somaS))