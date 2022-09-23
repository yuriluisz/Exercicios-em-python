'''Crie um programa que leia o tamanho de três segmentos de reta. 
Analise seus comprimentos e diga se é possível formar um triângulo com essas 
retas. Matematicamente, para três segmentos formarem um triângulo, o 
comprimento de cada lado deve ser menor que a soma dos outros dois. '''

rA = int(input("Insira o comprimento da primera reta: "))
rB = int(input("Insira o comprimento da segunda reta: "))
rC = int(input("Insira o comprimento da terceira reta: "))

if rA + rB > rC and rB + rC > rA and rA + rC > rB:
    print("Com essas 3 retas e sim possivel fazer um triangulo!")
else:
    print("Com essas 3 retas nao e possiver fazer uma reta!")