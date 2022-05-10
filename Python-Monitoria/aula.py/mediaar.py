n = float(input("Digite um numero maior ou igual a zero: "))
soma = n
total = 1.0
while n >= 0:
    n = float(input("Digite um numero maior ou igual a zero: "))
    if n >=0:
        soma+= n
        total+=1.0
if soma < 0:
    print("Nenhum numero valido foi digitado: ")
else:
    print(f"a media dos numeros digitados é: {soma/total}")