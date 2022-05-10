# Faça uma subrotina Python do tipo função chamada MultiplicaDigitos, que receba um
# número Num inteiro positivo de 6 dígitos como parâmetro, e devolva a multiplicação dos
# dígitos não nulos deste número como resultado. Caso Num não seja positivo ou tenha mais de
# 6 dígitos significativos, a função deve retornar como resultado -1 ou -2, respectivamente.

# Dica - O resto da divisão de um número por 10 retorna o dígito mais à direita, enquanto que a
# divisão inteira dele por 10 retorna a outra parte. Ex: 1234 % 10 -> 4 e 1234 // 10 -> 123.
# Este processo pode ser repetido para recuperar cada um dos dígitos de qualquer número.

# OBS - Você pode (ou não) incluir um programa principal para ler um valor de N e testar a sua
# função: somente a função será avaliada na correção.
import math

def multiplicaDigitos(num):
    algarismos = [0] * 6
    pos = 0
    if num > 999999 :
        return -2
    else:

        while num != 0:
            algarismos[pos] = num % 10
            num//=10
            pos+=1
        
        
        return algarismos
     
num = int(input("Digite um numero: "))
while num > 999999:
    num = int(input("Digite novamente. Digite um numero: "))
print(math.prod(multiplicaDigitos(num)))


# fat = multiplicaDigitos(num)
# print(fat)
def multiplicaDigitos(num):
    if num > 999999:
        return -2
    elif num < 1:
        return -1
    else:
        mult = 1
        while num > 0:
            if num %10 !=0:
                mult = mult * (num % 10)
            num = num // 10
    return mult

erro = True
while erro:
    try:
        num = int(input("Digite um numero inteiro: "))
        erro = False
    except:
        print("Erro.")

