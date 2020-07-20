tabuada = int(input("Montar a tabuada de: "))

inicio = int(input("Começar por: "))
fim = inicio
while fim <= inicio:
    fim = int(input("Terminar em: "))
    if fim <= inicio:
        print("Deve terminar num valor que iniciou.")

for i in range(inicio, fim+1):
    print(f"{tabuada} x {i} = {tabuada*i}")
