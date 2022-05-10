def isHeap(arr, n):
     
    # Start from root and go till
    # the last internal node
    for i in range(int((n - 2) / 2) + 1):
         
        # If left child is greater,
        # return false
        # Não é uma heap
        if arr[2 * i + 1] > arr[i] and (2 * i + 2 < n and arr[2 * i + 2] > arr[i]):
                return False
                
    return True
 
# Driver Code
if __name__ == '__main__':
    arr = [4, 10, 14, 1, 12, 6, 15, 8, 17, 13]
    n = len(arr)
 
    if isHeap(arr, n):
        print("Yes")
    else:
        print("No")