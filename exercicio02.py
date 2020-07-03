estadoCivil = input("Qual seu estado civil? \n"
                    "[S] - Solteiro(a) \n"
                    "[C] - Casado(a) \n"
                    "[V] - Viúvo(a) \n"
                    "[D] - Divorciado(a) \n").upper()

if (estadoCivil == 'S'):
    print("Seu estado civil é Solteiro.")
elif (estadoCivil == 'C'):
    print("Seu estado civil é Casado.")
elif (estadoCivil == 'V'):
    print("Seu estado civil é Viúvo.")
elif (estadoCivil == 'D'):
    print("Seu estado civil é Divorciado.")
else:
    print("Você não digitou um input válido.")