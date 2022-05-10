
# Fazer um programa Python para:
# – Ler uma seqüência de números inteiros positivos (ou
# zero).
# – A leitura deve parar com um número negativo.
# – O programa deve imprimir os números lidos cujos
# valores têm dois dígitos, mas na ordem inversa em



# que forem lidos – o último número lido deve ser o
# primeiro a ser impresso.
n = int(input("Digite um numero maior que zero(numeros negativos param o programa) "))
num = []
while n > 0:
    if n < 10:
        print("Digite um valor maior ou igual a 10")
        n = int(input("Digite um numero maior que zero(numeros negativos param o programa) "))
        
    if n >= 10 and n <= 99:
        num.append(n)
        n = int(input("Digite um numero maior que zero(numeros negativos param o programa) "))
print(num[::-1])
