# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#
#     Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#     326 = 3 centenas, 2 dezenas e 6 unidades
#     12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numb = int(input("Digite um número menor que 1000: "))

cent = numb // 100
deze = (numb % 100) // 10
unid = (numb % 10)

if cent > 0:
    if cent == 1:
        print(f"{cent} centena", end="")
    elif cent > 1:
        print(f"{cent} centenas", end="")

if deze > 0:
    if cent > 0 and unid > 0:
        print(", ", end="")
    elif cent > 0 and unid == 0:
        print(" e ", end="")

    if deze == 1:
        print(f"{deze} dezena", end="")
    elif deze > 1:
        print(f"{deze} dezenas", end="")

if unid > 0:
    if cent > 0 and deze > 0:
        print(" e ", end="")
    elif cent > 0 and deze == 0:
        print(" e ", end="")
    elif cent == 0 and deze > 0:
        print(" e ", end="")

    if unid == 1:
        print(f"{unid} unidade", end="")
    elif unid > 1:
        print(f"{unid} unidades", end="")