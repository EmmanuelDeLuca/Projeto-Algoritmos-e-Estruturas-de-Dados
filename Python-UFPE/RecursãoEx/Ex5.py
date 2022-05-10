# S_5 = 0 + 1/4 + 0 + 1/16 + 0 + 1/64...
def serie_5(n, den = 2, sin = 1):
    if n <= 1:
        if sin > 0:
            res =  0/ den 
        else:
            res =  1/ den
    else:
        if sin > 0:
            res = 0/ den + serie_5(n-1, den * 2, sin * -1)
        else:
            res = 1/ den + serie_5(n-1, den * 2, sin * -1)
    return res