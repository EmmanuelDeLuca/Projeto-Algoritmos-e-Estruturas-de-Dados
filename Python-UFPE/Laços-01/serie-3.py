# S = 37*38/1 + 36*37/2 + 35*36/3 + ...
num = 37
den = 1
N = int(input("Digite um numero: "))
for i in range(N):
    soma = num * (num + 1)/den
    num = num - 1
    den = den + 1
    print(soma)