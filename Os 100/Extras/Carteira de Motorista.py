nome = str(input("Insira o seu nome: "))
nasc = int(input("Insira o ano de seu nascimento: "))

cart = 2022 - nasc
if cart >= 18:
    pas = cart - 18
    print("Parabens {} voce ja pode fazer carteira de motorista! Ja fazem {} anos que voce pode.".format(nome, pas))
else:
    npas = 18 - cart
    print("Poxa {} parece que voce ainda nao pode tirar carteira! Faltam apenas {} anos".format(nome, npas))