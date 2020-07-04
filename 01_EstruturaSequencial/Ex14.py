peso = float(input("Qual o peso do peixe? "))
excesso = peso - 50
multa = excesso * 4

if peso <= 50:
    print("Tudo ok!")
else:
    print("O peixe tem um excesso de peso de {:.1f}kg".format(excesso))
    print("Você terá que pagar R$ {:.2f} de multa".format(multa))