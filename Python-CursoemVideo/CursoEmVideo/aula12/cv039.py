# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input("Digite o ano de nascimento: "))
alistamento = 2021 - ano
if alistamento < 18:
    restar = 18 - alistamento
    print("Ainda vai se alistar")
    print(f'falta {restar} ano/mes para o seu alistamento militar')
elif(alistamento == 18):
    print("Hora de se alistar")
else:
    passou = alistamento - 19
    print(f'já passou do tempo. Passou {passou} anos')