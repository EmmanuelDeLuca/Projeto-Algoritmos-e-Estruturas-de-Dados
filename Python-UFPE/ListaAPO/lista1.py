# Crie um programa em Python que peça seu nome, sua idade, sua altura, seu
# peso e True se for casado ou False para solteiro.
# Em seguida, ele deve armazenar todas essas informações numa lista 
# chamada eu. Por fim, imprima essa lista na tela.
nome = str(input("Diga seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
op = int(input("Estado civil:\n 1.casado\n2.solteiro\n"))
if op ==1:
    op=True
if op ==2:
    op=False
eu = [nome,idade,altura,peso,op]
print(eu)