# s1 = (37*38/1, - 36*37/2)

def intercalados(n, num1 = 37, num2 = 38, den = 1, sin = 1):
    if n < 2:
        res = sin * num1 * num2/ den
    else:
        res = sin * num1 * num2/ den + intercalados(n - 1, num1 - 1, num2 - 1, den + 1, sin * -1)
    return res

# exemplo 2 de Resposta:
# def intercalados(n, num1 = 37, num2 = 38, den = 1, sin = 1):
#     if n < 2:
#         res = num1 * num2 / den
#     else:
#         res = sin * num1 * num2 / den + intercalados(n - 1, num1 - 1, num2 - 1, den + 1, sin * -1)
#         res = sin * num1 * num2 / den + intercalados(n - 1, num1 - 1, num2 - 2, den + 1, sin * - 1)
#     return res
# RESPOSTA CERTA :
def intercalados(n, num1 = 37, den = 1, sin = 1):
    if n <= 1:
        res = (sin * num1 * (num1 + 1))/ den
    else:
        res = sin * num1 * (num1 + 1)/ den + intercalados(n - 1, num1 - 1, den + 1, sin * - 1)
    return res