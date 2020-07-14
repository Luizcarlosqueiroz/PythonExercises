nome = ""
idade = -1
salario = 0
sexo = ""
eCivil = ""

while len(nome) <= 3:
    nome = input("Digite o nome: ")
    if len(nome) <= 3:
        print("O nome deve ter mais do que 3 caracteres.")

while idade < 0 or idade > 150:
    idade = int(input("Digite a idade: "))
    if idade < 0 or idade > 150:
        print("A idade deve estar entre 0 e 150.")

while salario <= 0:
    salario = float(input("Digite o salário: "))
    if salario <= 0:
        print("O salário deve ser maior que 0.")

while sexo not in ("F", "M"):
    sexo = input("Digite o sexo [F/M]: ").upper().strip()
    if sexo != "F" and sexo != "M":
        print("Só pode ser digitado F ou M.")

while eCivil not in ('S', 'C', 'V', 'D'):
    eCivil = input("Digite seu estado civil [S/C/V/D]: ").upper().strip()
    if eCivil not in ('S', 'C', 'V', 'D'):
        print("Só pode ser digitado S, C, V ou D.")

print("CADASTRO REALIZADO.")