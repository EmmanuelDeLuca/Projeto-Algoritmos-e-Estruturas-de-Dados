print('_'*30)
print('LOJA SUPER BARATÃO')
print('_'*30)

soma = acima = menor = cont = 0
barato = ''
while True:
    

    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    cont +=1

    if preco:
        soma += preco

    if preco >= 1000:
        acima +=1

    if cont == 1:
        menor = preco
        barato = nome
    else: 
        if preco < menor:
            menor = preco
            barato = nome

    n = input("Deseja continuar cadastrando ? [S/N] ").upper()
    if n == 'N':
        break

print(f'Total comprado: {soma:.2f}\nProdutos acima de 1000: {acima}\nO produto mais barato foi {barato} custando {menor:.2f}')