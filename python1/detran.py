fim = False
tot_veic_velhos = 0
while not fim:
    try:
        nome_arquivo = input("Digite o nome/caminho do arquivo: ")
        registros = open(nome_arquivo, 'r')
        veic_velhos = open('veicVelhos.txt', 'w')
        with registros, veic_velhos:
            for reg in registros:
                placa, marca, modelo, ano, cpf = reg.split()
                if int(ano) <= 2000:
                    veic_velhos.write(f'{placa} {ano} {cpf}\n')
                    tot_veic_velhos += 1
    except FileNotFoundError:
        print("Arquivo informado pelo usuário não encontrado. Digite um nome válido.")
    else:
        print(f"Tarefa realizada com sucesso. Número de veículos velhos armazenados: {tot_veic_velhos}")
        fim = True
