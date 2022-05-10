import math
import random
tupla = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
for i in tupla:
    print(f'O numero gerado foi: {i}')
print(f'O maior numero gerado: {max(tupla)}')
print(f'O menor numero gerado: {min(tupla)}')