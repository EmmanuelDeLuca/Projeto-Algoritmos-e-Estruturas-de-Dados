a1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]          
a2 = ['M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
numero = ''
i = 0
x = int(input("Digite maior que zero: "))
if x > 0 and x < 4000:
    for _ in range(x//a1[i]):
        numero+ =a2[i]
        x -= a1[i]
    i+=1
print(numero)



    
