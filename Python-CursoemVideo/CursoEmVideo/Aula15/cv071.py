import random
print('='*30)
print('        BANCO DECODE    ')
print('='*30)

valor = int(input("Quanto você deseja sacar ? "))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
