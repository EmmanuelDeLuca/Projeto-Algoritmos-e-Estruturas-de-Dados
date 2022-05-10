lista = []
princ = []

maiorPeso = menorPeso = 0
while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))
    if len(princ) == 0:
        maiorPeso = menorPeso = lista[1]
    else:
        if lista[1] > maiorPeso:
            maiorPeso = lista[1]
        if lista[1] < menorPeso:
            menorPeso = lista[1]
    princ.append(lista[:])
    lista.clear()

    b = str(input("Deseja continuar [S/N] ?")).upper()
    if b == 'N':
        break

print(f'Pessoas cadastrada{len(princ)}')

for e in princ:
    if e[1] == maiorPeso:
        print(f'Maior peso {e[0],e[1]}')
for p in princ:
    if e[1] == menorPeso:
        print(f'Menor peso {e[0],e[1]}')
