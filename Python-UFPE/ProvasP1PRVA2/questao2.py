# – Faça uma subrotina Python do tipo função recursiva para calcular a soma dos N primeiros
# termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o
# resultado da função.
# S = 105 / 25 – 130 / 35 + 140 / 45 – 160 / 55 + 175 / 65 – 190 / 75 ....
# OBS1 - Observe que você não pode usar os comandos de repetição nesta questão.
# OBS2 - Você pode (ou não) incluir um programa principal para testar a sua função: somente
# a função será avaliada na correção.

def serie_1(n, num1 = 105, num2 = 130, den1 = 25, den2 = 35, sin = 1):
    if n <= 1:
        if sin > 0:
            res = sin*num1/den1
        else:
            res = sin*num2/den2
    else:
        if sin > 0:
            res = sin*num1/den1 + serie_1(n-1, num1, num2 + 30, den1, den2 + 20, sin * -1)
        else:
            res = sin*num2/den1 + serie_1(n-1, num1 + 35, num2, den1 + 20, den2, sin * -1 )  #Pq de inverter Num1 e Num2, pois estão em paralelas, logo uma vez de cada.
        return res 
fat = serie_1(2)
print(fat)
#Rotina
# erro = True
# while erro:
# 	try:
# 		n = int(input("Digite um número inteiro: "))

# 		erro = False
# 	except:
# 		print("Erro.")

# res = serie_1(n)
# print(res)