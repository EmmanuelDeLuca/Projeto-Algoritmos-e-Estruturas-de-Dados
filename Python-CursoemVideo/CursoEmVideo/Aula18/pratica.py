# Listas compostas
# galera = list()
# dado = list()

# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# print(galera)

# CRIANDO MATRIZES
#=====LISTA LIVRO======#

# Acessando uma lista
# pegando os indeces
# para pegar todos os elementos sempre coloque um a mais [0:n+1]
# lista = [15,3,2]
# print(lista[0:3])

# Modificando uma lista:
# Chamamos a lista com o indice que desejamos modificar, logo apos
# passamos o que queremos modifcar na lista
#Lista[0] = 1
# lista = [15,2,3]
# lista[0]=1
# print(lista[0:3])

# Calculo de media
# lista = [1,2,3,4,5]
# soma = 0
# x = 0
# while x < 5:
#   soma += lista[x]
#   x+=1
# print(f"media {soma/x}")
# Calculo da media com notas digitadas

# Exercicio 6.1
# notas = [0,0,0,0,0,0,0]

# soma = 0
# x = 0

# while x < 7:
#   notas[x] = float(input("Notas %d:" % x))
#   soma+= notas[x]
#   x+=1
# x=0
# while x < 7:
#   print("notas: %d" %notas[x])
#   x+=1
# print("media = %d"%(soma/x))

# Trabalhando com indices

# numeros = [0,0,0,0,0]
# x=0
# while x < 5:
#   numeros[x]= int(input("Numero %d:" %(x+1)))
#   x+=1
# while True:
#   escolhido = int(input("Que posição você quer imprimir (0 - para sair): "))
#   if escolhido == 0:
#     break
#   print("Você escolheu o numero: %d" %(numeros[escolhido-1]))
vetor = [0]*4
index = 0
for x in range(0, 4):
    vetor[x] = int(input())

for i in vetor:
    if i <= 0:
        index += 1
        print(f"X{([index-1])} = 1") 
    else:
        index +=1
        print(f"X{([index-1])} = {i}")    
