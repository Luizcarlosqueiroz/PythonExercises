codigo = int(input("Digite o código do seu cargo: "))
salario = float(input("Digite seu salário: "))

if (codigo == 1):
    print("Seu cargo é Secretário. Seu novo salário é R$", (salario * 1.45))
elif (codigo == 2):
    print("Seu cargo é Tesoureiro. Seu novo salário é R$", (salario * 1.35))
elif (codigo == 3):
    print("Seu cargo é Professor. Seu novo salário é R$", (salario * 1.25))
elif (codigo == 4):
    print("Seu cargo é Coordenador. Seu novo salário é R$", (salario * 1.15))
elif (codigo == 5):
    print("Seu cargo é Diretor. Você não terá aumento.")
else:
    print("Você não digitou um código válido.")