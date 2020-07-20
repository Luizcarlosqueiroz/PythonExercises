#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que
# leia as um conjunto indeterminado de temperaturas,
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temp = 1.0
total = 0
quantidade = 0

print("Dados de Temperatura")
print("Informe os dados. Caso deseje encerrar o programa, insira 0.")

while temp != 0:
    temp = float(input("Temperatura: "))
    if temp == 0:
        break
    quantidade += 1
    total += temp
    print(quantidade)

    if quantidade == 1:
        high = temp
        low = temp
    else:
        if temp > high:
            high = temp
        if temp < low:
            low = temp

print("Maior temperatura: {:.2f}".format(high))
print("Menor temperatura: {:.2f}".format(low))
print("Média temperatura: {:.2f}".format(total / quantidade))
