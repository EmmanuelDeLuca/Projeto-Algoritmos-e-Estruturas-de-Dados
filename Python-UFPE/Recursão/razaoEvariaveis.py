# S3 = (150/20, - 156/30)
def razao(n, num1 = 150, num2 = 142, den = 10, inc = 10, sin = 1):
    if n <= 1:
        if sin > 0:
            res = sin * num1/ den
        else:
            res = sin * num2/ den
    else:
        if sin > 0:
            res = sin * num1/ den + razao(n - 1, num1, num2 + 14, den + inc, inc + 10, sin * -1)
        else:
            res = sin * num2/ den + razao(n - 1, num1 + 12, num2, den + inc, inc + 10, sin * -1)
    return res