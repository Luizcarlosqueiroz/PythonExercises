continuar = "S"
produto = 1
numProd = 1
total = 0
pagoCliente = 0

while continuar == "S":
    while produto != 0:
        produto = float(input(f"Produto {numProd}: R$ "))
        total += produto
        numProd += 1

    print("--------")
    print("Total: R$ {:.2f}".format(total))

    while pagoCliente < total:
        pagoCliente = float(input("Dinheiro: R$ "))
        if pagoCliente < total:
            print("Valor insuficiente.")

    print("Troco: R$ {}".format(pagoCliente - total))
    print("===FIM DA COMPRA===")

    continuar = input("Novo cliente [S/N]? ").upper().strip()

    produto = 1
    numProd = 1
    total = 0
