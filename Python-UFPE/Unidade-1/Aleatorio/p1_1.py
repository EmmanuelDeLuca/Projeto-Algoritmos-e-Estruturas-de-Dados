'''print("soma dos valores par entre 50 e 100")
n = 0
for n in range(50, 101):
    if n%2==0:
        print(n,"Pares")
print("FIM")'''
'''
n = int(input())
fat=1
for i in range(2,n+1):
    fat = fat *i
print(n,i,fat)
'''
'''dizer qual numero é menor em FOR'''
'''
qtd = int(input())
for i in range (qtd):
    i = input("nome ")'''

#calcular os valores pares
'''soma = 0
for i in range(50, 101,2):
    print(i)'''

#fatorial
'''
a = int(input())
fat = 1
for i in range(2,a+1):
    fat= fat*i
    print(fat)'''
#maior que 
'''
qtd= int(input("Digite quantida de  numero: "))
menor = numero = 0
if a <= 0:
    print("ERROR! tem que ser maior que 0")
else:
    numero = int(input("digite um nuemr"))
    menor = numero
    for i in range(qtd-1):
        numero = int(input("digite o numero: "))
        if(numero < menor):
            menor = numero
    print("o menor numero digitado foi:", menor)'''

'''
a = 1
b = 2
for i in range(a+2, 100,):
    for x in range(2, 51):
        print(i,x)'''
'''numerador=1
denominador=1
contnum=2
contden=1
soma=numerador/denominador
for i in range (0,50):
    numerador+=contnum
    denominador+=contden
    soma+=numerador/denominador
    
print(soma)'''

a = int(input())
b = 0
for i in range(a+3):
    for x in range(500, 10):
        print(i,x)
    
        
    

    