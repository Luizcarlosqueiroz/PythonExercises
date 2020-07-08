import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Esta não é uma equação do segundo grau.")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não há resultados reais para a equação.")
    elif delta == 0:
        x = (-b) / (2*a)
        print("O resultado é {:.1f}".format(x))
    else:
        x1 = ((-b) + math.sqrt(delta)) / (2*a)
        x2 = ((-b) - math.sqrt(delta)) / (2*a)
        print("Os resultados de x possíveis são {:.1f} e {:.1f}.".format(x1, x2))