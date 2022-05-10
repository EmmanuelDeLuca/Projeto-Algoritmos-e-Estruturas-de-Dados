# should_continue = True
# quantidade_disciplinas = 0
# codigo = {}

# while should_continue and quantidade_disciplinas < 500:
#     codigoDisciplina = (input("Escreva uma paalavra com 5 caracteres: "))
#     tamanho = len(codigoDisciplina)
#     if tamanho <= 5:
#         should_continue = False
#     else:
#         nome = input("Digite seu nome: ")
#         cargaHoraria = int(input("Digite a carga horario(Carga horario > 0)"))
#         while cargaHoraria < 1:
#             cargaHoraria = int(input("Digite a carga horario(Carga horario > 0)"))
#             numeroCreditos = int(input("Digite creditos (Creditos > 0): "))
#             while numeroCreditos < 1:
#                 numeroCreditos = int(input("Digite creditos (Creditos > 0): "))
#             codigo[codigoDisciplina] = (nome, cargaHoraria, numeroCreditos)

#     print(f'Tabela -> {codigo}')

codigo = {}
codigoDisciplina = (input("Digite o codigo da disciplina(caractere tem que ser menor ou igual a 5): "))
tamanho = len(codigoDisciplina)

while tamanho <= 5:
    codigoDisciplina = (input("Erro! Digite o codigo da disciplina(caractere tem que ser menor ou igual a 5): "))

while codigoDisciplina != 'FIM':
    nome = input("Digite o nome : ")
    cargaHoraria = int(input("carga horaria(Idade > 0): "))
    while cargaHoraria < 1:
        cargaHoraria = int(input("Erro.Digite novamente a idade do aluno(Idade > 0): "))
    credito = int(input("Digite valor para creditos(creditos > 0)"))
    while credito < 1:
        credito = int(input("Digite valor para creditos(creditos > 0)"))

    codigo[codigoDisciplina] = (codigoDisciplina,nome, cargaHoraria, credito)
    codigoDisciplina = int(input("Digite seu codigo( caso seja maior que 5, o programa ira parar): "))
    while (codigoDisciplina > 0 ) or (codigoDisciplina in codigo):
        codigoDisciplina = (input("escreva seu codigo(FIM para o programa): "))

print(f"Tabela {codigo} ")

prefixo = input('Digite um prefixo: ')
tamanh = len(prefixo)
if tamanh <= 5:
    qtd = 0
    for i in codigo:
        if prefixo == codigo[i][0]:
            print('  ', i, codigo[i][1][2][3])
    if qtd == 0:
        print(' Nenhum Codigo foi encontrado')
    codigoDisciplina = codigoDisciplina = (input("escreva seu codigo(FIM para o programa): "))
print('Fim do programa')
