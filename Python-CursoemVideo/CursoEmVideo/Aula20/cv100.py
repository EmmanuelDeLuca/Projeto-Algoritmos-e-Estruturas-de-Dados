from random import randint, random


def sorteia(lista):
  for cont in range(0, 5):
    n = randint(1, 10)
    lista.append(n)
  print(lista)

def somar(lista):
  soma = 0
  for i in lista:
    if i % 2 == 0:
      soma+= i
  print(f'SOMA DOS VALORES PARES: {soma}')
  
numero = list()
sorteia(numero)
somar(numero)