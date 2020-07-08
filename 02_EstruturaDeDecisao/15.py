l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if (l1+l2+l3)/2 <= l1 or (l1+l2+l3)/2 <= l2 or (l1+l2+l3)/2 <= l3:
    print("Não é possível formar um triângulo.")
else:
    print("Forma um triângulo do tipo: ", end="")
    if l1 == l2 and l2 == l3:
        print("Triângulo Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")