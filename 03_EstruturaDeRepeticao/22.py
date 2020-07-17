numb = int(input("Digite o número? "))
primo = 0

print("O número é divisível por: ",end="")
for i in range(1,numb+1):
    if numb % i == 0:
        primo += 1
        print(i, end=" ")

if primo <= 2:
    print("\nLogo, o número é primo.")
else:
    print("\nLogo, o número não é primo.")