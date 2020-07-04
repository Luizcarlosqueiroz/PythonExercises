tamanho = float(input("Digite o tamanho do arquivo (MB): "))
vel = int(input("Digite a velocidade do link de internet (Mbps): "))

tempoTotal = int(tamanho/vel)
tempoMin = int(tempoTotal/60)
print(f"O arquivo será baixado em aproximadamente {tempoMin} minutos.")