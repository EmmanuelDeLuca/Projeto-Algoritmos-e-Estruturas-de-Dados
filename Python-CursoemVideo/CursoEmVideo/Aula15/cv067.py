while True:
    n = int(input("Digite o valor para tabuada: "))
    
    if n >= 0:
        cont = 0
        while cont < 10:
            cont += 1
            mult = n * cont
            print(f'{n} x {cont} = {mult}')
    else:
        break