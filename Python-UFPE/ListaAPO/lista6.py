# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores
# num = int(input("Digite o numero de entradas: "))
# lista = []
# listaPar = []
# listaImpar = []
# for i in range(num):
#     number = int(input("Digite uma sequencia de valores: "))
#     lista.append(number)
#     if number%2==0:
#         listaPar.append(number)
#     else:
#         listaImpar.append(number)
# print(f"Lista completa: {lista}, lista PAR: {listaPar}, Lista Impar: {listaImpar}")
    
# Questão 1 do Slide
# n = int(input('digite o tamanho dos vetores: '))
# vetor1 = [0]*n
# vetor2 = [0]*n
# res = [0]*n

# for i in range(n):
#     valor1 = int(input('Digite o elemento ' + str(i) + ' na lista 1: '))
#     vetor1[i] = valor1

# for i in range(n):
#     valor1 =  int(input('Digite o elemento ' + str(i) + ' na lista 2: '))
#     vetor2[i] = valor1
#     res[i] = vetor1[i] + vetor2[i]

# print(vetor1, '+', vetor2, '=', res)
# Questão 2 do Slide
# n = int(input("Digite o número de termos que deseja dentro da lista: "))
# lista = [0]*n
# lista_pares = [0]*n
# lista_impares = [0]*n
# tampar = 0
# tamimp = 0

# for i in range(n):
#     valor = int(input("Digite um valor para a lista: "))
#     lista[i] = valor
#     if valor % 2 != 0:
#         lista_impares[tamimp] = valor
#         tamimp = tamimp + 1
#     else:
#         lista_pares[tampar] = valor
#         tampar = tampar + 1
# lista_pares = lista_pares[:tampar]
# lista_impares = lista_impares[:tamimp]


# print("Lista digitada:", lista)
# print("Lista dos números pares:", lista_pares)
# print("Lista dos números ímpares:", lista_impares)
# Questão 3 Slide
# n=int(input("Digite de quantos alunos deseja analisar as notas: "))
# notas = [0]*n
# media=0
# acima=[]

# for i in range (n):
#     nota=int(input(f"Digite a {i+1} nota: "))
#     media+=nota
#     notas[i] = nota

# media=media/n
# for c in range (n):
#     if notas[c]>=media:
#         acima.append(notas[c])

# print(f"A média das {n} notas é igual a {media} e as notas aprovadas foram: {acima}")

# questão 4 Slide
# n = int(input("Digite um número (negativo para parar): "))
# lista = []
# lista_digitos = []
# while n > 0:
#     lista.append(n)
#     if n >= 10:
#         lista_digitos.append(n)
#     n = int(input("Digite um número (negativo para parar): "))
# lista_digitos.reverse()
# print(lista_digitos)

