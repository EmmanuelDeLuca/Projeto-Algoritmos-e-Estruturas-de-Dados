
# def MergeSort(lst):
#     # making sure length of list is 1 , which is the midpoint element
#     if len(lst) > 1:
#         # find midpoint of the list
#         midpoint = len(lst)//2
#         # divide the list into two parts (sublists), part to the left and right of midpoint
#         lefthalf = lst[:midpoint]
#         righthalf = lst[midpoint:]
        
#         # keep calling the function till length of list becomes 1
#         MergeSort(lefthalf)
#         MergeSort(righthalf)

#         # Assign zero value to all index variables initially
#         # k is the index variable for list parameter
#         i = j = k = 0
        
#         # compare all elements in leftpart and rightpart
#         # add elements in sorted order and update the list
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 lst[k] = lefthalf[i]
#                 i += 1
#             else:
#                 lst[k] = righthalf[j]
#                 j += 1
#             k += 1

#         #add any remaining elements in leftpart to the new list  
#         while i < len(lefthalf):
#             lst[k] = lefthalf[i]
#             i += 1
#             k += 1
  
#         #add any remaining elements in rightpart to the new list  
#         while j < len(righthalf):
#             lst[k] = righthalf[j]
#             j += 1
#             k += 1

#     return lst

# function to find median
def find_median(lst1, lst2):
    lst3 = lst1 + lst2
    lst3.sort()
    n = len(lst3)
    if n % 2 == 0:
        k = n // 2
        mid_value1 = lst3[k]
        mid_value2 = lst3[k-1]
        median = (mid_value1 + mid_value2)/ 2
        return median
    else:
        k = n // 2
        median  = lst3[k]
        return median
                    


#example lists to test median program
# list1 = [5,5,8,11]
# list2 = [3]
if __name__ == "__main__":
	
    arr1 = []
    entrada = input().split()
    for i in entrada:
        arr1.append(int(i))
    arr2= []
    entrad = input().split()
    for i in entrad:
        arr2.append(int(i))

# call the median function and print the final median value
print('%.2f'%find_median(arr1, arr2))





