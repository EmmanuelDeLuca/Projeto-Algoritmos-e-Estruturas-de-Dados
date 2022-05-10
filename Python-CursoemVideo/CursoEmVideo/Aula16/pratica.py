# Tuplas são imutaveis
lanche = ('Hambuguer', 'Suco', 'Pizza', 'Pudim')

# Não precisa de posição
for i in lanche:
    print(f'eu vou comer {i}')

# 1- opção Mostra posição e contador
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# 2- opção Mostra posição e contador
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# Sorted = organizado (colocando em ordem)
print(sorted(lanche))

# Tuplas
# count (ver quantas vezes aparece)
# index ==> ve a posição do numero
# del == apagando 
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)