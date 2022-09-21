d = int(input("Insira o dia do seu nascimento: "))
m = int(input("Insira o mes do seu nascimento: "))
a = int(input("Insira o ano do seu nascimento: "))

if d > 31:
    print("O Dia que voce inseriu ultrapassa os limites!")

if m > 12:
    print("O Mes que voce inseriu ultrapassa os limites!")



elif m == 1:
    print("A data do seu nascimento formatada e:", d, "/ janeiro /", a)
elif m == 2:
    print("A data do seu nascimento formatada e:", d, "/ fevereiro /", a)
elif m == 3:
    print("A data do seu nascimento formatada e:", d, "/ marco /", a) 
elif m == 4:
    print("A data do seu nascimento formatada e:", d, "/ abril /", a)
elif m == 5:
    print("A data do seu nascimento formatada e:", d, "/ maio /", a)
elif m == 6:
    print("A data do seu nascimento formatada e:", d, "/ junho /", a)
elif m == 7:
    print("A data do seu nascimento formatada e:", d, "/ julho /", a)
elif m == 8:
    print("A data do seu nascimento formatada e:", d, "/ agosto /", a)
elif m == 9:
    print("A data do seu nascimento formatada e:", d, "/ setembro /", a)
elif m == 10:
    print("A data do seu nascimento formatada e:", d, "/ outubro /", a)
elif m == 11:
    print("A data do seu nascimento formatada e:", d, "/ novembro /", a)
elif m == 12:
    print("A data do seu nascimento formatada e:", d, "/ dezembro /", a)


#print("A data do seu nacsimento e {} / {} / {}".format(d, m, a))