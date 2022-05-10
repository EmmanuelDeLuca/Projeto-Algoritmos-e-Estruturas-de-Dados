L = [0, 0, 0, 0, 0]
for i in range(0, 5):
    L[i] = int(input("Digite 5 valores %d: " % (i+1)))

fim = 5

while fim > 1:
    achou = False
    x = 0
    while x < (fim-1):
        if L[x] > L[x+1]:
            achou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x += 1
    if not achou:
        break
    fim -= 1
for e in L:
    print(e)
