lista1 = [1,2,3]
lista2 = [4,5,6]


lista3 = []
def mergisort(lista1, lista2):
    
    for i in range(len(lista2)):
        if(lista1[i] < lista2[i]):
            lista3.append(lista1[i])
        else:
            lista3.append(lista2[i])
print(lista3)


# def Solution(lista3):

# 	n = len(lista3)
# 	if n % 2 == 0:
# 		z = n // 2
# 		e = lista3[z]
# 		q = lista3[z - 1]
# 		ans = (e + q) / 2
# 		return ans
# 	else:
# 		z = n // 2
# 		ans = lista3[z]
# 		return ans

# if __name__ == "__main__":

#     lista1 = []
#     lista2 = []
#     entra1 = input().split()
#     for i in (entra1):
#         lista1.append(int)
#     entra2 = input().split()
#     for j in entra2:
#         lista2.append(int)

#     mergisort(lista1, lista2)

#     print('%.2f'%Solution(lista3))
    # A = [11,8,5,5]



# This code is contributed by Mohit Kumra
