def clientees(pontuacao_minima = 0):

    
        arq_leitura = open('clientes.arq.txt', 'r')
        clientes_acima = 0
        totaldepontos = 0.0
        clientesLido: 0
        clientes_impressos = 0
        
        with arq_leitura:
            for linha in arq_leitura:
                matricula = linha[0:4]
                nome = linha[6:36]
                sexo = linha[37:39]
                pontos = linha[40:46]
                if int(pontos) > pontuacao_minima:
                    totaldepontos += int(pontos)
                    clientes_acima = clientes_acima + 1
                    clientesLido+=1
            
                    print(f'clientes com pontuação acima {nome}, {pontos}, {matricula}')
                else:
                    clientes_impressos+=1
                    print(f"Cliente com pontuação abaixo do minimo: {nome}, {pontos}, {matricula}")
        media = totaldepontos/clientesLido
        print(f"Clientes Lidos: {clientesLido}")
        print(f'total de clientes impressos: {clientes_impressos}')
        print(f'Meida dos clientes Lidos: {media}')
        return None
flag = False
while not flag:
    try:
        pontuacao_minima = int(input("Digite um codigo: "))
        while pontuacao_minima > 1000:
            pontuacao_minima = int(input("Digite novamente.Coloque um numero positivo: "))
    except ValueError:
        print("Digite um valor maior que 1000")
    else:
        flag = True
