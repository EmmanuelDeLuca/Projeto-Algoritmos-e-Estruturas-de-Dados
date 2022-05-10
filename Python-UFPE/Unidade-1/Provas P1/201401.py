# Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo. O
# valor de N deve ser lido no início e deve ser positivo. 
# S = 100 / 1! – 13 / 2! + 95 / 3! – 24 / 4! + 90 / 5! – 35 / 6! + ...

N = int(input("Digite um valor para N(N>0): "))
while N < 1:
    N = int(input("Error! Digite um valor para N(N>0): "))
S = 0
valor_par = 100 #-5
valor_impar = -13 # 1+1!
for i in range(N):
    fatorial = 1
    for x in range(i+1, 1, -1):
        if i == 0: pass
        else: fatorial *=x
    if i%2==0:
        S+= valor_par/fatorial
        valor_par -= 5
    else:
        S+= valor_impar/fatorial
        valor_impar -= 11    
        
print(f"A soma dos termos {N} tem um valor {S}")

