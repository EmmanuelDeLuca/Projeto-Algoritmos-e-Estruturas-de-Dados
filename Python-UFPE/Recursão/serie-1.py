# Exemplo: S = 1 + 3/2 + 5/3 + 7/4

def SerieR(n, nu = 1, de= 1.0 ):
    if n <= 1:
        res = nu/de
        
    else:
        res = nu/de + SerieR(n-1, nu + 2, de + 1) #Função Recursiva 
    return res

n = int(input("Digite um valor: "))
num = SerieR(n)
print(num)

