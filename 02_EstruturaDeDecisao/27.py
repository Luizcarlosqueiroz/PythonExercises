prod = input("Qual fruta deseja comprar? ").upper()
peso = float(input("Digite o peso desejado: "))
custo = 0

if prod == "MORANGO":
    if peso <= 5:
        custo = peso * 2.5
    elif peso > 5:
        custo = peso * 2.2
elif prod == "MACA":
    if peso <= 5:
        custo = peso * 1.8
    elif peso > 5:
        custo = peso * 1.5

if custo > 25 or peso > 8:
    custo = custo * 0.9

print("À pagar: R$ {:.2f}.".format(custo))
