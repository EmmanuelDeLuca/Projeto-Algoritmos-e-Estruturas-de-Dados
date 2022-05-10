import random

x = random.randint(1, 10)
choice = 1
user = int(input("Digite um numero entre 0 e 10:"))
while user != x:
    if user == x:
        print("Acertou")
    else:
        choice += 1
        print("Tente novamente")
        user = int(input("Digite um numero entre 0 e 10:"))

print(f'Você acertou!!! {choice} chances')

