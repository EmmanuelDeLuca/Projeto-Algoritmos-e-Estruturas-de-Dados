lista = [[] , []]
valor = 0
for i in range(1,8):
  valor = (float(input("Digite os numeros: ")))
  if valor % 2 == 0:
    lista[0].append(valor)
  else:
    lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Valores pares {lista[0]}')
print(f'Valores impares {lista[1]}')
      


