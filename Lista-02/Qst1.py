
def sequencia(A, elemQ):
    
    esq, dire,  = 0, len(A) - 1

    while esq <= dire:

        mid = (esq + dire) //2 
            
        if int(A[mid]) > elemQ:
            dire = mid - 1

        elif int(A[mid])< elemQ:
            esq = mid + 1
        else:
            return elemQ

    
    
if __name__ == '__main__':
    
    A = input().split()
    Q = input().split()
    
    enc = ''
    nao_enc = ''


    for elem in Q:
        elem = int(elem)
        
       
        if sequencia(A, elem):
            enc += str(elem) + " "
        else:
            nao_enc += str(elem) + " "
    print(enc[:-1])
    print(nao_enc[:-1])
    
    



    




 
    
        

