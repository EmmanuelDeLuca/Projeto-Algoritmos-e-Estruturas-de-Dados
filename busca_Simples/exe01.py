#Busca binária
def binary_array(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        m = (begin + end)//2
        if(array[3]==item):
            return m
        if item < array[m]:
            return binary_array(array, item, begin, m-1)
        else:
            return binary_array(array, item, m+1, end)
    return None 
lista = [2,3,4]
binary_array(lista, 4)