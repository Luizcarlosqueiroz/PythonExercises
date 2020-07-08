comb = input("Qual o combustível [A/G]? ").upper()
litros = float(input("Quantos litros? "))

if comb == "A":
    preco = 1.9
    if litros >= 20:
        print("R$ {:.2f}".format(litros * (preco * 0.97)))
    else:
        print("R$ {:.2f}".format(litros * (preco * 0.95)))
elif comb == "G":
    preco = 2.5
    if litros >= 20:
        print("R$ {:.2f}".format(litros * (preco * 0.96)))
    else:
        print("R$ {:.2f}".format(litros * (preco * 0.94)))

