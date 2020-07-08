print("Telefonou para a vítima?\n"
      "Esteve no local do crime?\n"
      "Mora perto da vítima?\n"
      "Devia para a vítima?\n"
      "Já trabalhou com a vítima?")

cont = 0
for i in range (5):
    resp = input("").upper()
    if resp == "S":
        cont += 1

if cont == 5:
    print("Assassino")
elif 3 <= cont >= 4:
    print("Cúmplice")
elif cont == 2:
    print("Suspeita")
else:
    print("Inocente")
