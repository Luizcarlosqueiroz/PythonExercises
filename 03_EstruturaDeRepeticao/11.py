soma = 0

a = int(input("Digite um número: "))
b = int(input("Difite outro número: "))

if a < b:
    c = a
    d = b
else:
    c = b
    d = a

for i in range(c+1, d):
    soma += i

print(f"A soma é igual a {soma}")