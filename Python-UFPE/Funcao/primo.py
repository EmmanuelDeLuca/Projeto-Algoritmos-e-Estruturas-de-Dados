# import math
# def primo(num):
#     raiz = int(math.sqrt(num))
#     i = 2
#     while (i <= raiz) and ((num%i)!=0):
#         i=i + 1
#     if i > raiz : 
#         i = 0
# numero = int(input("Digite um numero inteiro: "))
# res = primo(numero)
# if res == 0:
#     print(numero, "é primo")

# else:
#     print("Não é")

lista = [1,2,3,4,5,9,9,9,9]
qtd = 0
for i in lista:
    if i == 9:
        qtd +=1
        print(i, qtd)
valor9 = int(input("Digitie "))
valor5 = valor9 // 1000 % 10
print(valor5)