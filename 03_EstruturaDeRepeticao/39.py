for i in range(1, 11):
    numb = int(input("Número: "))
    altura = float(input("Altura: "))

    if i == 1:
        numb_alto = numb_baixo = numb
        alto = baixo = altura
    else:
        if altura > alto:
            numb_alto = numb
            alto = altura
        elif altura < baixo:
            numb_baixo = numb
            baixo = altura

print("O/A aluno/aluna {} é o/a mais alto/alta com {:.1f}cm".format(numb_alto, alto))
print("O/A aluno/aluna {} é o/a mais baixo/baixa com {:.1f}cm".format(numb_baixo, baixo))
