# Faça um programa Python para ler uma seqüência de números inteiros – a leitura pára
# quando o número zero for lido. O programa deve imprimir as seguintes informações como
# resultado (nesta ordem):
#  A quantidade total de números digitados.
#  O maior número lido que seja múltiplo de 11.
#  Os números lidos cujos valores têm 3 dígitos significativos. A impressão destes números
# deve mostrar primeiro os números negativos (de 3 dígitos) e depois os positivos (idem).
#  A média aritmética dos números impressos no item anterior (todos os de 3 dígitos)
N = int(input("Digite um numero(0 parar o programa): "))
lista11 = []
i = 0
o = 0
b = 0
soma = 0
while N != 0:
    if N%11==0:
        i+=1
        lista11.append(N)
        print(f'Lista com todos os valores multiplos de 11: {lista11}')
        print('Maior multiplo de 11: ', max(lista11, key=int))
    elif(N >= 100 and N <= 999):
        o+=1
        negativo = N * (-1)
        print(f'Numeros negativos: {negativo}')
        print('Numeros positivos: ',N)
        soma+= N
        media = soma/o
        print(f"Media = {media}")
    else:
        b+=1
        print("Não é multiplo de 11 ou  nem esta entre 100 1 999")

    N = int(input("Digite um numero(0 parar o programa): "))   
    
print(f'Numero digitados: {i+o+b}')


