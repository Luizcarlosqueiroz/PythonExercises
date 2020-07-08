saque = int(input("Qual o valor do saque: "))

n100 = saque // 100
n50 = (saque % 100) // 50
n10 = (saque % 50) // 10
n5 = (saque % 10) // 5
n1 = (saque % 5)

print(f"Notas de 100: {n100}")
print(f"Notas de  50: {n50}")
print(f"Notas de  10: {n10}")
print(f"Notas de   5: {n5}")
print(f"Notas de   1: {n1}")