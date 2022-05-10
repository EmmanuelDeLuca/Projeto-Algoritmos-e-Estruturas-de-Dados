num = 1
soma = count = maior = menor = 0
choice = 'S'
while choice != 'N':
    num = int(input("Digite valores (0 parar o programa): "))

    soma += num
    count += 1
    media = soma/count
    if count == 1:
        maior = menor = num
    else:
        if(num > maior):
            maior = num
            
        if(num < menor):
            menor = num

    choice = input("Deseja continuar [S/N] ? ").upper()
print(f'media {media}')
print(f'maior {maior} e menor {menor}')
    
