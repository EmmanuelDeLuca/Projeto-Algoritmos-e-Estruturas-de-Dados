'''Calcular o fatorial de um numero inteiro lido'''
numero = int(input("Digite um numero qualquer inteiro: "))
resultado = 1
count = 1
while count <= numero:
    resultado = resultado * count
    count +=1


print(resultado)