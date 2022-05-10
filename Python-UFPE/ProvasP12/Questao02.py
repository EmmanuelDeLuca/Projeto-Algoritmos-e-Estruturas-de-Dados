# Faça uma subrotina Python do tipo função recursiva para calcular a soma dos N primeiros
# termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o
# resultado da função. Observe que o símbolo “!” se refere ao fatorial do número e também que
# você não pode usar os comandos de repetição nesta questão.
# S = 3 + 5 / 2! + 15 / 3! + 30 / 4! + 75 / 5! + 180 / 6! + ...
# def fatorial(n):
#     if n == 0:
#         res = 1
#     else:
#         res = n * fatorial(n-1)

# def serie_2(n, num = 5, inc = 10 ):
#     if n < 1:
#         res = num/fatorial(n)
#     else:
#         res = num/fatorial(n) + serie_2(n-1, num + inc, inc + 10 )
#     return res

def fatorial(n):
    if n == 0:
        res = 1
    else:
        res = n * fatorial(n-1)
    return res

def serie_1(n, num_impar = 3, num_par = 5, den = 1, sin = 1):

    if n <= 1:
        if sin > 0:
            res = sin * num_impar/ fatorial(den)
        else:
            res = sin * num_par/ fatorial(den) 

    else:
        if sin > 0:
            res = sin * num_impar/fatorial(den) + serie_1(n - 1, num_impar, num_par * 6, den + 1, sin * -1 )
        else:
            res = sin * num_par/fatorial(den) + serie_1(n - 1, num_impar * 5, num_par, den + 1, sin * -1)
    return res