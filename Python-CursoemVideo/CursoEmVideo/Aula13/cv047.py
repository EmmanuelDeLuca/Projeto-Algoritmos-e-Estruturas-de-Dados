contador = 0
for i in range(1, 50):
    if i % 2 == 0:
        contador = contador + 1
        print(f'Os numeros pares: {i}')
print(f"Total de {contador} numeros  pares")