while True:
    idade = int(input("Digite sua idade: "))
    sexo = input("Qual seu sexo ? [M/F] ").upper()
    acima20 =  homens = pessoas = 0

    if idade > 18:
        pessoas += 1 
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            acima20 += 1
    n = input("Deseja continuar ? [S/N] ").upper()
    if n == 'N':
        break
print(f'Pessoas maiores de 18 anos: {pessoas}\nHomens registrados: {homens}\nMulheres acima dos 20: {acima20}')

