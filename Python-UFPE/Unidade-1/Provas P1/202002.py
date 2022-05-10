# Faça um programa Python para ler uma seqüência de números inteiros
# negativos – a leitura para quando um número não negativo for lido. No entanto, o usuário
# só deve poder digitar no máximo 300 números negativos. O programa deve imprimir as
# seguintes informações como resultado (nesta ordem):
# • Os números lidos cujos valores são negativos e são múltiplos de 5. A impressão
# destes números deve ser feita na ordem inversa da que foram lidos.
# • O maior número lido que seja múltiplo de 11.
# should_continue = True
n = 0
lista5 = []
lista11 = []
while should_continue and n <=300:
        N = int(input("Digite valores negativos ate 300(N>0 stop programa): "))
        if N >= 0:
            should_continue = False
        elif(N%5 == 0):
            lista5.append(N)
            print(f"Lista do 5: {lista5}")
            print("Ordem inversa da lista",lista5[::-1])
             #Maior numero da uma lista
        
        elif(N%11 == 0):
            lista11.append(N)
            print(f"Lista do 11: {lista11}")
            print('Maior multiplo de 11: ',max(lista11, key=int))
        
            
        