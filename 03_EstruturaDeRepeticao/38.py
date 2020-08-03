salario = float(input("Digite o salário inicial: "))
taxa = 0.015
ano = 1996

while ano <= 2020:
    salario = salario * (1 + taxa)
    taxa = taxa * 2
    ano += 1

print("Salário Atual: R$ {:.2f}".format(salario))
