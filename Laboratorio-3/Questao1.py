def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2 
    print(A[meio])
    if A[meio] == item:
        return meio
    elif A[meio] > item:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: 
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)


A =[13, 16, 21, 28, 37, 48, 61, 76, 93, 112, 133, 156, 181, 208, 237, 268, 301, 336, 373, 412, 453, 496, 541, 588, 637, 688, 741, 796, 853, 912, 973, 1036, 1101, 1168, 1237, 1308, 1381, 1456, 1533, 1612, 1693, 1776, 1861, 1948, 2037, 2128, 2221, 2316, 2413, 2512, 2613, 2716, 2821, 2928, 3037, 3148, 3261, 3376, 3493, 3612, 3733, 3856, 3981, 4108, 4237, 4368, 4501, 4636, 4773, 4912, 5053, 5196, 5341, 5488, 5637, 5788, 5941, 6096, 6253, 6412, 6573, 6736, 6901, 7068, 7237, 7408, 7581, 7756, 7933, 8112, 8293, 8476, 8661, 8848, 9037, 9228, 9421, 9616, 9813]

print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 450))

