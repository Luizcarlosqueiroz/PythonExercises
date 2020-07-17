numb = 0
soma = 0

while numb <= 0:
    numb = int(input("Digite o número de pessoas: "))
    if numb <= 0:
        print("O número deve ser maior que 0.")

for i in range(0, numb):
    idade = 0
    while idade <= 0:
        idade = float(input("Idade: "))
        if idade <= 0:
            print("A idade não pode ser negativa.")
    soma += idade

media = soma / numb
print(media)

if 0 <= media <= 25:
    print("Esta turma é jovem.")
elif 26 <= media <= 60:
    print("Esta turma é adulta.")
elif media > 60:
    print("Esta turma é idosa.")
