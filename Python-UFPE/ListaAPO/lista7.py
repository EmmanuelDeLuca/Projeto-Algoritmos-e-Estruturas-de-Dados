
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# entrada = int(input("Numeros de notas: "))
# listaNotas=[]
# somaNotas = 0
# listaMedia=[]

# for i in range(entrada):
#     notas = float(input("Digite suas notas : "))
#     somaNotas+=notas
#     listaNotas.append(notas)

#     media = somaNotas/entrada

# print(listaNotas, media)

# Ler as notas de N alunos (N é informado pelo
# usuário antes), calcular e imprimir a média das
# notas e depois imprimir as notas que sejam
# maiores do que a média calculada.
entrada = int(input("Numeros de notas: "))

somaNotas = 0
notasAcima = []


for i in range(entrada):
    notas = float(input("Digite suas notas : "))
    somaNotas+=notas

    media = somaNotas/entrada

    for c in range(entrada):
        if notas>= media:
            notasAcima.append(notas)
            print(notasAcima)



    
    
    


