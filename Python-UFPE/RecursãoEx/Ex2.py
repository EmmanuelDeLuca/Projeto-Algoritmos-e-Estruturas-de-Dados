# S_2 = 0 - 1/100 + 2 - 3/100 + 4 - 5/100 + 6 + ...

def serie_2(n, num = 0, den_1 = 1, den_2 = -100):
    if n <= 1:
        res = num / den_1
    else:
        res = num / den_1 + serie_2(n-1, num + 1, den_2, den_1)
    return res

