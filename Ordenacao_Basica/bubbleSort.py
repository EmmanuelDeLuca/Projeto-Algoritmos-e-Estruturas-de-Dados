#Algoritmo simples de ordenação
# Melhor caso: O(n)
#Caso Medio: O(n^2)
# Pior caso: (n^2)

#Algortimo

def bubble_sort(lista):
    #Tamanho do array, vetor ou lista
    n = len(lista)
    #Esse for tem a utilidade de sempre fica perccorendo o array
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos nas poscçoes i + i + 1
                lista[i], lista[i + 1] = lista[i+1], lista[i]

lista = [4,8,9,5,3,2,6,1]
bubble_sort(lista)
print(lista)