# S2 = (2/500, - 5/490)
def intercalados2(n, num1 = 2, num2 = 5, den = 500, sin = 1):
    if n <= 1:
        if sin > 0:
            res = sin * num1/den
        else:
            res = sin * num2/den
    else:
        if sin > 0:
            res = sin * num1/den + intercalados2(n - 1, num1,num2, den - 10, sin * -1)
            res = sin * num2/den + intercalados2(n - 1,num1, num2, den - 10, sin * -1)
    return res
