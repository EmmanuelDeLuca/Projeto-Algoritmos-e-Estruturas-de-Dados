print("---------Tabela de conversão de F' para C'------------")
a = float(input("Digite a temperatura em Fahrenheit: "))
b = float(input("Digite outro valor em Fahrenheit: "))
F = 0
if a > b:
    a,b = b,a
    
while a <= b:
    C = ((F-32)*5/9)
    F = F + 1
    a+=1
    
print(a, C)
