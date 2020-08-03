soma = 0
soma_2000 = 0
numb_2000 = 0

for i in range(0, 5):
    codigo = int(input("Código da cidade: "))
    numb_veic = int(input("Nº de Veículos: "))
    numb_acid = int(input("Nº de Acidentes: "))

    if i == 0:
        mais_acid = menos_acid = numb_acid
        mais_cod = menos_cod = codigo
    else:
        if numb_acid > mais_acid:
            mais_acid = numb_acid
            mais_cod = codigo
        elif numb_acid < menos_acid:
            menos_acid = numb_acid
            menos_cod = codigo

    soma += numb_veic

    if numb_veic < 2000:
        soma_2000 += numb_acid
        numb_2000 += 1

print(f"Cidade com mais acidentes: cód {mais_cod} - acidentes {mais_acid}.")
print(f"Cidade com menos acidentes: cód {menos_cod} - acidentes {menos_acid}.")
print("A média de veículos é de {:.2f}".format(soma / 5))
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos é de: {:.2f}".format(soma_2000 / numb_2000))
