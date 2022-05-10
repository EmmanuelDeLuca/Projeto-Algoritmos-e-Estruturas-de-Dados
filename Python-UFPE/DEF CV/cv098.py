# Faça um programa que tenha uma função chamado contador(), que receba tres parametros: inicio, fim e passo e realize a contagem.
# seu programa tem que realizar três contagens através da função criada:
# A) de 1 até 10, de 1 em 1
# B) de 10 até 0, de 2 em 2
# C) Uma contagem personalizada

def contador(inicio, fim, passo):
    if inicio < fim:
        for i in range(inicio, fim, passo):
            print(i)
            
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}')
            cont -= passo

contador(1,11,1)

contador(10,1,2)
contador(int(input("INICIO")), int(input("FIM")), int(input('PASSO')))