# def busca_sequencial(lista, x):
#     cont = 0
#     for i in range(len(lista)):
#         cont = cont + 1
#         if lista[i] == x:
#             print(x, cont)
#     return -1
# lista = [12, 16, 22, 30, 40, 52, 66, 82, 100]
# busca_sequencial(lista, 100)

def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    cont = 0
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


A = [12, 16, 22, 30, 40, 52, 66, 82, 100]
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 100))



