def Heap(A):
    if len(A) <= 1:
        return True
   
    maxx =  0
    for i in range(1 , (len(A) // 2)):
        
        # retorna maixmo se for true
        if A[i] > A[2*i + 1]  and A[i] > A[2*i ]:
            maxx = 1
            
        
        # retorna minimo se for true
        elif (A[i] < A[2*i + 1]  and A[i] < A[2*i ]):
             
             maxx = 2
             
        
        else:
            
            maxx = 3
            
    
    if maxx == 1:
        print('E uma Heap de maximo!')
    elif maxx == 2:
        print('E uma Heap de minimo!')
    elif maxx == 3 :
        print('Nao e uma Heap!')

    
 
if __name__ == '__main__':
 
    # A = [3, 5, 9, 7, 6, 13, 18, 17, 10, 11]
    # A = [4, 10, 14, 1, 12, 6, 15, 8, 17, 13]
    # A = [99, 80, 70, 60, 50, 40, 30]

    A = []
    entrada = input().split()
    for i in entrada:
        A.append(int(i))
    Heap(A)
    # if isHeap == 2:
    #     print('E uma Heap de minimo!')
    # if isHeap == 1:
    #     print('E uma Heap de maximo!')
    # if isHeap == 0:
    #     print('Nao e uma Heap!')