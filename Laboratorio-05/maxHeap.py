


def max_heapify(A, k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def left(k):
    return 2 * k + 1
def right(k):
    return 2 * k + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)

# A= [3, 10, 40, 1, 60, 34, 21, 100, 5, 31, 2, 4, 6]

# A=[100, 90, 80, 70, 60, 50, 40, 30, 20, 11, 1001]

# A= [1, 2, 3, 9, 8, 7, 6, 5, 4, 20, 30, 40, 50, 60]
A = [5, 5, 8, 11, 2]
build_max_heap(A)
print(A)