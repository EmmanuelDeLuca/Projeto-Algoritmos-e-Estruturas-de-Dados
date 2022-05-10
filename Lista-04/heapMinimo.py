
def checkMinHeap(A):
    # base case
    if len(A) <= 1:
        return True
    for i in range((len(A) - 2) // 2 + 1):
        if A[i] > A[2*i + 1] or (2*i + 2 != len(A) and A[i] > A[2*i + 2]):
            print("Maximo")
            return False
    print("Minimo")
    return True
 
 
if __name__ == '__main__':
    
    A = [1,2,3,4,5,6]
 
    if checkMinHeap(A):
        print('is a min-heap')
    else:
        print('is not a min-heap')

