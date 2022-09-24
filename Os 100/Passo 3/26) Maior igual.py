'''Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
na tela uma das mensagens abaixo: - O primeiro valor é o maior 
- O segundo valor é o maior 
- Não existe valor maior, os dois são iguais '''

n1 = float(input("Insira o primeiro numero: "))
n2 = float(input("Insira o segundo numero: "))

dif = n1 - n2

if dif > 0:
    print("- O primeiro numero e maior.")
    print("- O segundo numero e menor.")
elif dif < 0:
    print("- O primeiro numero e menor.")
    print("- O segundo numero e maior.")
elif dif == 0:
    print("Nenhum numero e maior ou menor, os dois sao iguais!")