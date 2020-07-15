n = int(input("Quantos números serão digitados? "))
soma = 0

number = int(input("Número: "))
maior = number
menor = number
soma = number

for i in range(1,n):
    number = int(input("Número: "))

    if number > maior:
        maior = number
    elif number < menor:
        menor = number

    soma += number

print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Soma:  {soma}")