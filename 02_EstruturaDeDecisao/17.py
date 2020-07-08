ano = int(input("Digite o ano: "))
bisexto = False


if ano % 4 == 0 and ano % 100 != 0:
    bisexto = True
if ano % 400 == 0:
    bisexto = True

if bisexto:
    print("O ano é bisexto.")
else:
    print("O ano não é bisexto.")