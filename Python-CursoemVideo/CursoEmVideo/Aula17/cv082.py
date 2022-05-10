L = []
par = []
impar = []
while True:
    num = int(input("Digite valores: "))
    L.append(num)
    b = input("Deseja continuar [N/S] ?  ").upper()
    if b == 'N':
        break

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Lista completa {L}')
print(f'Lista pares {par}')
print(f'Lista impares {impar}')
