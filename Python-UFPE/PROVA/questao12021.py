# Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo,
# onde o valor de N deve ser informado pelo usuário no início. O seu programa deve imprimir o
# resultado (com 4 casas decimais) da seguinte forma: “O valor da série com ... termos é ...”.
# S = 2 – 7 / 5 + 8 / 3 – 13 / 9 + 32 / 9 – 19 / 13 + 128 / 27 ...
N = int(input("Digite um numero N: "))
while N < 1:
    N = int(input("Digite um numero N maior que zero: "))


S = 0
#Recebendo o primeiro valor
numerado1 = -5
numerado2 = 8
denominador1 = 5
denominador2 = 3
#Colocando no laço para determina se for maior faça isso, caso contrario faça isso.
for i in range(N):

    if numerado1 < 0:
        numerado1 = 10
        denominador1 += 5
    elif(numerado2>0):
        numerado2 = 8*4
        denominador2 *= 3
    S+= numerado1/denominador1
print(f'Ovalor da série com {N} termos é %.4f'%S)   
