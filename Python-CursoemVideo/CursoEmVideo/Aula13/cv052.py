# 1 - Só tem dois divisores ele mesmo e o 1
# Essa questão é matematica

# num = int(input("Digite um numero inteiro: "))
# div = 0
# soma = 0
# for i in range(1, num + 1):

#     if num  % i == 0:
#         print('\033[33m')
#         div += 1
#         soma = soma + i

#     else:
#         print('\033[31m')
#     print(f'{i}', end='')
# print(f'\n\033[mO numero {num} foi divisivel {div} vezes')

# if div == 2:
#     print(f"é primo {soma}")
# else:
#     print(f"Não é primo{soma}")

num = int(input('Digite valores: '))
soma = 0
div = 0
for i in range(1, num+1 ):
  if num % i == 0:
    div += 1
    
    print(f'{i}')
  
    if div == 2:
        soma = soma + i
    print('primo %d'%soma)