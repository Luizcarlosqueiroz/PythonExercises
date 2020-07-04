h = float(input("Digite sua altura em metros: "))
pesoH = (72.7 * h) - 58
pesoM = (62.1 * h) - 44.7
print("Seu peso ideal é: \n"
      "se você for homem: {:.1f}kg. \n"
      "se você for homem: {:.1f}kg.".format(pesoH, pesoM))