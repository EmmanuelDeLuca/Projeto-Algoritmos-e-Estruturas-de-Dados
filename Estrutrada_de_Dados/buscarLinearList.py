#Busca linear em lista em alocação sequencial
#Percorrer uma lista: iterando elementos ou usando função range
#que irá iterar os index
# -1 -> representa o ultimo elemento da lista

def busca(lista, elem):
    """Retorna o indice do elemento se ele estiver na lista ou none caso contrario"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = 32

indice = busca(lista_estranha, elemento)
if indice is not None:
    print(f"O indice do elemento {elemento} é {indice}")
else:
    print(f"O elemento {elemento} não se encontra na lista")




