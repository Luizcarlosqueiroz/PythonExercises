print("== Análise de um número ==")
num = int(input("Digite um número: "))

#Análise de o número é par ou ímpar
if (num == 0):
    print("O número é nulo.")
elif (num % 2 == 0):
    print("O número é par.")
else:
    print("O número é ímpar.")

#Análise se o valor é positivo ou negativo
if (num > 0):
    print("Além disso, o número é positivo.")
elif (num < 0):
    print("Além disso, o número é negativo.")