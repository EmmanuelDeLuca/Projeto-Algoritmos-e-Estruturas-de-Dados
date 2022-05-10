
n = int(input('Digite valores maiores que zero: '))
# O Máximo Divisor Comum (MDC) de 2 números
# inteiros é o maior número inteiro que divide
# ambos sem deixar resto. Fazer um programa
# Python para: – Ler 2 números inteiros – verificar se são positivos.O Máximo Divisor Comum (MDC) de 2 números inteiros é o maior número inteiro que divide
# ambos sem deixar resto. Fazer um programa


mdc = []*n
while n !=0:
    a = int(input("Digite valores positivos: "))
    b = int(input("Digite valores positivos: "))
    if a and b > 0:
        while b !=0:
            resto = a%b
            a = b
            b = resto
        mdc.append(a)
        n = int(input('Deseja para o programa(0 - Para o programa) ? '))
    else:
        print("Error! Só valores maiores que zero. Digite novamente")

print(f'lista = {mdc}') 

num1 = int(input('digite um número positivo:'))
while num1 <= 0 :
    num1 = int(input('digite um número positivo:'))
    
num2 = int(input('digite outro número positivo:'))
while num2 <= 0 :
    num2 = int(input('digite um número positivo:'))
    
if num1 < num2:
    mdc = num1
else:
    mdc = num2

while num1 % mdc != 0 or num2 % mdc != 0 :
    mdc = mdc - 1

print('O MDC dos números:', num1, 'e', num2, 'é', mdc)

