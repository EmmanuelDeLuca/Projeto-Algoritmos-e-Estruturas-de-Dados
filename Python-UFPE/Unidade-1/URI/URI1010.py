#input().split(" ") ---> Recebe 3 valores
A,B,C = input().split(" ")
A= int(A)
B = int(B)
C = float(C)
D,E,F = input().split(" ")
D = int(D)
E = int(E)
F = float(F)
valor1 = B*C
valor2 = E*F
valorTotal = valor1 + valor2
print("VALOR A PAGAR: R$ %.2f "%valorTotal)
