# Listas
# num = [2,5,9,1]
# num[2] = 3  --> troca de valores
# num.append(7)  --> Adicionando valores na lista
# num.sort()  --> organizando por ordem
# num.sort(reverse=True)  --> Ordem decrescente
# len(num) --> tamanho da lista
# num.insert(2, 0)  --> Na posição 2 ele ira colocar o 0 (posição, numero)
# num.pop()  removendo o ultimo numero
# num.remove(2) Caso tenha dois elementos igual o remove irá remover o primeiro
# print(num)
# ============================================

# usando lista na estrutura de repetição FOR
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o numero 5')
# =============================================

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for v in valores:
#     print(f'{v}...', end='')
# Index e valores
# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for c, v in enumerate(valores): Enumerate pega tanto a chave quanro valor
#     print(f'na posição{c} encontrei o valor {v}!', end='')
# print('cheguei ao final da lista')

# Lendos valores pelo teclado e colocando na lista

# valores = []
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores): Enumerate pega tanto a chave quanro valor
#     print(f'na posição{c} encontrei o valor {v}!', end='')
# print('cheguei ao final da lista')

# Percularidade do python
# a = [2,3,4,7]
# b = a
# b[2] = 8
# print(f'lista a : {a}')
# print(f'lista b : {b}')

# Copia de uma lista
# a = [2,3,4,7]
# b = a[:]
# b[2] = 8
# print(f'lista a : {a}')
# print(f'lista b : {b}')

# CACLCULANDO MEDIA
# [I] --> Forma de armazenar na lista sem precisar do append
# notas = [0,0,0,0,0]
# soma = 0
# for i in range(0, 5):
#     notas[i] = float(input("Digite suas notas: "))


#     soma += notas[i]
#     total = soma/5

# print(f'Media dos alunos: total somado {soma} media final {total}\n{notas}')

# Busca numero
# lista = [0,0,0,0,0]

# for i in range(0, 5):
#     lista[i] = int(input("Digite 5 valores %d: "%(i+1)))
# while True:
#     buscar = int(input("Digite o numero que quer busca(0 parar): "))
#     if buscar == 0:
#         break
#     print("voce escolheu o numero %d " %lista[buscar-1])

# tamanho de lista
# L = [12,9,5]
# len(L)

# Tamanho da lista com repetição
# l =[1,2,3]
# x =0
# while x < 3:
#     print(l[x])
#     x+=1
# Repetição com tamanho da lista usando len
# l = [1,2,3]
# x = 0
# while x < len(l):
#     print(l[x])
#     x+=1
# =====
# Ordem que foi digitados
# lista = []

# while True:
#     n = int(input("Digite os valores"))
#     if n == 0:
#         break
#     lista.append(n)
# x = 0
# while x < len(lista):
#     print(lista[x])
#     x+=1
# Outro metodo para adicionar na lista
# l = []
# l = l+[1]
# +++++++++

# lista1 = [1,2,3,4,5]
# lista2 = [1,2,3,4,5]
# lista3 = lista1 + lista2
# print(lista3)

# lista1 = [1, 2, 4, 5]
# lista2 = [1, 3, 4, 6]
# lista3 = []

# for i in lista1, lista2:

#     if lista1[i] == lista2:
#         print('Elementos iguais')
#     else:
#         lista3.append(lista1)
# print(lista3)
