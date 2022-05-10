# Considere um arquivo texto, cujo nome externo deve ser informado pelo usuário no início,
# contendo as informações dos materiais/estoque da empresa: código (inteiro com 3 posições),
# nome (string com 20 posições), qtdMinima e qtdAtual (ambos inteiros com 4 posições).
# Assuma que tem um espaço em branco separando as informações e que tem um material em
# cada linha do arquivo. Faça um programa Python para ler este arquivo e gravar o arquivo
# texto ‘compras.txt’, contendo informações das compras, também um material por linha:
# código, nome, e qtdCompra (inteiro com 4 posições), que precisam ser feitas para repor o
# estoque, apenas dos materiais que estejam com estoque abaixo do mínimo.
# Você deve escrever e usar uma função calculaCompra que deve receber como parâmetros o
# estoque mínimo e o estoque atual, e retornar como resultado a quantidade a ser comprada. A
# quantidade a ser comprada deve satisfazer a:
# (a) Os materiais que estejam com menos da metade do estoque mínimo devem fazer compras
# para ficar com estoque 20% acima do estoque mínimo.
# (b) Os materiais que estejam com estoque entre 50% e 90% (inclusive) do estoque mínimo
# devem fazer compras para ficar com estoque 10% acima do mínimo.
# (c) Os materiais que estejam com estoque de mais de 90% do estoque mínimo devem fazer
# compras apenas para repor este estoque mínimo.
# OBS - Eventuais valores decimais resultantes das operações envolvendo percentuais devem
# ser truncados (desprezados).
flag = False
while not flag:
        try:
            nome= input("Digita o nome do arquivo: ")
            arq_lido = open(nome, 'r')
            arq_escrito = open('compras.txt', 'w')
            with arq_lido:
                for linha in arq_lido:
                    codigo = int(linha[0:3])
                    nome = linha[5:25]
                    qtdMinima = int(linha [26:30])
                    qtdAtual = int(linha[26:30])
        except FileNotFoundError:  #Identifica o erro 
            print("Digite caminho certo: ")
        else:
            print("Acesso a função")
            flag = True

                
            def calculaCompra(minimo = 0, atual = 0):
                for coluna in arq_escrito:
                    codigo = coluna[0:3]
                    nome = coluna[5:25]
                    qtdCompra = coluna[26:31]
                    if (qtdMinima) < '50%':
                        print("Deve ser feito compra de 20%")
                        compra = qtdCompra * 0.20
                    elif qtdMinima < '50' and qtdMinima <'90':
                        print("Ficar acima de '10%' do estoque")

                        compra = qtdCompra * 0.10
                    else:
                            print('compras para repor estoque')
                            
                    arq_escrito.write(f'{codigo} {nome} {qtdCompra}')
    # except FileNotFoundError:  #Identifica o erro 
    #     print("Digite caminho certo: ")
    # else: # Finaliza o programa
    #     flag = True
    #     print(f"Programa finalizado com sucesso.")

