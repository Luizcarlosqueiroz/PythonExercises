prod1 = int(input("Digite o preço do produto 1: "))
prod2 = int(input("Digite o preço do produto 2: "))
prod3 = int(input("Digite o preço do produto 3: "))

if prod1 <= prod2 and prod1 <= prod3:
    print("Compre o primeiro produto.")
elif prod2 <= prod1 and prod2 <= prod3:
    print("Compre o segundo produto.")
elif prod3 <= prod1 and prod3 <= prod1:
    print("Compre o terceiro produto.")