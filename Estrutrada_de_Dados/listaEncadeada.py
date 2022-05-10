#Permitir que os elementos sejam armazenado em espaços quaisquer da memoria.
#Probelmas: Unir os espaços, resolver esse problema -> criação de um nó[base para estrutras]

#Lista sequencial: Elementos armazenados contiguamente
# tamanho unico e não tem tanta flexibilidade.
#Se desejamos inserir um elemento essa lista em questão de complixidade não
# é recomendavel, pois precisaremos mover todos so elementos.
# se desejarmos que essa lista tenha tamanho dinamico, sem um valor pre definido, isso não irá acontecer como ja dito antes, elas tem tamanho fixo.

#Lista encadeadas: estrututura de dados dinamico.
# Possui valor e ponteiro para proximo elemento
#Ponteiro = uma variavel que armazena o endereço de outra variavel.No caso, armaneza o endereço do proximo elemento da lista
#Desvantagens: espaço adicional para os ponteiros, se quisermos acessar um elemento em uma dada posição da lista, precisamos perccorer todos os elementos anteriores.

#Nó da lista
# class NodoLista:
#     """Esta classe represneta um nó de uma lista encadeada"""
#     def __init__(self, dado = 0, proximo_nodo = None):
#         self.dado = dado
#         self.proximo = proximo_nodo 
#         #Aposnta para proximo no da lista
#         # o ultimo apontador tem que indicar que é none
#     def __repr__(self):
#         return '%s -> %s' % (self.dado, self.proximo)

# #Criando una nova class para ponteiro (cabeça da lista)

# class ListaEncadeada:
#     """Esta classe represneta uma lista encadeada."""
#     def __init__(self):
#         #Primeiro apontador da lista
#         self.cabeca = None
#     #O primeiro e o ultimo elemento da lista são muito importantes, chamados de cabeça e cauda
#         def __repr__(self):
#             return "[" + str(self.cabeca) + "]"

# #Inserção

#     def insere_no_inicio(lista, novo_dado):
#         # cria um novo nodo com o dado a ser armazenado
#         novo_nodo = NodoLista(novo_dado)

#         #faz com que o novo nodo seja a cabeça da lista
#         novo_nodo.proximo = lista.cabeca

#         #faz com que a cabela da lista referencie o novo nodo
#         lista.cabeca = novo_nodo

#     def insere_depois(lista, nodo_anterior, novo_dado):
#         assert nodo_anterior, "Nodo anterior precisa existir na lista"

#         #Cria um novo nodo com dado dejesado
#         novo_nodo = NodoLista(novo_dado)

#         #faz o proximo do novo do ser o proximo do nodo anteior
#         novo_nodo.proximo = nodo_anterior.proximo

#         #faz com que novo nodo seja o proximo do nodo anterior.
#         nodo_anterior.proximo = novo_nodo
    
#criando nó




class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    #Reproduzir o append em lista encadeado

    def append(self, elem):
        if self.head:
            #Quando já tem um elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size
    
    def get(self, index):
        pass

    def set(self, index, elem):

        pass

    def __getitem__(self, index):
        # a = lista[6]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        raise IndexError("List index out of range")
    
    def __setitem__(self, index, elem):
        # lista[5] = 9
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range")

    def index(self, elem):
        """Retorna o indice do elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError(f"{elem} não está na lista")
    
        
lista = LinkedList()
print(lista)
lista.append(7)
lista.append(80)
print(len(lista))

print(lista.index(80))



