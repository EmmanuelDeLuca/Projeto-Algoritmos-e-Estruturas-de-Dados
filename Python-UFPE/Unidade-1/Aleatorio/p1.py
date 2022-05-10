'''temp = float(input("Digite a temperatura em grau: "))
conver = ((temp * 9/5) + 32)
print(f"Sua temperatura em Fahrenheit é {conver} e sua temperatura em grau era {temp}")'''
for i in range(5):
    v = i*3
    print(v)

temp = float(input())
while temp > 0:
    conver = ((temp * 9/5) + 32)
    print(conver)
    temp+=1
    break
temp = float(input())