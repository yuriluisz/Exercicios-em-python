'''Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
dela e depois mostre se ela pode ou não votar. '''

idade = int(input("Insira sua idade: "))

if idade >= 16:
    print("\033[0;32mVoce ja pode votar!\033[0;0m")
else:
    id = 16 - idade
    print("Voce ainda nao pode votar pois ainda falta \033[0;31m{}\033[0;0m anos!".format(id))