turno = input("Em qual turno você estuda [M/V/N]: ").upper()

if turno == "M":
    print("Matutino")
elif turno == "V":
    print("Vespertino")
elif turno == "N":
    print("Noturno")
else:
    print("Opção inválida.")