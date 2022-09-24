''' Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
BISSEXTO. '''

from calendar import isleap

ano = int(input("Insira o ano em que deseja saber se e bissexto ou nao: "))

if isleap(ano):
    print("O ano de {} e bissexto!".format(ano))
else:
    print("O ano de {} nao e bissexto!".format(ano))