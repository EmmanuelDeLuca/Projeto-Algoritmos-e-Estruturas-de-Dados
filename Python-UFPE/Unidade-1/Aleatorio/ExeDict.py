# Fazer um programa para:
# – Ler uma tabela com Cursos, onde:
# • Cada curso é formado por um código (número positivo), um
# nome (String), e o centro a que pertence (número positivo).
# • A leitura da tabela de cursos pára com o código de curso zero. – Depois o usuário fornecerá uma lista de códigos de
# centro para que o programa imprima o código e nome
# de todos os cursos associados a cada centro digitado.
# – Se o código do centro não existir na tabela, mostrar a
# mensagem “Nenhum curso encontrado” e continuar.
# – O programa pára com a digitação de um código de
# centro inválido (negativo ou zero).
entrada = int(input("Digite o tamanho da tabela: "))
while entrada < 1:
    entrada = int(input("Tamanho deve ser inteiro e positivo.Tente novamente: "))
tab = {}
for i in range(entrada):
    codCurso = int(input("Codigo do curso (número positivo)"))
    while codCurso < 1:
        codCurso = int(input("Tente novamente. Digite um numero maior que zero"))
    nomeCurso = input("Nome do curso: ")
    centroCurso = int(input("Digite o numero do curso: "))
    while centroCurso < 1:
        centroCurso = int(input("Tente novamente. Digite um numero maior que zero"))
    
    tab[codCurso] = (nomeCurso, centroCurso)

    print(f"Tabela com {entrada}cursos foi lida corretamente.")
    print(f"Tabela -> {tab}")
    codCurso = int(input("Digite um código de profissão para buscar(<= 0 para parar)"))
    while codCurso > 0:
        if codCurso in tab:
            nomeCurso, centroCurso = tab[codCurso]
            print(f'Curso: {nomeCurso}, Centro: {centroCurso}, Codigo: {codCurso}')
        else:
            print(f"Esse curso {codCurso} não existe")

        codCurso = int(input('Digite outro codigo para busca(<= 0 para parar):'))
    print('Fim do programa')