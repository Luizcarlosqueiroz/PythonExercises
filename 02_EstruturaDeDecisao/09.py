n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

print("A ordem decescente é: ")
if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(n1, n2, n3)
    else:
        print(n1, n3, n2)

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(n2, n1, n3)
    else:
        print(n2, n3, n1)

elif n3 >= n1 and n3 >= n1:
    if n1 >= n2:
        print(n3, n1, n2)
    else:
        print(n3, n2, n1)