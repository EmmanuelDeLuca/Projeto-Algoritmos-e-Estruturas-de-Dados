# O arquivo “titanic.txt” disponibiliza informações dos passageiros que embarcaram no navio. Faça a
# leitura deste arquivo e, em seguida, armazene em um outro arquivo (“sobreviventes.txt”) o nome, o
# sexo e a idade dos passageiros que sobreviveram. Ao encerrar o programa, mostre na tela a
# quantidade de homens e mulheres sobreviventes bem como a média da idade deles (independente
# do sexo).
try:
    arq_leitura = open('titanic.txt', 'r')
    arq_escrita = open('sobreviventes.txt', 'w')
    homem = 0
    mulher = 0
    media = 0.0
    with arq_leitura, arq_escrita:
        for titan in arq_leitura:
            colunas = titan.split(',')
            if colunas[1] == '1':
                nome = colunas[3]
                sexo = colunas[4]
                idade = colunas[5]
                if colunas[4] == 'male':
                    mulher += 1
                else:
                    homem += 1
                media += float(idade)
                arq_escrita.write(f'{nome}, {sexo}, {idade} \n')
except FileNotFoundError:
    print("Digite o caminho certo.")
else:
    print(f"Quantidade de homenes vivos: {homem}")
    print(f"Quantidade de mulheres vivas: {mulher}")
    media = media/homem+mulher
    print(f"media de idade entre homem e mulher: {media}")


