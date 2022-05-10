# def melhoresClientes(nome = '', pontuacao_acima = 0):
#     arq_melhores = open(nome, 'r')
#     arq_melhordomelhor = open(nome + 'melhoresDecode.txt', 'w')
#     cont = 0
#     soma = 0
#     with arq_melhores, arq_melhordomelhor:
#          for linha in arq_melhores:
#              matricula = linha[0:5]
#              sexo = linha[6:7]
#              pontos = linha[7:15]
#              cliente = linha[16:36]
#              if(int(pontos) > pontuacao_acima):
#                  arq_melhordomelhor.write(f'{matricula} {pontos}')
#                  cont+=1
#                  soma+=1
#     media = cont/soma
#     print(f"O nome da empresa é {nome}.")
#     print(f"Foram gravados {cont} registros.")
#     print(f"A pontuação média dos melhores clientes é {media}.")

    # return None
# flag = False
# while not flag:
#     try:
#         N = int(input('Digite o numero de empresas: '))
#         while N <=0:
#             N = int(input('Digite o numero de empresas: '))
#     except ValueError:
#         print("Error. Digite um inteiro positvo")
#     else:
#         flag = True
# for i in range(N):
    # nome = input('Digite o nome da empresa: ')
    # pontuacao_acima = int(input("Digite um valor pra pontuação:"))

def melhoresClientes(nome = '', pontuacao_acima = 0):
    arq_melhores = open(nome, 'r')
    arq_melhordomelhor = open(nome + 'melhoresDecode.txt', 'w')
    
    soma = 0
    media = 0.0
    with arq_melhores, arq_melhordomelhor:
         for linha in arq_melhores:
             matricula = linha[0:5]
             sexo = linha[6:7]
             pontos = linha[9:15]
             cliente = linha[16:36]
             if int(pontos) > pontuacao_acima:
                 media += int(pontos)
                 soma+=1
                 arq_melhordomelhor.write(f'{matricula} {pontos} \n')
    total = media/soma
    print(f"O nome da empresa é {nome}.")
    print(f"Foram gravados {soma} registros.")
    print(f"A pontuação média dos melhores clientes é {total}.")

    return None

nome = input('Digite o nome da empresa: ')
pontuacao_acima = int(input("Digite um valor pra pontuação:"))

melhoresClientes(nome, pontuacao_acima)





