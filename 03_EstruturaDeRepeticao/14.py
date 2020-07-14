impar = par = nulo = 0

for i in range(10):
    numb = int(input("Digite um número: "))
    if numb == 0:
        nulo += 1
    elif numb % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Você digitou {par} números pares e {impar} números ímpares.")