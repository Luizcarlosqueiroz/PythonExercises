popA = popB = 0
txA = txB = -1.0
anos = 0
cont = "S"

while cont != "N":

    while popA < 1:
        popA = int(input("Digite a população da cidade A: "))
        if popA < 1:
            print("A população não pode ser negativa.")

    while txA <= -1:
        txA = float(input("Digite a taxa de variação anual da população: "))
        if txA <= -1:
            print("A taxa não pode ser menor que -100%")

    popB = popA
    txB = txA

    while popB <= popA:
        popB = int(input("Digite a população da cidade B: "))
        if popB <= popA:
            print("A população B não pode ser menor ou igual a população A.")

    while txB >= txA:
        txB = float(input("Digite a taxa de variação anual da população: "))
        if txB >= txA:
            print("A taxa de crecimento de B não pode ser maior ou igual a taxa de A")

    while popA < popB:
        popA = popA * (1 + txA)
        popB = popB * (1 + txB)
        anos += 1

    print(f"Demorou {anos} anos para a população A ultrapassar a pop. da cidade B.")


    cont = input("Deseja continuar [S/N]? ").upper().strip()
    if cont != "N":
        popA = popB = 0
        txA = txB = -1.0
        anos = 0
