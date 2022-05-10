# Faça uma função recursiva power(base, expoente) que, quando chamada, retorna
# base**expoente. Por exemplo: power(3, 4) = 3 * 3 * 3 * 3 = 81. Assuma que o expoente é um
# inteiro maior ou igual a 1.

def power(n, base = 0, expo = 1):
    if n < 1:
        res = base **expo
    else:
        res = base **expo + power(n-1, base + 1, expo + 1)
    return res
pow = power(5)



    