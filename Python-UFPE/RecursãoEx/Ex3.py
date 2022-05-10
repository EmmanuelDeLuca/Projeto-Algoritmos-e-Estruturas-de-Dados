# S_3 = - 1/5 + 2/10 - 6/20 + 24/35 - 120/55 + ...

# 1 = -1/5
# 2 = +2/10
# 3 = -6/20
# 4 = +24/35

# 1- Fatorial em cima # 2- Incremento  embaixo mais uma somar no incremento

def fatorial(n): #Criando a função e colocando os argumentos
    if n <=1:    #Criando a condição de parada
        res = 1  #Retornando o valor
    else:
        res = n * fatorial(n-1) #Recursão de N e fatorial
    return res   #Retornadno o valor do resultado 

#Paramentos: n, num = 1, den = 5, inc = 5, sin = 1
def serie_3(n, num = 1, den = 5, inc = 5, sin = 1):
    if n <= 1:
        res = sin * fatorial(n)/ den
    else:
        res = sin * fatorial(n)/ den + serie_3(n-1, num + 1, den + inc, inc + 5, sin * -1)
    return res


