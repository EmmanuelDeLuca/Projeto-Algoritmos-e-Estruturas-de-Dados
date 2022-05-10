
# nA = int(input("Primeiro termo: "))
# razao = int(input("Razão: "))
# count = 1
# termo = 0
# while count <= 10:

#     print(f'{termo}')
#     termo += razao
#     count+=1

# print( 'fim')

na = int(input("Primeiro termo: "))
razao = int(input('Razão: '))
termo = na
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}')
        termo += razao
        cont+=1
    print('PAUSA')

    continuar = input("Deseja continuar [N = 0] ?").upper()
print( 'fim')
