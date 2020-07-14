x = -1
while 0 > x or x > 10:
    x = int(input("Digite um número entre 0 e 10: "))
    if 0 > x or x > 10:
        print("Nota inválida.")