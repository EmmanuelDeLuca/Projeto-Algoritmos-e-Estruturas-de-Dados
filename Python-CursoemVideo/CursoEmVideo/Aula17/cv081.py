lista = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    b = input("Deseja continuar [N/S").upper()
    if b == 'N':
        break

    n2 = len(lista)

    lista.sort(reverse=True)

for i in lista:
    if i == 5:
        print("Numero 5 foi digitado")
    else:
        print("Numero 5 não foi digitado")
print(f"Numero digitados {n2}")
print(f"Ordem decrescente {lista}")
