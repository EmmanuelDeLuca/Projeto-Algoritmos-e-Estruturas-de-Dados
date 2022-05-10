# Cria um programa onde 4 jogadores joguem um dado e tenham resultado aleatorio.Guarde esses resultados em um dicionario.No final, coloque esse dicionario em ordem, sabendo que o vendedor tirou o maior numero no dado.
from math import dist
import random
from operator import itemgetter

jogador = 4
jogo = {
    'Jogador 1': random.randint(1,6),
    'Jogador 2': random.randint(1,6),
    'Jogador 3': random.randint(1,6),
    'Jogador 4': random.randint(1,6),
}
ranking = []

print("Valores sorteados")

for i,o in jogo.items():

    print(f"{i} tirou {o} no dado")

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Ranking dos jogadores')

for p, o in enumerate(ranking):
    
    print(f"{p+1} lugar: {o[0]} com {o[1]}")
    



    

