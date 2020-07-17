turmas = 0
totalAlunos = 0

while turmas <= 0:
    turmas = int(input("Digite o número de turmas: "))
    if turmas <= 0:
        print("O número de turmas deve ser positivo.")

for i in range(0, turmas):
    alunos = 0
    while 0 >= alunos or alunos > 40:
        alunos = int(input("Digite o número de alunos: "))
        if 0 >= alunos or alunos > 40:
            print("O número de alunos deve estar entre 1 e 40.")
    totalAlunos += alunos


print(f"O número médio de alunos por turma é: {totalAlunos/turmas}")
