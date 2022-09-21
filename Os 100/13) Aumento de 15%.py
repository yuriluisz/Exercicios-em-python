''' Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.'''

nome = str(input("Insira o nome do funcionario: "))
salario = float(input("Insira o salario do funcionario: "))

aumento = salario + (salario * 15 / 100)
print("O salario do funcionario {} com 15% de aumento sera: \033[0;32m{}\033[0;0m".format(nome, aumento))