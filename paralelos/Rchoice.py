import random

nm = int(input("Insira o numero de alunos PRESENTES: "))

alunos = []
while len(alunos) < nm:
    nomes = input("Nome do Aluno: ")
    alunos.append(nomes)

print("O aluno sorteado para ir a frente apresentar foi: {}".format(random.choice(alunos)))