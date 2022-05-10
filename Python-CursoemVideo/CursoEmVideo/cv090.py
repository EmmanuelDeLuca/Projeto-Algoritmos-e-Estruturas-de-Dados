# Faça im programa que leia o nome e a media de um aluno, guardando tambem a situação em um dicionario.No final, mostre o conteudo da estrutura na tela

aluno = dict() #{}

aluno['nome'] = (input('Digite seu nome: '))
aluno['media'] = float(input(f"Media de {aluno['nome']}:  "))
if aluno['media'] >= 7.0:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'
print('-='*30)
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')