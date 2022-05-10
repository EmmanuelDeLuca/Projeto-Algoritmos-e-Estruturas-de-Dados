class Nodo:
    """Estrtura duplamente encadeada."""
    def __init__(self, dado = 0, proximo_nodo = None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self) -> str:
        return '%s -> %s' %(self.dado, self.proximo)

class Fila:
    """Fila usando uma estrutura encadeada"""
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None
        self.size = 0

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"
    
    def insere(self, novo_dado):

        """Insere um elemento no final da fila"""
        novo_nodo = Nodo(novo_dado) #dentro do nó
        #Se a fila estiver vazia
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
            self.size = self.size + 1
        #caso contrario
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo
            self.size = self.size + 1
    def remove(self):
        assert self.primeiro != None, "Impossivel remover"

        self.primeiro = self.primeiro.proximo
        self.size = self.size - 1

        if self.primeiro == None:
            self.ultimo = None
            # self.size = self.size - 1
            
    def __len__(self):
        return self.size
fila = Fila()
for i in range(5):
    fila.insere(i)
    print("Insere o valor {0} final da fila: {1}".format(i, fila))

while fila.primeiro != None:
    fila.remove()
    print("Removendo elemento que está no começo da fila: ", fila)
print(fila.__len__())