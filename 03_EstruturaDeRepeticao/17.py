numb = int(input("Digite um número: "))
fatorial = numb
print("O fatorial desse número é: ")

print(f"{numb}! = ",end="")

for i in range(1,numb):
    print(f"{i}.",end="")
    fatorial = fatorial * i

print(f"{numb} = {fatorial}")