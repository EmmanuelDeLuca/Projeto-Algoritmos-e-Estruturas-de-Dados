def salarioAtualEnovo(A,B):
    for i in range(len(A)):
        for j in range(len(B)):
            p = A[i] * B[j]
            print('%.2f' %p)
A = [1,2]
B = [3,2]
salarioAtualEnovo(A,B)
    
