num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
contadores_impares = 0
# O codigo abaixo está sendo feito para tratação de error
if num1 > num2:
    num1, num2 = num2, num1
if num1%2==0:
    num1 +=1

while num1 <= num2 :
    if num1%2!=0:
        contadores_impares+=1
    num1 = num1 +1
print(contadores_impares)

#ddkdkkdkkd
