numb = 0
while numb < 1 or numb > 10:
    numb = int(input("Digite o número que deseja saber a tabuada: "))
    if numb < 1 or numb > 10:
        print("O valor deve estar entre 1 e 10.")

for i in range(1, 11):
    print(f"{numb} X {i} = {numb*i}")