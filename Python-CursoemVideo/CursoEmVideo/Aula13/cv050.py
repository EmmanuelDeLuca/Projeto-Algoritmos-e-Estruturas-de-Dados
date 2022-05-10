
soma = 0
for i in range(1,7):
    numeros = int(input("Digite 6 valores inteiros: "))
    if numeros % 2 == 0:
        soma += numeros
print(f"Somas dos pares: {soma}")