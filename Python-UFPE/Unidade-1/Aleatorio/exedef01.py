# – Ler números inteiros positivos de até 5 dígitos (consistir)
# e imprimir quantas vezes o dígito 9 ocorre em cada um.
# – A leitura pára com número negativo ou zero.
# – Escrever subrotina que deve desmembrar o valor do
# número em seus 5 dígitos, retornando o resultado em
# uma lista de tamanho 5.
# – Escrever outra subrotina que usa a anterior e que:
# • Recebe como parâmetros um número positivo até 99999
# e um algarismo inteiro (0 a 9), nesta ordem.
# • Retorne como resultado a quantidade vezes que o
# algarismo aparece no número

def quebra_numeros(num):
    lista = [0]*5
    i = 0
    while num != 0:
        lista[i] = num % 10
        num//=10
        i+=1
    return lista
def 



numero = int(input("Digite um numero positovo de até 5 digitos: "))
while numero > 99999:
    numero = int(input("digite novamente. Digite um numero positovo de até 5 digitos: "))
qtd = int(input("Digite um valor postivo entre (0 e 9)"))
while qtd < 0 and qtd > 9:
    qtd = int(input("DIGITE NOVAMENTE. Digite um valor postivo entre (0 e 9)"))


