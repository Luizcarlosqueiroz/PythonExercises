n = int(input("Quantos números serão digitados? "))
number = 1001

while number > 1000:
    number = int(input("Número: "))
    if number > 1000:
        print("O número deve estar entre 0 e 1000.")

maior = number
menor = number
soma = number

for i in range(1, n):
    number = int(input("Número: "))

    if number > maior:
        maior = number
    elif number < menor:
        menor = number

    soma = soma + number

print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Soma:  {soma}")