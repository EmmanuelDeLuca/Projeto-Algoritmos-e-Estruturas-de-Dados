# S = 2/500 - 5/490 + 2/480 - 5/470 + ...
N = int(input("Digite um numero: "))

num = 2
# num = 5
den = 500
for i in range(N):
    if num%2 == 0:
        soma = num/den
        num = -5
        den -= 10
    else:
        soma = num/den
        num = 2
        den -= 10
    print('a soma das series %.6f'%soma)



