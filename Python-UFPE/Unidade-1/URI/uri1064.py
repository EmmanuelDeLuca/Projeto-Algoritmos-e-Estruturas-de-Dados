# num = int(input("Digite numero de entrada: "))
# soma = 0
# for i in range(num):
#     num = int(input("Digite numero de entrada: "))
#     if num > 0:
#         soma+=1
#     print(soma)
# notas = int(input("Digite o numero de notas: "))
# count = 0
# s = 0
# media = 0

# while count < notas:
#     num = float(input("Digite suas notas: "))
#     if num > 0:
#         s+=1
#         media+=num
#         count+=1
# print(media/s)

# alunos = int(input("Numeros de alunos"))
# count = 1
# soma = 0
# while count <= alunos:
#     print("Nota do aluno", count)
#     nota = float(input() )
#     soma+=nota
#     count+=1
# print(soma/alunos)
# 1)
# nome = str(input("Digite seu nome: "))
# count = 0
# for i in nome:
#     print(str.upper(i))

# 2)
# nome = str(input("Digite seu nome: "))
# for i in range(0, len(nome)+1):
#     print(nome[:i])

# 
# nome = str(input("diga seu nome"))
# for i in nome:
#     print(i)
# nome = str(input("Diga seu nome: "))
# for i in range(len(nome)):
#     print(nome[:i+1])

# nome1 = str(input("Diga o  nome: "))
# nome2 = str(input("Diga outro nome: "))
# vezes = 0

# print(nome2.find([-1]) == (nome1.find([-1])))

# PRIMEIRA QUESTÃO do PROFESSOR
# nome = str(input("diga seu nome: "))
# for c in range(len(nome)):print(nome[c])
valores = list(map(int(input("Digite valors:").split())))

valores1 = list(map(int(input("Digite valores:").split())))
soma = 0
for i in range(valores):
    for j in range(valores1):
        soma+= i + j
        print(soma)








