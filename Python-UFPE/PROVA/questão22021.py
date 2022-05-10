# Faça um programa Python para ler uma seqüência de números inteiros negativos – a leitura
# pára quando o número zero for lido. No entanto, o usuário só deve poder digitar no máximo
# 150 números negativos. O programa deve imprimir as seguintes informações como resultado
# (nesta ordem):
#  Os números lidos cujos valores têm 2 dígitos significativos e também são múltiplos de 5.
# A impressão destes números deve ser feita na ordem inversa da que foram lidos.
#  O maior número lido que não seja múltiplo de 7.
# should_continue = True
# quantidade_numeros = 0

# while should_continue and quantidade_numeros < 150:
#   N = int(input("Digite valores  negativos : "))
#   if N > 0:
#     should_continue = False
# TÁ DANDO ERRO ESSA PARTE DE CIMA, INFELIZMENTE N TIVE TEMPO PARA CHEGAR AO ACERTO
N = int(input("Digite numero ate 150 negativos(0 parar o programa): "))
lista5 = []
lista7 = []
while N < 0:
    if N<= -10 and N >= -99:
        if (N%5==0):
            lista5.append(N)
        print(f'Lista com todos os valores multiplos de 5: {lista5}')
        print('Ordem inversa: ', lista5[::-1])
    elif(N%7!=0):
        lista7.append(N)
        print('Maior numero lido que não é multiplo de 7: ', max(lista7, key=int))
    
    
    N = int(input("Digite um numero(0 parar o programa): "))   
    

