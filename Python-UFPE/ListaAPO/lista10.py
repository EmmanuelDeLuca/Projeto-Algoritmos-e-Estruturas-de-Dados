# Ler 2 vetores de tamanho N, com N informado
# pelo usuário antes, somar os 2 vetores, imprimir
# os 2 vetores e depois o vetor resultado.
n = int(input("Digite o tamanho do vetor : "))

lista1 = []
lista2 = []
res = []
for i in range(n):

    vetor1 = int(input("valores do vetor 1: "))
    lista1.append(vetor1)
    # print(lista1)

for j in range(n):
    vetor2 = int(input("valores do vetor 2: "))
    lista2.append(vetor2)
    resu = lista1[j] + lista2[j]
    res.append(resu)
    
print(res)

