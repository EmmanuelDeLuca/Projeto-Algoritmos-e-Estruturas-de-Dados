# S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50
num = 0
den = 1
for i in range(99):
    soma = num/den
    num = num + 2
    den = den + 1
    print('A soma dos termos é %.2f' %soma)