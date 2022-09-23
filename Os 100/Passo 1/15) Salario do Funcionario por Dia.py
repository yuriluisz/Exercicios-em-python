'''Crie um programa que leia o número de dias trabalhados em um mês e mostre
o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha
R$25 por hora trabalhada.'''

dias = int(input("Insira o numero de dias trabalhados pelo funcionario: "))

salario = (dias * 8) * 25
print("O salario do funcionario que trabalho {} dias, sera de \033[0;32m{}\033[0;0mR$".format(dias, salario))