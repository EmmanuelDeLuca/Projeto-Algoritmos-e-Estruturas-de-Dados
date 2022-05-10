# Ler um arquivo do Detran onde cada registro contém as
# seguintes informações: placa, marca, modelo e ano de
# cada veículo, além do CPF do proprietário. O nome
# físico do arquivo será fornecido pelo usuário. – Gravar em um outro arquivo com nome externo
# “veicVelhos.txt” a placa e ano do veículo e o CPF dos
# proprietários de todos os veículos que sejam do ano
# 2000 ou mais velhos.
# – Informar no final ao usuário o número de veículos
# velhos gravados no arquivo.
flag = False
total_Veic = 0
while not flag:
    try:
        nome = input("Digite o nome do arquivo: ") #Recebe o nome do arquivo
        arq_leitura = open(nome, 'r') #Ler o arquivo
        arq_escrita = open('veicVelhos.txt', 'w') #Grava o arquivo
        with arq_leitura: #abre o arquivo e n precisa fechar 
            for carro in arq_leitura: #interação com o arquivo
                placa, marca, modelo, ano, cpf = carro.split(',') #Recebe as variaveis e transforma tudo
                if int(ano) < 2000: #Cria um If para ve qual é o melhor
                    total_Veic += 1 #soma sempre mais um
                    arq_escrita.write(f'{placa} {ano} {cpf}\n') #escreve no arquivo novo
    except FileNotFoundError:  #Identifica o erro 
        print("Digite caminho certo: ")
    else: # Finaliza o programa
        flag = True
        print(f"Programa finalizado com sucesso. total de veiculos velhos {total_Veic}")
