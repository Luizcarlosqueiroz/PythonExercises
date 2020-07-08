# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#
#                           Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#
#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
#
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
#
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

prod = input("Qual o produto você deseja?\n"
             "[1] - Filé Duplo\n"
             "[2] - Alcantra\n"
             "[3] - Picanha\n")
produto = ""
preco = 0
kg = float(input("Quantos quilos? "))
pagamento = input("Será pago com cartão Tabajara? [S/N] ").upper()


if prod == 1:
    produto = "Filé Duplo"
elif prod == 2:
    produto = "Alcantra"
elif prod == 3:
    produto = "Picanha"


if prod == 1:
    if kg <= 5:
        preco = kg * 4.9
    elif kg > 5:
        preco = kg * 5.8
elif prod == 2:
    if kg <= 5:
        preco = kg * 5.9
    elif kg > 5:
        preco = kg * 6.8
elif prod == 3:
    if kg <= 5:
        preco = kg * 6.9
    elif kg > 5:
        preco = kg * 7.8


if pagamento == "S":
    desc = preco * 0.05
    pagamento = "Cartão Tabajara"
else:
    desc = 0
    pagamento = "Outro método"


total = preco - desc


print("Produto:           {}".format(produto))
print("Qtd:               {:.1f} Kg".format(kg))
print("Preço total:       R$ {:.2f}".format(preco))
print("Tipo do pagamento: {}".format(pagamento))
print("Valor do Desconto: R$ {:.2f}".format(desc))
print("Valor a pagar:     R$ {:.2f}".format(total))
