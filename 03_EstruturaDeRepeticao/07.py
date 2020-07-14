for i in range(5):
    numb = int(input("Digite um número: "))
    if i == 0:
        maior = numb
    else:
        if numb > maior:
            maior = numb

print(f"O maior número foi {maior}.")