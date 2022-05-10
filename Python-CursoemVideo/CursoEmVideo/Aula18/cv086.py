# matriz = []
# for i in range(3):
#   matriz.append([])
#   for j in range(3):
#     valor=(int(input('digite valor de ['+str(i)+ ','+ str(j)+ ']:')))
#     matriz[i].append(valor)
# for i in range(3):
#   print(matriz[i])
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz [l][c]= int(input(f'Digite um valor para {l} e {c}: '))
for i in matriz:
    print(i)