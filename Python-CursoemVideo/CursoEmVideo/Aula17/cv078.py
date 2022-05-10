# lista = [0]
# menor = lista[0]
# maximo = lista[0]


# for i in range(1, 6):
#     num = int(input("Digite os valores: "))
#     lista.append(num)
#     for e in lista:
#         if e < menor:
#             menor = e

#     if e > maximo:
#         maximo = e
    
    
# print(maximo, menor)

# lista=[0,1,2,3,4]
# menor = lista[0]
# for e in lista:
#     if e < menor:
#         menor = e
# print(menor)

    
valores = []
for i in range(0, 5):
    valores[i] = (int(input('Digite um valor: ')))

print(f'''\nMaior valor digitado: {max(valores)}
Posição:''', end='')

for x in range(0, 5):
    if valores[x] == max(valores):
        print(x, end=' ')

print(f'''\n \nMenor Valor digitado: {min(valores)}
Posição: ''', end='')
for o in range(0, 5):
    if valores[o] == min(valores):
        print(o, end=' ')