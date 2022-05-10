


# def crie_matriz(n_linhas, n_colunas): 
    # qteInstrucoes = []
ns =[1, 2, 3, 40]
qtdeInstrucoes = []
for N in ns:
    contInstrucao = 0
    n_linhas = range(N)
    n_colunas = range(N)

    
    
    matriz = []
    contInstrucao+=1
    for i in range(N):
        contInstrucao+=1
        linha = [] 
        for j in range(N):
            contInstrucao+=1
            matriz.append(N)
        print(matriz) 
    qtdeInstrucoes.append(contInstrucao)
print(qtdeInstrucoes)        
	
# A = crie_matriz(n_linhas = 3, n_colunas=3)

# ns =[3, 4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,
#   21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
#   39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54,  55,  56,
#   57,  58,  59,  60,  61,  62,  63,  64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,
#   75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,
#   93,  94,  95,  96,  97,  98,  99, 100,]
# for N in ns:
#     n_linhas = range(N)
#     n_colunas = range(N)

# A = crie_matriz(n_linhas = 2, n_colunas= 2)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import PolynomialFeatures

def f1(N):
  return N*3
ns =[1, 2, 3, 40]
qtdeInstrucoes = []
for N in ns:
    contInstrucao = 0
    n_linhas = range(N)
    n_colunas = range(N)

    
    
    matriz = []
    contInstrucao+=1
    for i in range(N):
        contInstrucao+=1
        linha = [] 
        for j in range(N):
            contInstrucao+=1
            matriz.append(N)
        # print(matriz) 
    qtdeInstrucoes.append(contInstrucao)
qtdeInstrucoesTeorica = [f1(N) for N in ns]
# print(qtdeInstrucoes)   


plt.plot(range(len(qtdeInstrucoes)),qtdeInstrucoes , label="quad")
plt.plot(range(len(qtdeInstrucoesTeorica)),qtdeInstrucoesTeorica , label="f1")

print(qtdeInstrucoes)
print(qtdeInstrucoesTeorica)

plt.legend()

plt.show()