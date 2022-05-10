n = int(input("Sequencia de fibonacci: "))
n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Por favor entra com numero positivo e inteiro")
elif n == 1:
    print(f"Fibonacci {n1}")
else:
    print("Sequencia de fibonacci: ")
    while count <= n:

        print(n1, end=' ')
        fib = n1 + n2
        n1 = n2
        n2 = fib
        count += 1
