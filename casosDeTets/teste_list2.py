

lista1 = []
lista2 = []
Q = input().split()
A = input().split()
lista1.append(A)
lista2.append(Q)

for i in lista1:
    if(lista1[i] == lista2[i]):
        print(i)

