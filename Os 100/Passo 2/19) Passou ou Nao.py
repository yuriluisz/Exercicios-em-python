'''Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua 
média e mostre na tela. No final, analise a média e mostre se o aluno teve 
ou não um bom aproveitamento (se ficou acima da média 7.0). '''

nota1 = float(input("Insira a primeira nota que o aluno tirou: "))
nota2 = float(input("Insira a segunda nota que o aluno tirou: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("\033[0;32mO Aluno foi aprovado com nota {}\033[0;0m".format(media))
else:
    falta = 7 - media
    print("\033[0;31mO Aluno nao foi aprovado por falta de {} pontos :(\033[0;0m".format(falta))