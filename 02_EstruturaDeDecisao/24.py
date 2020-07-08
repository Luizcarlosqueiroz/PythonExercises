a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

op = int(input("Qual operação deseja realizar:\n"
      "[1] - Adição\n"
      "[2] - Subtração\n"
      "[3] - Multiplicação\n"
      "[4] - Divisão\n"))

if op == 1:
    numb = a + b
elif op == 2:
    numb = a - b
elif op == 3:
    numb = a * b
elif op == 4:
    numb = a / b

print(f"Resultado: {numb}")

if numb == 0:
    print("O número é nulo.")
elif numb % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

if numb == 0:
    print("O número é nulo.")
elif numb < 0:
    print("O número é negativo.")
else:
    print("O número é positivo.")

if numb == round(numb):
    print("O número é inteiro.")
else:
    print("O número é decimal.")