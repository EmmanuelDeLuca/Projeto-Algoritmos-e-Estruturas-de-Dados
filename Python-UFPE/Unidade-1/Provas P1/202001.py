N = int(input("Digite um numero(N>0): "))
while N < 0:
    N = int(input("Error. Digite novamente um numero(N>0): "))

S = 0
numerador = 150
denominador = 20
for i in range(N):
    S+= numerador/denominador
     
    if numerador == 150 and denominador == 20:
        numerador = -156
        # numerador -= 14
        denominador += 10

    else:
        numerador += numerador + 6
    print(S)

# S = 0
# denominador = 150
# for numerador in range(1,N, 10):
#     S+= numerador/denominador
#     denominador -= 6
# print