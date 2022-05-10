def pareec(n, razao = 0):
    if n <= 1:
        res = razao
    else:
        res = pareec(n-1, razao + 2)
    return res
