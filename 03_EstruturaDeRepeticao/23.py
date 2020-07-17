numb = int(input("Você deseja saber quantos números primos? "))
div = 0

for i in range(1, numb+1):
    primo = True
    for j in range(2, int(i/2+1)):
        div += 1
        if i % j == 0:
            primo = False
            break

    if primo:
        print(i, end=" ")

print(f"\nTotal de divisões: {div}")
