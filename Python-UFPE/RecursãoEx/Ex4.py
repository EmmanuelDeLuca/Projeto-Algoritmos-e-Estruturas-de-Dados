# S_4 = 1/2 + 0 + 1/4 + 0 + 1/8 + 0 + ...

def serie_4(n, den = 2, sin = 1):
    if n <= 1:
        if sin > 0:
            res = 1/den
        else:
            res = 0/den
    else:
        if sin > 0:
            res = 1/den + serie_4(n-1, den, sin * -1)
        else:
            res = 0/den + serie_4(n-1, den*2, sin * -1)
    return res