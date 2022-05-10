soma = 0
cont = 0
while True:
    n = int(input("Digite um numero (999 para parar): "))
    if n != 999:

        soma += n
        cont += 1
    else:
        if n == 999:
            break
print(f'A soma dos valores {cont} foi {soma}')
