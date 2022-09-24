''' Crie um programa que leia duas notas de um aluno e calcule a sua média, 
mostrando uma mensagem no final, de acordo com a média atingida: 
- Média até 4.9: REPROVADO 
- Média entre 5.0 e 6.9: RECUPERAÇÃO 
- Média 7.0 ou superior: APROVADO '''

nota1 = float(input("Insira a primera nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2
if media >= 7:
    print("\033[0;32mO aluno foi aprovado com nota {}. Parabens!\033[0;0m".format(media))
elif media in (5, 5.1, 5.2, 5.3, 5.4, 5.6, 5.7, 5.8, 5.9, 6, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9):
    print("\033[0;33mO aluno ficou de recuperacao com nota {}. Tente melhorar!\033[0;0m".format(media))
elif media <= 5:
    print("\033[0;31mO aluno foi reprovado com a nota {}. :(\033[0;0m".format(media))
