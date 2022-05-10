# Fatorial em SubString
def fatorial(num):
    f=1
    for i in range(2,num+1):
        f=f*i
    return f
fat = fatorial(5)

# Fatorial em Recursão
def fatorial_rec(num):
    if num < 2:
        f=1
    else:
        f = num * fatorial_rec(num -1)
    return f
fat = fatorial_rec(5)