#Facilitando o entendimento: precisamos criar uma variavel para armazenar o maior e o menor numero
primeiro = float(input("Digite o primeiro numero: "))
segundo = float(input("Digite o segundo numero: "))
terceiro = float(input("Digite o primeiro numero: "))

maior = primeiro

menor = primeiro

if(segundo > maior):
    maior = segundo
    
if(terceiro > maior):
    maior = terceiro
print(maior)

if(segundo < menor):
    menor = segundo
if(terceiro < menor):
    menor = terceiro
print(menor)

