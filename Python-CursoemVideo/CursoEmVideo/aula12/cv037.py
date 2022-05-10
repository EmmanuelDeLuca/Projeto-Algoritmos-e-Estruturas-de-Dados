
# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('''
    -1 para Binario
    -2 para Octal
    -3 para Hexadecimal
''')
opçao = int(input("Digite sua opção: "))

num = int(input("Digite um interio qualquer: "))


if opçao == 1:
    print(f'{num} convertido para BINARIO é igual {bin(num)}')
elif(opçao == 2):
    print(f'{num} convertido para OCTAL é igual {oct(num)}')
elif(opçao == 3):
    print(f'{num} convertdio para HEXADECIMAL é iggual a {hex(num)}')
else:
    print("Digite um numero valido")