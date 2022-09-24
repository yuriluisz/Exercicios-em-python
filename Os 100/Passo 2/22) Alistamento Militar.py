'''Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
situação em relação ao alistamento militar.
- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
alistamento. 
- Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
alistamento. '''

ano = int(input("Insira o seu ano de nascimento: "))

id = 2022 - ano

if id >= 18:
    pas = id - 18
    print("Voce ja Pode se alistar fazem {} anos,".format(pas))
else:
    npas = 18 - id
    print("Voce ainda nao pode se alistar, ainda falta {} anos!".format(npas))