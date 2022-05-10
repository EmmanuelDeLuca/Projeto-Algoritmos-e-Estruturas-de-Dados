frag = False
contador = 0
while not  frag:
    try:
        nome = input("Digite o nome do arquivo: ")
        arq = open(nome, 'r')
        arq_esc = open('veicVelhoos.txt', 'w')
        for linha in arq:
            placa, marca, modelo, ano, cpf = linha.split()
            if int(ano) <= 2000:
                       contador +=1
                       arq_esc.write(f'{placa} {ano} {cpf}')
        arq.close()
        arq_esc.close()
                       
    except FileNotFoundError:
        print("ERRO. Digite um caminho certo")
    else:
        print("Programa finalizado com sucesso.")
        print(f"Numero de veiculos velhos gravados no arquivo:{contador}")
    frag = True
    
