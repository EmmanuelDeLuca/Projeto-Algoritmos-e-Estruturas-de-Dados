media = 0
count = 0
countMulher = 0
for pessoas in range(1,5):

    nome = input("Digite seu nome: ")
    idade = int(input("Digite seu idade: "))
    sexo = input("Diga seu sexo: ").lower()

    maisVelho = idade

    if idade:
        media += idade
        count = count + 1
        meidaTotal = media/count

    elif(sexo == 'masculino'):
        if idade > maisVelho:
            maisVelho = idade

    elif(sexo == 'feminino'):
        if idade < 20:
            countMulher += 1
    else:
        print("Digite os valores validos")

print(f'Media de idade do grupo {meidaTotal} anos')
print(f'homem mais velho {maisVelho} {nome}')
print(f'Mulheres abaixo dos 20 anos {countMulher}')
    

