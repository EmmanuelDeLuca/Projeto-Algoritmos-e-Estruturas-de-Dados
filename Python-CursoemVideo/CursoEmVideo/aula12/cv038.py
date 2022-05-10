# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais
a = float(input("Digite um numeo: "))
b = float(input("Digite um numero: "))
numero = a
if(b>a):
    numero = b
    print(f'{b} é maior que {a}')
    print(f'{a} é o menor ')
elif(a>b):
    print(f'{a} é mairo que {b}')
else:
    print('iguais')