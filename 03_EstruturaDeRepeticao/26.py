candA = candB = candC = 0
voto = ""
total = 0

while total <= 0:
    total = int(input("Qual o número total de eleitores? "))
    if total <= 0:
        print("Favor inserir um valor positivo.")

for i in range(1, total+1):
    while voto not in ("A", "B", "C"):
        voto = input("Voto [A/B/C]: ").upper()
        if voto not in ("A", "B", "C"):
            print("Candidato inválido.")

    if voto == "A":
        candA += 1
    elif voto == "B":
        candB += 1
    elif voto == "C":
        candC += 1
    voto = ""

print("===RESULTADO===")
print(f"Candidato A: {candA}")
print(f"Candidato B: {candB}")
print(f"Candidato C: {candC}")
