numb = int(input("Digite um número: "))
fatorial = numb
print(f"O fatorial de {numb}")

print(f"{numb}! = {numb}", end="")

for i in reversed(range(1, numb)):
    print(f".{i}", end="")
    fatorial = fatorial * i

print(f" = {fatorial}")
