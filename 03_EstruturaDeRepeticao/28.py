qtdCD = 0
total = 0.0

while qtdCD <= 0:
    qtdCD = int(input("Qual a quantidade de CDs? "))
    if qtdCD <= 0:
        print("A quantidade de CDs deve ser positiva. ")

for i in range(1, qtdCD+1):
    valor = float(input(f"Valor do CD {i}: "))
    total += valor

print("O valor investido foi de R$ {:.2f}".format(total))
print("A média dos valores dos CDs é de R$ {:.2f}".format(total/qtdCD))
