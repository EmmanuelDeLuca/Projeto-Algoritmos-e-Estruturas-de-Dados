# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time

print('''
    [0] - Pedra
    [1] - Papel
    [2] - Tesoura
    ''')
user = int(input("Qual sua jogada? "))
cpu = random.randint(0,2)
print("PEDRA")
time.sleep(1)
print("PAPEL")
time.sleep(1)
print("TESOURA")
time.sleep(1)
print('-'*40)

if cpu == 0: #Pedra
    if user == 0:
        print('empate')
    elif user == 1:
        print("Jogador venceu")
    elif user == 2:
        print(f'Computador venceu. Jogou {cpu}')
    else:
        print('Jogada invalida1')
elif(cpu == 1): #Papel
    if user == 1:
        print("Empate")
    elif user == 0:
        print(f'Computador venceu. Jogou {cpu}')
    elif user == 2:
        print("Jogador venceu")
    else:
        print('Jogada invalida2')
elif(cpu == 2): #Tesoura
    if user == 2:
        print('Empate')
    elif user == 0:
        print('Jogador venceu')
    elif user == 1:
        print(f'Computador venceu. Jogou {cpu}')
    else:
        print("Jogada invalida3")