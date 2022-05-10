def multiplos(num1):
    mult7 = [0]*100
    mult5 = [0]*100
    mult11 = [0]*100
    qtd5 = 0
    qtd7 = 0
    qtd11 = 0

    num1 = int(input("Digite uma sequencia de numeros inteiros: "))
    if  num1 < 101:

        if (num1 % 7 == 0):
            mult7[qtd7] = num1
            qtd7 = qtd7 + 1
        if(num1 % 5 == 0):
            mult5[qtd5] = num1
            qtd5 = qtd5 + 1
        if(num1 % 11 != 0):
            mult11[qtd11] = num1
            qtd11 = qtd11 + 1

    print(f"Os multiplos de 7: {mult7}")
    print(f"Os multiplos de 5: {mult5}")
    print(f"Os multiplos de 11: {mult11}")

    num1 = int(input(" 0 p/parar: "))
    while num1 > 0 :
        num1 = int(input(" 0 p/parar: "))
