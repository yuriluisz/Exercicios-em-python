''' Faça um algoritmo que pergunte a distância que um passageiro deseja 
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
viagens até 200Km e R$0.45 para viagens mais longas. '''

dist = int(input("Insira a distancia da viagem: "))

if dist >= 200:
    valor = dist * 0.45
    print("O valor total da viagem de {}km ficara de R${}".format(dist, valor))
else:
    valor = dist * 0.50
    print("O valor total da viagem de {}km ficara de R${}".format(dist, valor))