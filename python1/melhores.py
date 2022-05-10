def melhoresClientes(nome = '', pontuacao_acima = 0):
    arq_melhores = open(nome, 'r')
    arq_melhordomelhor = open(nome + 'melhoresDecode.txt', 'w')
    
    soma = 0
    mediia = 0.0
    with arq_melhores, arq_melhordomelhor:
         for linha in arq_melhores:
             matricula = linha[0:5]
             sexo = linha[6:7]
             pontos = linha[9:15]
             cliente = linha[16:36]
             if(int(pontos) > pontuacao_acima):
                 mediia += int(pontos)
                 arq_melhordomelhor.write(f'{matricula} {pontos}')
                 soma+=1
    media = mediia/soma
    print(f"O nome da empresa é {nome}.")
    print(f"Foram gravados {soma} registros.")
    print(f"A pontuação média dos melhores clientes é {media}.")

    return None

nome = input('Digite o nome da empresa: ')
pontuacao_acima = int(input("Digite um valor pra pontuação:"))
melhoresClientes(nome, pontuacao_acima)
