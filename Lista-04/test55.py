# def Heap(A):
#     # caso base
#     if len(A) <= 1:
#         return True
#     # verifica todos os nos right e left
#     # raiz ta comecando com index 0
#     for i in range((len(A) - 2) // 2 + 1):
#         # Minimo
#         if A[i] > A[2*i + 1] or (2*i + 2 != len(A) and A[i] > A[2*i + 2]):
#             return False
#         #maximo
#         elif (A[i] < A[2*i + 1 ] or (2*i + 2) < len(A) and A[i] < A[2*i + 2]):
#              return False
#     return True

    
 
# if __name__ == '__main__':
 
#     # A = [3, 5, 9, 7, 6, 13, 18, 17, 10, 11]
#     # A = [4, 10, 14, 1, 12, 6, 15, 8, 17, 13]
#     # A = [99, 80, 70, 60, 50, 40, 30]
#     # A = []
#     A = input().split()
#     # A.append(entrada)
    
 
#     if Heap(A):
#         print('E uma Heap de minimo!')
#     elif Heap(A):
#         print('E uma Heap de maximo!')
#     else:
#         print('Nao e uma Heap!')

def isHeapMax(A):
    if len(A) <= 1:
        return True

    
    for i in range(1, (len(A) // 2)):
        if (A[i] > A[2*i + 1 ] and A[i] > A[2*i]):
            return True
        else:
            return False
    # return True
def isHeapMin(A):
    if len(A) <= 1:
        return True

    
    for i in range(1, (len(A) // 2)):
        if A[i] < A[2*i + 1] and A[i] < A[2*i]:
            return True
        else:
            return False
    # return True
        
 

if __name__ == '__main__':
 
    # A = [3, 5, 9, 7, 6, 13, 18, 17, 10, 11]
    # A = [4, 10, 14, 1, 12, 6, 15, 8, 17, 13]
    # A = [99, 80, 70, 60, 50, 40, 30]
    A = []
    entrada = input().split()
    for i in entrada:
        A.append(int(i))
    # print(A)
    
    
    if isHeapMax(A) == True and isHeapMin(A) == False:
        print('E uma Heap de maximo!')
    elif isHeapMin(A) == True and isHeapMax(A) == False:
        print("E uma Heap de minimo!")
    elif isHeapMax(A) == False and isHeapMin(A) == False :
        print("Nao e uma Heap!")
    


    # if isHeap(A):
    #     print('Heap de maximo')