# def min_heapify(A,k):
#     l = left(k)
#     r = right(k)
#     if l < len(A) and A[l] < A[k]:
#         smallest = l
#     else:
#         smallest = k
#     if r < len(A) and A[r] < A[smallest]:
#         smallest = r
#     if smallest != k:
#         A[k], A[smallest] = A[smallest], A[k]
#         min_heapify(A, smallest)

# def left(k):
#     return 2 * k + 1

# def right(k):
#     return 2 * k + 2

# def build_min_heap(A):
#     n = int((len(A)//2)-1)
#     for k in range(n, -1, -1):
#         min_heapify(A,k)

# A = [1,3,2,9,5,4]
# build_min_heap(A)

# if build_min_heap == A:
#     print("naoo")
# else:
#     print("E")
# print(A)
# def isHeap(arr, i, n):
     
# # If a leaf node
#     if i >= int((n - 2) / 2):
#         return True
     
#     # If an internal node and is greater
#     # than its children, and same is
#     # recursively true for the children
#     elif(arr[i] >= arr[2 * i + 1] and
#        arr[i] >= arr[2 * i + 2] and
#        isHeap(arr, 2 * i + 1, n) and
#        isHeap(arr, 2 * i + 2, n)):
#         return 'MAXIMO'
#     elif(arr[i] <= arr[2 * i + 1] and
#        arr[i] <= arr[2 * i + 2] and
#        isHeap(arr, 2 * i + 1, n) and
#        isHeap(arr, 2 * i + 2, n)):
#         return 'MINIMO'
     
#     return False
 
# # Driver Code
# if __name__ == '__main__':
#     arr = [90, 15, 10, 7, 12, 2, 7, 3]
#     n = len(arr) - 1
 
#     if isHeap(arr, 0, n):
#         print("Yes")
#     else:
#         print("No")


# # Iterative function to check if a given list represents a min-heap or not
# def Heap(A):
 
#     # caso base
#     if len(A) <= 1:
#         return True
 
#     # verifica todos os nós right e left
 
#     # raiz ta começando com index 0
#     for i in range((len(A) - 2) // 2 + 1):
#         # se for false -> retoran o maximo
#         if A[i] > A[2*i + 1] or (2*i + 1 != len(A) and A[i] > A[2*i + 1]):
#             return False

#         # Minimo
#         if (A[i] < A[2*i + 1 ] or (2*i + 2) < len(A) and A[i] < A[2*i + 2]):
#             return False
        

#     return True
 
        
   
 
 
# if __name__ == '__main__':
 
#     A = [3, 5, 9, 7, 6, 13, 18, 17, 10, 11]
#     # A = [4, 10, 9, 1, 12, 16, 13, 8, 17, 13]
#     # A = [99, 80, 70, 60]
 
#     if Heap(A):
#         print('E heap minimo!')
#     else:
#         print('E um heap maximo')
#     # else:
#     #     print('Nao e um heap')
    

def Heap(A):
    if len(A) <= 1:
        return True
    for i in range((len(A) - 2) // 2 + 1):
        
        # Minimo
        if A[i] > A[2*i + 1] or (2*i + 2 != len(A) and A[i] > A[2*i + 2]):
            return False
        #maximo
        if (A[i] < A[2*i + 1 ] or (2*i + 2) != len(A) and A[i] < A[2*i + 2]):
             return False
    return True

    
 
if __name__ == '__main__':
 
    A = [3, 5, 9, 7, 6, 13, 18, 17, 10, 11]
    # A = [4, 10, 14, 1, 12, 6, 15, 8, 17, 13]
    # A = [99, 80, 70, 60, 50, 40, 30]
    # A = []
    # A = input().split()
    # for i in entrada:
    #     A.append(entrada)
    
 
    if Heap(A):
        print('E uma Heap de minimo!')
    # elif Heap(A):
    #     print('E uma Heap de maximo!')
    else:
        print('Nao e uma Heap!')