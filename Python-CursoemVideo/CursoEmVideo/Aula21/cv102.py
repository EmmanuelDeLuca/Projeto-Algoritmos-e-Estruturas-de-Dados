

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*=c
    return f

print(fatorial(5, show=False))
# def fatorial(num, show=False):

#     if show == True:
#         fat = 1
#         for i in range(num, 0, -1):
#             fat *= i
#         print(f'fatorial de {num} é: {fat}')
#     else:
#         fat = 1
#         for i in range(num, 0, -1):
#             fat *= i
#             print(f'{i} x ', end='')

# n = fatorial(4, show=False)
# print(n)


