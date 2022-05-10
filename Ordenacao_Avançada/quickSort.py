#QuickSort
# def quicksort(lista, inicio = 0, fim = None ):
#     #Recursivo
#     if fim is None:
#         fim = len(lista)-1
#     if inicio < fim:
#         p = partition(lista, inicio, fim)
#         quicksort(lista, inicio, p-1)
#         quicksort(lista, p+1, fim)

# def partition(lista, inicio, fim):

#     pivot = lista[fim]
#     i = inicio

#     for j in range(inicio, fim):
#         if lista[j] <= pivot:

#             lista[j], lista[i] = lista[i], lista[j]
#             i = i + 1
#     lista[i], lista[fim] = lista[fim], lista[i]
#     return i
# if __name__ == "__main__":

def partition(lista, inicio, fim, pi):
    i = (inicio-1)         
    pivo = pi
  
    for j in range(inicio, fim):
        if lista[j] <= pivo:

            i = i+1
            lista[i], lista[j] = lista[j], lista[i]
  
    lista[i+1], lista[fim] = lista[fim], lista[i+1]
    return (i+1)
  
def quickSort(lista1, lista2, inicio, fim):
    if inicio < fim:
  
        pi = partition(lista1, inicio, fim, lista2[fim])
        partition(lista2, inicio, fim, lista1[pi])

        quickSort(lista1, lista2, inicio, pi-1)
        quickSort(lista1, lista2, pi+1, fim)
        

if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        chaves = input().split()
        cadeados = input().split()
        quickSort(chaves, cadeados, 0, len(cadeados)-1)
        cha = ""
        cad = ""
        for i in range(len(cadeados)):
            cha += chaves[i] + " "
            cad += cadeados[i] + " "
        print(cha.strip())
        print(cad.strip())
else:
    chave = "cQO trj VfC GyC zrs SZy JjC".split()
    cadeado = "cQO trj VfC GyC zrs SZy JjC".split()
    quickSort(chave, cadeado, 0, len(cadeado)-1)
    print(chave)
    print(cadeado)

