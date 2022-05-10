# # def mergeSort(arr3):
# #     if len(arr3) > 1:
# #         mid = len(arr3)//2
# #         L = arr3[:mid]
# #         R = arr3[mid:]
# #         mergeSort(L)
# #         mergeSort(R)
# #         i = j = k = 0
# #         while i < len(L) and j < len(R):
# #             if L[i] < R[j]:
# #                 arr3[k] = L[i]
# #                 i += 1
# #             else:
# #                 arr3[k] = R[j]
# #                 j += 1
# #             k += 1
# #         while i < len(L):
# #             arr3[k] = L[i]
# #             i += 1
# #             k += 1
  
# #         while j < len(R):
# #             arr3[k] = R[j]
# #             j += 1
# #             k += 1
  
# # def Solution(arr3):

# # 	n = len(arr3)
# # 	if n % 2 == 0:
# # 		z = n // 2
# # 		e = arr3[z]
# # 		q = arr3[z - 1]
# # 		ans = (e + q) / 2
# # 		return ans
# # 	else:
# # 		z = n // 2
# # 		ans = arr3[z]
# # 		return ans
# # if __name__ == "__main__":
	
# #     arr1 = []
# #     entrada = input().split()
# #     for i in entrada:
# #         arr1.append(int(i))
# #     arr2= []
# #     entrad = input().split()
# #     for i in entrad:
# #         arr2.append(int(i))
# #     arr3 = []


    
# #     mergeSort(arr3)

# #     print('%.2f'%Solution(arr3))

# from tkinter import N


# def mergeArrays(arr1, arr2, n1, n2):
#     arr3 = [None] * (n1 + n2)
#     i = 0
#     j = 0
#     k = 0
#     while i < n1 and j < n2:
#         if arr1[i] < arr2[j]:
#             arr3[k] = arr1[i]
#             k = k + 1
#             i = i + 1
#         else:
#             arr3[k] = arr2[j]
#             k = k + 1
#             j = j + 1
#     while i < n1:
#         arr3[k] = arr1[i]
#         k = k + 1
#         i = i + 1
#     while j < n2:
#         arr3[k] = arr2[j]
#         k = k + 1
#         j = j + 1

# def Solution(arr3):

# 	n = len(arr3)
# 	if n % 2 == 0:
# 		z = n // 2
# 		e = arr3[z]
# 		q = arr3[z - 1]
# 		ans = (e + q) / 2
# 		return ans
# 	else:
# 		z = n // 2
# 		ans = arr3[z]
# 		return ans
# if __name__ == "__main__":
	
#     arr1 = []
#     entrada = input().split()
#     for i in entrada:
#         arr1.append(int(i))
#     arr2= []
#     entrad = input().split()
#     for i in entrad:
#         arr2.append(int(i))
    
#     n1 = len(arr1)
#     n2 = len(arr2)
#     mergeArrays(arr1, arr2, n1, n2)
#     print('%.2f'%Solution(mergeArrays(N))


# A Simple Merge based O(n) solution to find
# median of two sorted arrays

""" This function returns median of ar1[] and ar2[].
Assumption in this function:
Both ar1[] and ar2[] are sorted arrays """
def mediana(ar1, ar2, n, m) :

	i = 0 # Current index of input array ar1[]
	j = 0 # Current index of input array ar2[]
	m1, m2 = -1, -1

	# Since there are (n+m) elements,
	# There are following two cases
	# if n+m is odd then the middle
	# index is median i.e. (m+n)/2
	if((m + n) % 2 == 1) :
		for count in range(((n + m) // 2) + 1) :	
			if(i != n and j != m) :		
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1		
			elif(i < n) :		
				m1 = ar1[i]
				i += 1
		
			# for case when j<m,
			else :		
				m1 = ar2[j]
				j += 1	
		return m1
	
	# median will be average of elements
	# at index ((m + n)/2 - 1) and (m + n)/2
	# in the array obtained after merging ar1 and ar2
	else :
		for count in range(((n + m) // 2) + 1) :		
			m2 = m1
			if(i != n and j != m) :	
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1		
			elif(i < n) :		
				m1 = ar1[i]
				i += 1
			
			# for case when j<m,
			else :		
				m1 = ar2[j]
				j += 1	
		return (m1 + m2)//2
	
ar1 = [900]
ar2 = [5, 8, 10, 20]

n1 = len(ar1)
n2 = len(ar2)
print(mediana(ar1, ar2, n1, n2))


