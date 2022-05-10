def sequenciaPaePg(n, num = 0, den = 1):
    if n <= 1:
        res = num/den
    else:
        res = num/den + sequenciaPaePg(n-1, num + 2, den * 2)
    return res
