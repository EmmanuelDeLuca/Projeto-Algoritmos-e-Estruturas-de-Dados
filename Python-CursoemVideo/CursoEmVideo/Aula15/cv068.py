import random

print('-='*30)
print('VAMOS JOGAR PARA OU ÍMPAR')
print('-='*30)

vitorias = 0
while True:

    jogador = int(input("Diga uma valor:"))
    tipo = input('Par ou Ímpar ? [P/I]: ').upper()
    computador = random.randint(1, 10)
    total = jogador + computador

    if tipo == 'P':
        if total % 2 == 0:
            vitorias+=1
            print('Você ganhou!!!')
        else:
            print("Você perdeu!!!")
            break
    elif tipo == 'I':
        vitorias+=1
        if total % 2 == 1:
            print("Você ganhou!!!")
        else:
            print("Você perdeu!!!")
            break
print(f'Você jogou {jogador} e o computador {computador} somando {total}')

if vitorias == 0:
    print("Game over! Você não ganhou nenhuma vez")
else:
    print(f'Gamer Over! O jogador ganhou {vitorias} vezes ')
        
        
        



