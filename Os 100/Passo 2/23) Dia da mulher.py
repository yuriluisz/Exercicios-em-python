''' Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
sexo e o valor das compras do cliente e calcule o preço com desconto. 
Sabendo que: 
- Homens ganham 5% de desconto 
- Mulheres ganham 13% de desconto'''

nome = str(input("Insira seu nome: "))
sexo = str(input("Insira seu sexo (f) ou (m): "))
valor = float(input("Insira o valor de suas compras: "))

if sexo == "m" or "M":
    des = valor - (valor * 3 / 100)
    print("Obrigado {} pela sua compra, com a promocao especial de dia da mulher com 3% de desconto o valor total ficou: R${}".format(nome, des))
elif sexo == "f" or "F":
    desf = valor - (valor * 15 / 100)
    print("Feliz dia da mulher {} e  obrigado pela sua compra, e gracas ao dia da mulher com 15% de desconto o valor total ficou: R${}".format(nome, desf))