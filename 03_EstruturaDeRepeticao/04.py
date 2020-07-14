popA = 80000
popB = 200000
anos = 0

while popA < popB:
    popA = popA * 1.03
    popB = popB * 1.015
    anos += 1

print(f"Demorou {anos} anos para a população A ultrapassar a pop. da cidade B.")