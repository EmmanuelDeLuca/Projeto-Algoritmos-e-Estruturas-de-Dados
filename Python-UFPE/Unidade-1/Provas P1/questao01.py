# Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo,
# onde o valor de N deve ser informado pelo usuário no início. O seu programa deve imprimir o
# resultado (com 4 casas decimais) da seguinte forma: “O valor da série com ... termos é ...”.
N = int(input("Digite um valor para N(N>0): "))
while N <= 0:
    N = int(input("Digite novamente um valor para N(N>0): "))
S= 0
numerado = 19
denominador = 1
for i in range(N):
    S+= (numerado/denominador)

    if numerado == 19 and denominador ==1:
        numerado = -70
        numerado -= 15
        denominador = 5
        denominador += 7
    else:
        numerado = 19
        numerado += 7
        denominador = 1
        denominador *= 2
    print("Para", N, "termos, o valor de S= %.4f" %S)
