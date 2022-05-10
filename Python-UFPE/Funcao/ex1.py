# Fazer um programa para:
# – Ler uma tabela com N profissões, onde
# • O valor de N é informado antes pelo usuário.
# • Cada profissão é formada por um código (número positivo),
# um nome (String) e uma área (String).
# • Leitura da tabela deve ser feita em subrotina.
# – Depois o usuário fornecerá uma lista de códigos para
# que o programa informe o nome de cada profissão.
# – Se o código da profissão não existir na tabela, mostrar
# a mensagem “Profissão Inexistente” e continuar.
# – O programa pára com a digitação de um código
# inválido (negativo ou zero).

def leitura(profissional):
    codigo = int(input("Digite o codigo(numero tem que ser maior que zero)"))
    while codigo <= 0:
        codigo = input('Tamanho deve ser inteiro e positivo. Tente novamente:')
    name = input("Digite seu nome: ")
    area = input("Digite a area: ")

    profissional[codigo] = (name, area)

N = int(input("Digite um N maior que zero: "))
while N <= 0:
    N = int(input("Digite um N maior que zero: "))

tabela = {}
for i in range(N):
    leitura(tabela)
codigo = int(input("Digite um codigo para ser pesquisado: "))
while codigo > 0:
    if codigo in tabela:
        print(f"Código encontrado.\nNome: {tabela[codigo][0]}\nÁrea: {tabela[codigo][1]}")
    else:
        print("Código inexistente.")

    codigo = int(input("Digite um código para ser pesquisado: "))
    
    