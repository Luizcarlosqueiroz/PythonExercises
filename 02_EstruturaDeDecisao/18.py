#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite a data no formato dd/mm/aaaa: ")

if int(data[:2]) > 30:
    print("Data inválida.")
elif int(data[3:5]) > 12:
    print("Data inválida.")
elif int(data[6:10]) > 2020:
    print("Data inválida.")
else:
    print("Data válida.")