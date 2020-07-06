sal = float(input("Digite seu salário: "))

if sal < 0:
    print("Valor incorreto.")
elif sal <= 280:
    print("Salário atual: {:.2f}.".format(sal))
    print("Percentual aumento: 20%.")
    print("Valor do aumento: {:.2f}.".format(sal * 0.2))
    print("Novo salário: {:.2f}.".format(sal * 1.2))
elif sal <= 700:
    print("Salário atual: {:.2f}.".format(sal))
    print("Percentual aumento: 15%.")
    print("Valor do aumento: {:.2f}.".format(sal * 0.15))
    print("Novo salário: {:.2f}.".format(sal * 1.15))
elif sal <= 1500:
    print("Salário atual: {:.2f}.".format(sal))
    print("Percentual aumento: 10%.")
    print("Valor do aumento: {:.2f}.".format(sal * 0.1))
    print("Novo salário: {:.2f}.".format(sal * 1.1))
else:
    print("Salário atual: {:.2f}.".format(sal))
    print("Percentual aumento: 5%.")
    print("Valor do aumento: {:.2f}.".format(sal * 0.05))
    print("Novo salário: {:.2f}.".format(sal * 1.05))
