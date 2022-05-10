# print("Fatorial de qualquer numero")
# fact = int(input("Dgitie o numero para o fatorial: "))
# n = 1
# for i in range(2, fact + 1):
#     n*=i
# print(n)

# def fatorial(num):
#     n = 1
#     for i in range(2, num + 1):
#         n*= i
#     return n
# # fat = fatorial(4)

# def fatorial(num):
#     if num < 2:
#         f = 1
#     else:
#         f = num * fatorial(num - 1)
#     print(f)
# fat = fatorial(5)

def fibonacci(num):
    anterior = 0
    proximo = 1
    soma = 0
    for i in range(2,num):
        soma = proximo + anterior
        anterior = proximo
        proximo = soma
    return soma

num = int(input("Digite um numero positivo: "))
while num <0:
    num = int(input("Digite um numero positivo: "))
lista = []
qtd = 0
while num > 0:
    qtd+=1
    num = int(input("Digite um numero positivo: "))
    lista.append(num)
# while qtd > 0:
    # print(fibonacci(num), f"é equivalente {num}")def melhoresClientes(nome = '', pontuacao_acima = 0):
    arq_melhores = open(nome, 'r')
    arq_melhordomelhor = open(nome + 'melhoresDecode.txt', 'w')
    cont = 0
    soma = 0
    with arq_melhores, arq_melhordomelhor:
         for linha in arq_melhores:
             matricula = linha[0:5]
             sexo = linha[6:7]
             pontos = linha[7:15]
             cliente = linha[16:36]
             if(int(pontos) > pontuacao_acima):
                 arq_melhordomelhor.write(f'{matricula} {pontos}')
                 cont+=1
                 soma+=1
    media = cont/soma
    print(f"O nome da empresa é {nome}.")
    print(f"Foram gravados {cont} registros.")
    print(f"A pontuação média dos melhores clientes é {media}.")

    # return None
# flag = False
# while not flag:
#     try:
#         N = int(input('Digite o numero de empresas: '))
#         while N <=0:
#             N = int(input('Digite o numero de empresas: '))
#     except ValueError:
#         print("Error. Digite um inteiro positvo")
#     else:
#         flag = True
# for i in range(N):
    nome = input('Digite o nome da empresa: ')
    pontuacao_acima = int(input("Digite um valor pra pontuação:"))


    

    
    
    

    




# # numero = int(input("Digite numero inteiro positivo: "))
# # while numero < 0:
# #     numero = int(input("Digite numero inteiro positivo: "))
# #Não Recursiva
# def fatorial(num):
#     f = 1
#     for i in range(2, num + 1):
#         f*=i
#     return f
# fat = fatorial(5)

# #Recursiva capacidade de resolver um problema aparti de um valor anterior
# def fatorial(num):
#     #CASO BASE
#     if num < 2:
#         f=1
#     else:
#         #CASO GERAL
#         f = num*fatorial(num-1)
#     return f
# fat = fatorial(5)

# #Recursão:
# def serieR(n, nu=1, de = 1.0):
#     if n <=1:
#         res = nu/de
#     else:
#         res = nu/de + serieR(n-1, nu+2, de +1)
#     return res
# #EXE DA VI D  EX1
# def s2(n, nu=37, de = 1):
#     if n%2==0:
#         S2 = nu/de - (n-1, nu*(nu+1)/de)
#     else:
#         S2 = nu/de + s2(n-1, nu*(nu+1)/de)
#     return S2

# #EXEMPLO DA VI D EX2
# def s3(n, nu1=2, de= 500):
#     res = nu1/de
#     de1 = -10
#     if n > 1:
#         for i in range(n):
#             if nu1 == 2:
#                 nu1 = -5
#                 res = nu1/de - s3(n-1, nu1*(nu1 + 1)/ de-de1)
#             else:
#                 S3 = nu1/de + s3(n-1, nu1*(nu1 + 1)/ de-de1)

# n = int(input("Digite um numero inteiro menor 50: "))
# while n > 50:
#     n = int(input("Digite um numero inteiro menor 50: "))


# EXEMPLO DO PROFESSOR Ex1:
# def series2(n, numl = 37, den = 1, sinal = 1):
#     res = sinal * num1 * (num1 + 1) / den
#     if n > 1 :
#         res = res + series2(n - 1, num1 - 1, den + 1, - sinal)
#     return res


# Questão da prova Q1

def questao1(n, num1 = 2, den1 = 1, num2 = -7, den2 = 5,):
    soma = 0
    for i in range(n):
        if i % 2 == 0:
            soma = soma + questao1(num1) / questao1(den1)
            num1 = num1 * 4
            den1 = den1 * 3
        else:
            soma = soma - questao1(num2) / questao1(den2)
            num2 = num2 + 6
            den2 = den2 + 4
        



n = int(input("Digite o valor de n: "))
while n < 1:
    n = int(input("N deve ser positivo. Digite novamente: "))
    num = questao1(n)
    print(num)