alunos = {}
matricula = int(input("Digite sua matricula(numero negativo pára o programa): "))
while matricula < 1:
    matricula = int(input("Erro! Digite novamene.Matricula tem que ser maior que zero: "))

while matricula != 0:
    nomeDoAluno = input("Digite o nome do Aluno: ")
    idadeDoAluno = int(input("Digite a idade do aluno(Idade > 0): "))
    while idadeDoAluno < 1:
        idadeDoAluno = int(input("Erro.Digite novamente a idade do aluno(Idade > 0): "))
    alunos[matricula] = (nomeDoAluno, idadeDoAluno)

    matricula = int(input("Digite sua matricula(numero negativo pára o programa): "))
    while (matricula <0 ) or (matricula in alunos):
        matricula = int(input("Digite sua matricula(numero negativo pára o programa): "))

print(f"Tabela dos alunos listados{alunos} ")

entrada = int(input("Digite um numero de entrada: "))
while entrada < 1:
    entrada = int(input("Digite novamente um numero de entrada: "))


while entrada !=0:
    minimo = int(input("Idade minima: "))
    maximo = int(input("Idade maxima: "))
    for i in alunos:
        if alunos[i][1] >= minimo and alunos[i][1] <= maximo:
            # print('  ', i, alunos[i])
            print('  ', i, alunos[i])
        else:
            print("Aluno não existe")
    entrada = int(input("Digite outra entrada (0 parar o programa): "))




