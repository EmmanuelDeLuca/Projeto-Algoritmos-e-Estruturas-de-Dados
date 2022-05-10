n = int(input("Digite o tamanho da tabela"))
while n != 0:
    n =  int(input("Tamnho deve ser inteiro e maior que zero, caso contrario o program para"))
    curso = {}
    for i in range(n):

        curso['Código'] = int(input("Digite o codigo do curso: "))
        curso['Nome'] = str(input("Nome do curso: "))
        curso['Centro'] = int(input("Numero do centro: "))

        print(f"Tabela com Nome do curso: {curso['Nome']} foi lida corretamente")
        print(f"Tabela ->{curso}")

        curso['Código'] = int(input("Digite um código de profissão para busca (<= 0 para parar): "))
        while curso['Código'] > 0:
            if curso["Código"] in curso:

                curso["Nome"], curso['Código'] = curso['Código']
                
                print(f"Curso: {curso['Nome']}, Codigo: {curso['Código']}")
            else:
                print(f"Esse curso {curso['Nome']} não existe")
            curso['Código'] = int(input("Digite um código de profissão para busca (<= 0 para parar): "))
            # i=0
            # while (i < n) and (curso["Código"]!=[i][0]):
            #     i = i+1
            # if i < n:
            #     curso['Nome'], curso['Código'] = curso [i][1:]
                
            #     print(f"{curso['Nome']}, {curso['Código']}")
            # else:
            #     print(f'Curso e Centro não existe') 
    

print('fim do programa')

