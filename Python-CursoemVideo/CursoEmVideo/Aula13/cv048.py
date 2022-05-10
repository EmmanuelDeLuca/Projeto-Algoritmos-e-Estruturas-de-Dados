soma = 0
count = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        count = count + 1
print(f'A soma total {soma} e a quantidade {count}')