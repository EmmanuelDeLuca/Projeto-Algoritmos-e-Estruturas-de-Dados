N = int(input("Digite um valor maior que 50: "))

S = 0
P = 1

numerador = 2
denominador = 500
while P <= N:
    S+=numerador/denominador
    denominador -= 10

    if numerador == 2:
        numerador = -5
    else:
        numerador = 2
print(S)

