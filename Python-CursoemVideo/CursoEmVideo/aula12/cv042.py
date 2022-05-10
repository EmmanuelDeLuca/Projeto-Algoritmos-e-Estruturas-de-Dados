# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes
a = float(input("1-numero: "))
b = float(input("2-numero: "))
c = float(input("3-numero: "))

if(a==b==c):
    print('Trinagulo Equilátero')
elif(a==b or b == c or c==a):
    print('Triangulo isosceles')
else:
    print('Triangulo escaleno')