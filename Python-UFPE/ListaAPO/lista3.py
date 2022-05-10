# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
num = int(input("Digite numeros reais: "))
lista = []
for i in range(num):
    num1 = int(input("Digite os vetores: "))
    lista.append(num1)
    lista.sort(reverse=True)
print(lista)