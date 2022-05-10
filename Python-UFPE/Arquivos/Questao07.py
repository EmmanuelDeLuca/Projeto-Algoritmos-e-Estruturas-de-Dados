# Mostre: 
# 1. Quem tem a maior pontuação.

# 2. Quem tem a menor pontuação.

# 3. Quantidade de homens.

# 4. Quantidade de mulheres.
# Organizado: cadastro, sexo, pontos, nome
#No fatiamento devemos acrescentar mais um no final para pegar o que deseja
frag = False
while not frag:
    try:
        nome = input("Digite o nome do arquivo: ")
        arq_lido = open(nome, 'r')
        pontuacao = 0
        menor_pontuacao = 0
        homem = 0
        mulher = 0
        with arq_lido:
            for linha in arq_lido:
                cadastro = linha[0:5]
                sexo = linha[7:8]
                pontos = linha[10:15]
                nome = linha[16:36]
                for i in int(pontos):
                    if i > 10000:
                        pontuacao +=1
                if int(pontos) > int(pontos):
                    pontuacao = int(pontos)
                else:
                    menor_pontuacao = int(pontos)
                if (sexo) == '1':
                    homem += 1
                else:
                    mulher += 1
    except FileNotFoundError:
        print("Informe o caminho correto do arquivo.")
    else:
        print(f'Maior pontuação: {pontuacao} e a menor pontuação: {menor_pontuacao}')
        print(f'Quantidades de homens e mulheres respectivamente: {homem} e {mulher}')
        frag = True
        

