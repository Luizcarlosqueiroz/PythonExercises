preco = 1.99

print("Lojas Quase Dois - Tabela de preços")

for i in range(1, 51):
    print("{} - R$ {:.2f}".format(i, preco))
    preco += 1.99
