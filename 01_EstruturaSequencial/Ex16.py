import math
area = float(input("Qual o tamanho da área em metros a ser pintada? "))
latas = math.ceil(area/3/18)
print("Você precisará de {} latas de tinta com um custo de R$ {:.2f}.".format(latas, latas*80))