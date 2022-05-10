num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
user = 0
while user != 5:
    print('''
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa
''')
    user = int(input("Digite um valor do menu: "))
    while user < 1 and user > 5:
        user = int(input("Digite um valor do menu: "))

    if user == 1:
        somar = num1 + num2
        print(f"Somar: {somar}")
        
    elif user == 2:
        mult = num1 * num2
        print(f'Multiplicação: {mult}')
    elif user == 3:
        if(num1 > num2):
            maior = num1
            print('Numero 1 é o maior')
        else:
            maior = num2
            print("Numero 2 é o maior")
    elif user == 4:
            num1 = float(input("Digite novos valores: "))
            num2 = float(input("Digite novos valores: "))
    elif user == 5:
        print('Saindo...')

