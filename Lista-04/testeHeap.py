# def isHeap(A):

    
 
#     # caso base
#     if len(A) <= 1:
#         return True
 
#     # verifica todos os nos right e left
 
#     # raiz ta comecando com index 0
#     for i in range((len(A) - 2) // 2 + 1):
#         if A[i] > A[2*i + 1 ] and (2*i + 2 != len(A) and A[i] > A[2*i + 2]):
#             print("E uma Heap de maximo!")

#         elif (A[i] <= A[2*i + 1] and (2*i + 2) != len(A) and A[i] <= A[2*i + 2]):
#             print('E uma Heap de minimo!')
 
#         else:
#             print( 'Nao e uma heap')
 
 
# if __name__ == '__main__':
 
#     # A = [3, 5, 9, 7, 6, 13, 18, 17, 10, 11]
#     # A = [4, 10, 9, 1, 12, 16, 13, 8, 17, 13]
#     # # A = [100, 90, 80, 70]
#     A = []
#     entrada = input().split()
#     for i in entrada:
#         A.append(entrada)

# isHeap(A)
  
# def isHeap(arr, i, n):
     
# # If a leaf node
#     if i >= int((n - 2) / 2):
#         return True
    

     
#     # If an internal node and is greater
#     # than its children, and same is
#     # recursively true for the children
#     # if(arr[i] >= arr[2 * i + 1] and arr[i] >= arr[2 * i + 2] and isHeap(arr, 2 * i + 1, n) and isHeap(arr, 2 * i + 2, n)):
#     #     return True
#     if(arr[i//2]<= arr[i]):
#         print('Minimo')
     
#     return False
 
# # Driver Code
# if __name__ == '__main__':
#     arr = [1,2,3,4]
#     n = len(arr) - 1
 
#     if isHeap(arr, 0, n):
#         print("Yes")
#     else:
#         print("No")


def isHeap(A):
    # caso base
    if len(A) <= 1:
        return True
    for i in range((len(A) - 2) // 2 + 1):
        
        if A[i] > A[2*i + 1] or (2*i + 2 != len(A) and A[i] > A[2*i +2]):
            return True

        if A[2 * i + 1] > A[i] or (2*i+2 < len(A) and A[2 * i + 2] < A[i]):
            return True

        
    return True
if __name__ == '__main__':
 
    A = [1,2,3,4,5]
 
    if isHeap(A):
        print('é uma heap')
    elif isHeap(A):
        print('É MAIXMO')
    else:
        print("é minimo")