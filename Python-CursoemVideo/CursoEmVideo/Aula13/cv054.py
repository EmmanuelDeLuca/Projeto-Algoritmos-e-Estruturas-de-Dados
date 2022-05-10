menores = 0 
maiores = 0
for i in range(1,8):
    num = int(input("Digite o ano de nascimento: "))
    idade = 2021 - num

    if idade < 18 :
        menores = menores + 1
        
    else:
        maiores = maiores + 1
        
print(f"{menores} de menor")
print(f'{maiores} de maior')