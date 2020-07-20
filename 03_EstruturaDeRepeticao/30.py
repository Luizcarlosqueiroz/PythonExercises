preco =  0.18

print("Preço do pão: R$ 0.18\nPanificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    print("{} - R$ {:.2f}".format(i, preco))
    preco += 0.18
