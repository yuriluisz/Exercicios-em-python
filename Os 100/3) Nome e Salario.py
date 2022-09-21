''' Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho. '''

nome = str(input("Insira o nome do funcionario: "))
salario = float(input("Insira o salario do funcionario"))

print("O funcionario {} ira receber {}R$ no final do mes".format(nome, salario))