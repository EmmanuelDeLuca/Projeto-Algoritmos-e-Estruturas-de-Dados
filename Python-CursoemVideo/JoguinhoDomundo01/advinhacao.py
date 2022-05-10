# print('-'*60)
# print('                   \033[4;31m Jogo da advinhação')
# print('-'*60)

# print('--------Menu--------')
# print('1 - Continuar jogando')
# print('0 - sair')

# num = int(input("Digite um numero do menu: "))

# if num == 1:

#     user = float(input("Digite um numero para adivinhar entre(0 e 25)"))
#     advinhar = 24

#     if user == advinhar:
#         print("Parabenns!! Você ganhou!")
#     elif(user > advinhar):
#         print('Você passou do numero')
#     elif(user < advinhar):
#         print("digitou um numero menor")
#     else:

#         print("Você errou!")
# elif(num == 0):
    
#     print('Saindo...')

#Com o comando WHILE

print('''

    [1] Jogar

        Você terá 3 tentativas para acerta o numero
    
''')
num = int(input("Digite [1] para iniciar o jogo: "))
tentativas = 3
rodada = 0

while (rodada < tentativas):
    if num == 1:
        user = float(input("Digite um numero (maior > 1 e menor < 25):\n "))
        advinhar = 20
        
        
        if user == advinhar:
            print('Parabéns,você ganhou!')
            break
        elif(user > advinhar):
            print('Você passou do numero')
        elif(user < advinhar):
            print("digitou um numero menor")
        else:
            print("Você errou!")

    rodada = rodada + 1

    print(f'Voce está na {rodada} rodadas de {tentativas} tentativas')
   
    # num = int(input("Dsejar continuar ?\n[0] Sair\n[1] Continuar jogando"))
print("Fim de jogo")




