# Fazer subrotinas recursivas para calcular o valor
# das seguintes séries – com n termos, onde n deve
# ser um parâmetro recebido na chamada:
# – S2 = 37*38/1 - 36*37/2 + 35*36/3 – 34*35/4 + ...

# def serie2(n, nu1 = 37, de = 1, sin = 1):
#     if n <= 1:
#         res = sin * nu1 * (nu1 + 1)/ de
#     else:
#         res = sin * nu1 * (nu1 + 1) / de + serie2(n-1, nu1-1, de+1, sin *-1 )
#     return res

def serie2(n, nu1 = 38, de=1):
    if n <= 1:
        res= nu1 * (nu1+1)/de
    else:
        if nu1%2==0:
            res = nu1*(nu1+1)/de - serie2(n-1, nu1-1, de+1)
        else:
            res = nu1*(nu1 + 1)/de + serie2(n-1, nu1-1, de+1)
    return res
n = int(input("Digite um termo: "))
num = serie2(n)
print(num)
