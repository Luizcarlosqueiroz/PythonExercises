a = 1
b = 2

ate = int(input("Digite o n-ésimo termo: "))

print(f"1, {a}, ",end="")
for i in range(0, ate):
    print(b, end=", ")
    c = b
    b += a
    a = c
