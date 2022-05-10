tupla = (
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")),
    int(input("Digite um valor: ")))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'o valor 3 apareceu na{tupla.index(3)+1}')

print('Os valores pares digitados foram')
for n in tupla:
    if n % 2 == 0:
        print(n)