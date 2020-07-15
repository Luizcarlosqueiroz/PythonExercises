continuar = "S"
numb = 16

while continuar == "S":

    while numb <= 0 or numb >= 16:
        numb = int(input("Digite um número: "))

    fatorial = numb

    print("O fatorial desse número é: ")
    print(f"{numb}! = ",end="")

    for i in range(1,numb):
        print(f"{i}.",end="")
        fatorial = fatorial * i

    print(f"{numb} = {fatorial}")

    continuar = input("Você deseja continuar [S]? ").upper().strip()
    if continuar == "S":
        numb = 16
        print("==============")