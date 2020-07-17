numb = int(input("Digite o número de notas: "))
soma = 0

for i in range(0, numb):
    nota = float(input("Nota: "))
    soma += nota

print(f"A média das notas é: {soma/numb}")
