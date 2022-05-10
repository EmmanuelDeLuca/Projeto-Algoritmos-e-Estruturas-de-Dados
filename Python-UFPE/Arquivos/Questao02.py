# Ler um arquivo com profissões, onde cada profissão é
# formada por um código (positivo) e um nome (String), uma
# profissão por linha.
# – Receber do usuário uma lista de códigos para que o
# programa informe o nome de cada profissão.
# – Se o código da profissão não existir no arquivo, mostrar a
# mensagem “Profissão Inexistente”, gravar em outro arquivo
# estes códigos de profissões, e continuar.
# – O programa pára com a digitação de um código inválido
# (negativo ou zero).
def ler_arquivo(nome='profissoes.txt'): #Criando uma função, caso n passe nada tera como paramentro o arquivo txt
    dict = {} #Criando um dicionario para armazenar o arquivo
    try:
        arq_lido = open(nome, 'r') == with open(nome, 'r') as arq_lido:
        with arq_lido:
            for linha in arq_lido:
                lst = linha.split() #Nesse momennto tudo vai retorna string e separado de espaçoe outra n pode coloca codigo e string, pois ele ira quebra nos espaço e ira volta muita coisa
                dict[int(lst[0])] = ' '.join(lst[1:])#Ira junta as string quebradas 
    except FileNotFoundError:
        print("Arquivo/ caminho não encontrado.")

    return dict

dict = ler_arquivo #Pegando o retorno da função
codigo = int(input("Digite um codigo positovo(zero ou negativo para encerar): "))
while codigo > 0:
    if codigo in dict:
        print(f'O codigo{codigo} corresponde a profissão de {dict[codigo]}')#acessa o codigo atraves do dict
    else:
        print("Profissão inexistente")
        with open('cod_invalidos.txt', 'a') as arq_invalidos == arq_invalido = open('cod_invalidos.txt', 'a')
        arq_invalidos.write(f'{codigo}\n')







arq_profi = open('profissoes.txt', 'r')
with arq_profi:
    for profi in arq_profi:
        profissoes = profi.split()
        if profissoes[0] != usuario:
            print('profissoes inexistente')


flag = False
while not flag:
    try:
        usuario = int(input("Digite um codigo: "))
        while usuario <= 0:
            usuario = int(input("Digite novamente.Coloque um numero positivo: "))
    except ValueError:
        print("Error. Digite um numeiro inteiro.")
    else:
        flag = True


