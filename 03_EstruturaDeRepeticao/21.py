numb = int(input("Digite o número? "))
primo = 0

for i in range(1,numb):
    if numb % i == 0:
        primo += 1

if primo == 1:
    print("O número é primo.")
else:
    print("O número não é primo.")