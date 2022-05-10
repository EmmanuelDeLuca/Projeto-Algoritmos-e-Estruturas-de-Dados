def quickSort(vetor1,vetor2, baixo, alto):
    if baixo < alto:
        pi = particao(vetor1, baixo, alto, vetor2[baixo])
        particao(vetor2,baixo,alto, vetor1[alto])

        quickSort(vetor1,vetor2, baixo,pi-1)
        quickSort(vetor1,vetor2, pi+1, alto)
def particao(array, baixo, alto, pivo):
    pivo = array[alto]
    i = (baixo) 
    
    for j in range(baixo, alto):
        if array[j] <= pivo:

            array[i], array[j] = array[j], array[i]
            i = i + 1
            
    array[i], array[alto] = array[alto], array[i] 
    return (i)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        bauDaChave = input().split()
        bauDoCadeado = input().split()
        quickSort(bauDaChave, bauDoCadeado,0,len(bauDoCadeado)-1)
        chave = ""
        cadeado = ""
        for i in range(len(bauDoCadeado)):
            chave += bauDaChave[i] + " "
            cadeado += bauDoCadeado[i] + " "
        print(chave.strip())
        print(cadeado.strip())

# 1
# KwY DGA ZYG VMb SQW WqJ 
# VMb DGA SQW KwY ZYG WqJ
# 1
# KwY rim DGA ZYG VMb SQW WqJ 
# VMb DGA rim SQW KwY ZYG WqJ 
# 1
# KwY rim DGA ZYG VMb SQW WqJ cAl
# VMb DGA rim cAl SQW KwY ZYG WqJ
# 1 
# KwY rim DGA ZYG VMb SQW WqJ cAl mTt
# VMb DGA rim cAl SQW KwY ZYG WqJ mTt
# 1
# mKN cgz cNr ysK yli
# mKN cgz cNr yli ysk



#Quando coloco assim pega Normal      
# arr = ['bjX', 'mbj', 'fIS']
# n = len(arr)
# quickSort(arr, 0, n-1)
# print("Sorted array is:")
# for i in range(n):
#     print(arr[i], end=" ")




# def partition(arr, low, high):
#     i = (low-1)         
#     pivot = arr[high]     
 
#     for j in range(low, high):
 

#         if arr[j] <= pivot:
 
            
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]
 
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)
 
 
# def quickSort(arr, low, high):
#     if len(arr) == 1:
#         return arr
#     if low < high:
 
#         pi = partition(arr, low, high)

#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)
 
# if __name__ == '__main__':
#     k = int(input())
#     for i in range(k):
#         chaves = input().split()
#         cadeados = input().split()
#         quickSort(cadeados, 0, len(cadeados)-1)
#         cad = ""
#         for i in range(len(cadeados)):
#             cad += cadeados[i] + " "
            
#         print(cad.strip())

# arr = ['mbj','bjx', 'fIS']
# n = len(arr)
# quickSort(arr, 0, n-1)
# print("Sorted array is:")
# for i in range(n):
#     print(arr[i], end=" ")