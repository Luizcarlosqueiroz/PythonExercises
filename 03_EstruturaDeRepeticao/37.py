code = 1
numb = 1
soma_peso = 0
soma_altura = 0

while code != 0:
    code = int(input("Digite seu código: "))
    if code == 0:
        break
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    soma_peso += peso
    soma_altura += altura

    if numb == 1:
        mais_gordo = mais_magro = peso
        cod_gordo = cod_magro = code
        mais_alto = mais_baixo = altura
        cod_alto = cod_baixo = code
    else:
        if peso > mais_gordo:
            mais_gordo = peso
            cod_gordo = code
        elif peso < mais_magro:
            mais_magro = peso
            cod_magro = code

        if altura > mais_alto:
            mais_alto = altura
            cod_alto = code
        elif altura < mais_baixo:
            mais_baixo = altura
            cod_baixo = code

    numb += 1

print("O cliente mais alto é o {} com {:.2f}cm.".format(cod_alto, mais_alto))
print("O cliente mais magro é o {} com {:.2f}cm.".format(cod_magro, mais_magro))
print("O cliente mais gordo é o {} com {:.2f}kg.".format(cod_gordo, mais_gordo))
print("O cliente mais baixo é o {} com {:.2f}kg.".format(cod_baixo, mais_baixo))
print("A média de altura é: {:.1f}".format(soma_altura / numb))
print("A média de peso é: {:.2f}".format(soma_peso / numb))
