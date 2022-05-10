# Considere um arquivo texto com nome externo  ́discip.old ́, contendo informações de disciplinas
# (Código com 5 posições, nome com 35 posições e créditos com 2 posições), uma disciplina por
# linha. Faça um programa Python para criar um segundo arquivo com nome externo  ́discip.new ́
# contendo informações das mesmas disciplinas, mas com as seguintes modificações:
# (a) As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e., não devem ser
# gravadas no novo arquivo.
# (b) Os números de créditos das disciplinas cujos códigos começam por MA devem ser
# alterados para 5.
# (c) O novo arquivo terá um campo a mais (carga horária, com 3 posições) cujo valor deve ser
# o número de créditos da disciplina multiplicado por 15.
# No final o seu programa deve imprimir o número de disciplinas de cada arquivo e também o
# número de disciplinas que tiveram seus números de créditos alterados.
try:
    arq_antigo = open('discip.old.txt', 'r')
    arq_new = open('discip.new.txt', 'w')
    discip = 0
    discitAlterada = 0

    with arq_antigo, arq_new:
        for disc in arq_antigo:
            codigo = disc[0:5] #string
            nome = disc[6:41]
            credito = disc[42:44]

            if (codigo != 'IF125') and (codigo != 'IF380'):
                if codigo[0:2] == 'MA':
                    discip +=1
                    credito = '5'
                cargaHoraria = int(credito) * 15
                arq_new.write(f'{codigo} {nome} {credito:2} {str(cargaHoraria):3}')
except FileNotFoundError:
    print("Digite o caminho correto do arquivo")
except PermissionError: #
    print("Erro. Sem permissão de acesso/criação de arquivo.")
else:
    print(f"Total de disciplinas no arquivo velho: {tot_velho}")
    print(f"Total de disciplinas no arquivo novo: {tot_novo}")
    print(f"Total de disciplinas alteradas arquivo novo: {disc_alteradas}")





        




