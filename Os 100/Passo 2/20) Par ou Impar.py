''' Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou 
ÍMPAR'''

num = int(input("Insira um numero para saber se ele e impar ou par: "))

ip = num % 2

if num == 0:
    print("O numero inserido e PAR!")
else:
    print("O numero inserido e IMPAR!")