
def minimum(A):

    min_value = None
    for num in A:
        if (min_value is None or num < min_value):
          min_value = num
    return min_value

A = [11, 8, 5, 5]
minimum(A)
print('Minimo value:', minimum(A) )

def maximum(A):
    max_value = None

    for num in A:
        if (max_value is None or num > max_value):
            max_value = num
    return max_value
A = [10, 9, 8, 7, 6, 5]
maximum(A)
print('Maximum value:', maximum(A))

