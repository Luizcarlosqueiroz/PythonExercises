salarioB = float(input("Digite seu salário bruto: "))

print("+ Salário Bruto : R$ {:.2f} \n"
      "- IR (11%) : R$ {:.2f} \n"
      "- INSS (8%) : R$ {:.2f} \n"
      "- Sindicato (5%) : R$ {:.2f} \n"
      "= Salário Liquido : R$ {:.2f}"
      .format(salarioB, salarioB * 0.11, salarioB * 0.08, salarioB * 0.05, salarioB * 0.76))