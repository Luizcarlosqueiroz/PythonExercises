area = float(input("Qual o tamanho da área em metros a ser pintada? "))
litros = area / 6
latas = int(litros / 18)
galoes = int(litros / 3.6)

if litros % 18 != 0:
    latas += 1

if litros % 3.6 != 0:
    galoes += 1

mixLatas = int(litros/18)
litrosRest = litros - (mixLatas*18)
mixGaloes = int(litrosRest / 3.6)

if litrosRest % 3.6 != 0:
    mixGaloes += 1

print("Você precisará de {} latas de tinta com um custo de R$ {:.2f}.".format(latas, latas*80))
print("OU")
print("Você precisará de {} galões de tinta com um custo de R$ {:.2f}.".format(galoes, galoes*25))
print("OU")
print("Você precisará de {} latas e {} galões de tinta com um custo de R$ {:.2f}."
      .format(mixLatas, mixGaloes, mixLatas*80 + mixGaloes*25))
