nome = input("Digite o número do usuário: ")
senha = nome
while nome == senha:
    senha = input("Digite uma senha: ")
    if nome == senha:
        print("Senha não pode ser igual ao usuário.")

print("Cadastro Realizado.")