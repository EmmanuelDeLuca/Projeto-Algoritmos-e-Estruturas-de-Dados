def checkHeap(A):
    if len(A) <= 1:
        return True
        
    for i in range((len(A) - 2) // 2 + 1):

        if A[i] < A[2*i + 1] or (2*i + 2 != len(A) and A[i] < A[2*i + 2]):
            return 'maximo'

        elif A[i] > A[2*i + 1] or (2*i + 2 != len(A) and A[i] > A[2*i + 2]):
            return 1

        elif A[2 * i + 1] > A[i] or (2*i+2 < len(A) and A[2 * i + 2] < A[i]):
            return 2
    return True
    

if __name__ == '__main__':
    
    # A = [4, 10, 9, 1, 12, 16, 13, 8, 17, 13]
    A = [1,2,3,4,5]

    isHeap = checkHeap(A)

    if isHeap == 'maximo':
        print('is a maximo')
    if isHeap == 1:
        print('Is minimo')
    if isHeap == 2:
        print('não é')
    
   
