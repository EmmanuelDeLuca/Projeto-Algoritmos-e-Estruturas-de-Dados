frag = False
while not frag:
    try:
        nome = input("Digite o nome do arquivo: ")
        arq_lido = open(nome, 'r')
        maiorPontuacao = [-999999999, ""]
        menorPontuacao = [9999999999, ""]
        homem = 0
        mulher = 0
        with arq_lido:
            for linha in arq_lido:
                cadastro = linha[0:5]
                sexo = linha[6:7]
                pontuacao = linha[10:15]
                nome = linha[16:36].strip()
                if int(pontuacao) > int(maiorPontuacao[0]):
                    maiorPontuacao[0] = pontuacao
                    maiorPontuacao[1] = nome

                if int(pontuacao) < int(menorPontuacao[0]):
                    menorPontuacao[0] = pontuacao
                    menorPontuacao[1] = nome
                if sexo == '1':
                    homem += 1
                else:
                    mulher += 1
    except FileNotFoundError:
        print("Informe o caminho correto do arquivo.")
    else:
        print(f"Maior pontuação: {maiorPontuacao[1]} com {maiorPontuacao[0]} pontos")
        print(f"Menor pontuação: {menorPontuacao[1]} com {menorPontuacao[0]} pontos")
        print(f'Quantidades de homens e mulheres respectivamente: {homem} e {mulher}')
        frag = True
        
