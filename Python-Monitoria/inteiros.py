'''Somar os inteiros pares entre 50 e 100(inclusive)'''
numero = 50 #Entrada com 50
somar=0 #Soma vai adiquirindo o valor da soma de Numeros
while numero <= 99: #Enquanto numero for menor ou igual ele continuara executando
    if numero%2==0: #Se numero for um numero par
        somar = somar + 1 # ele irá somar mais UM
    numero = numero+1 #Na variavel numero ele irá adicionar +1 até o 100
print(somar)
