''' Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta. '''

A = float(input("Insira o valor de A: "))
B = float(input("Insira o valor de B: "))
C = float(input("Insira o valor de C: "))

D1 = B ** B
Delta = D1 - 4 * A * C
print(Delta)
