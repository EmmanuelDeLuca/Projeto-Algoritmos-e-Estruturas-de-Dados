# Fatorial = 5 -> 5x4x3x2x1

# n = int(input("Digite um numero"))
# fat = 1
# for i in range(1, n + 1):
#     fat = fat * i
# print(fat)

num = int(input("fatorial de : "))

resultado = 1
count = 1
while count <= num:
    resultado *= count
    count+=1
print(resultado)