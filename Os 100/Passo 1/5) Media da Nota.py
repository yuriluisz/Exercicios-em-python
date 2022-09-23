'''Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5 
'''

nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("\033[0;32m O aluno passou com a nota: {}\033[0;0m".format(media))
else:
    print("\033[0;31m O aluno ficou de recuperacao com a nota: {}\033[0;0m".format(media))