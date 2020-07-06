salarioHora = float(input("Digite o salário por hora: "))
horasTrab = int(input("Digite a quantidade de horas trabalhadas: "))

sal = salarioHora * horasTrab
if sal <= 900:
    ir = 0
elif sal <= 1500:
    ir = sal * 0.05
elif sal <= 2500:
    ir = sal * 0.10
else:
    ir = sal * 0.2
inss = sal * 0.10
fgts = sal * 0.11

print("Salário Bruto: {:.2f}".format(sal))
print("IR   : R$ {:.2f}".format(ir))
print("INSS : R$ {:.2f}".format(inss))
print("FGTS : R$ {:.2F}".format(fgts))
print("Total de descontos: R$ {:.2f}".format(ir + inss))
print("Salário Líquido : {:.2f}".format(sal - ir - inss))