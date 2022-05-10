# Altere o programa anterior para garantir que o
# usuário digitará no máximo 1000 números.

n = int(input("Digite numeros maior ou igual a 10 (numeros negativos para programa): "))
numeros = []
while n > 0:
    if n < 10:
        print("Digite valores maiores ou iguais a 10: ")
    if n>=10 and n <=1000:
        numeros.append(n)
        n = int(input("Digite numeros maior ou igual a 10 (numeros negativos para programa): "))
print(numeros[::-1])