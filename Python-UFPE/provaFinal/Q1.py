# def serieR (n, num1 = 105, num2 = -130, den = 25.0, pos = 1) :
# # Parâmetro den definido como float para funcionar também em Python 2
#     if pos == 1 : # Termos ímpares (positivos)
# res = num1 / den
#     else:
# res = num2 / den
# if n > 1 : # Caso geral -> recursão
# if pos == 1 :
# res = res + serieR (n - 1, num1 + 35, num2, den + 10, 2)
# else:
# res = res + serieR (n - 1, num1, num2 - 30, den + 10, 1)
# return res

def serieR(n, num1 = 150,den1 = 4, num2 = -145, den2 = 9, pos = 1):
    if pos == 1:
        res = num1 / den1
    else:
        num2/ den2
    if n > 1:
        if pos == 1:
            res = res + serieR(n-1, num1 - 10, den1 + 2, num2, den2, 2 )
        else:
            res = res + serieR(n-1, num1, den1, num2 - 10, den2 + 4, 1)
    return res

num = int(input("Digite um valor positovo (valor negativo parar o programa): "))
while num > 0:
    num = int(input("Digite um numero negativo para parar o programa"))
serie = serieR(num)
print("A serie com %d termos totaliza %.3f " %(num, serie))
    
