import random as random

nm = int(input("Insira o numero de alunos PRESENTES: "))

alunos = []
while len(alunos) < nm:
    nomes = input("Insira os nomes dos alunos: ")
    alunos.append(nomes)

print("O aluno sorteado para ir a frente apresentar foi:\033[1;32m {}\033[0;0m".format(random.choice(alunos)))