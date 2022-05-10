prt = input("Digite os parentenses ")

lista = []
x = 0
while x < len(prt):
    if prt[x] == '(':
        lista.append('(')
    if prt[x] == ')':
        if len(lista) > 0:
            topo = lista.pop(-1)
        else:
            lista.append(')')
            break
    x += 1
if len(lista) == 0:
    print('Ok')
else:
    print('erro')
