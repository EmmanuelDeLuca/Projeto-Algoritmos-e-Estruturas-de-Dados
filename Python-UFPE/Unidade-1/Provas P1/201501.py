N = int(input('Digite um valor para N(N>0): '))
while N < 1:
    N = int(input('Erro.Digite  novamente um valor para N(N>0): '))
print(N)
S = 0
numerador = 10
denominador = 1
for i in range(N):
    S+= numerador/denominador
    if numerador == 10 and denominador == 1:
        numerador = -15
        numerador -= 10
        denominador = 2
    else:
        numerador = 10
        numerador += 10
        denominador = 1
        denominador *= 4
    print(S)