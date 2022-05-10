from operator import le


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        self.maior = 0
        self.menor = 9999
        
        

    def push(self, elem):
        
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size= self._size + 1
        
        if elem > self.maior: 
            self.maior = elem
        
        elif elem < self.menor:
            self.menor = elem
            
        

    def pop(self):
        
        if self._size != 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        
        raise IndexError("A pilha esta vazia")
    
    def empty(self):
        if self._size == 0:
            print( "Pilha vazia")
        else:
            print("Pilha nao vazia")
        
    def getMax(self):
        print(self.maior)
    
    def getMin(self):
        print(self.menor)
    
    def __len__(self):
        #Tamanho da lista
        return self._size
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r        
    def __str__(self) :
        return self.__repr__()

if __name__ == "__main__":
    pilha = Stack()

    n = int(input())
    for i in range(n):

        entrada = input()
        if "getMax" in entrada:
            pilha.getMax()
        if "getMin" in entrada:
            pilha.getMin()
        if "push" in entrada:
            valora, valorb = entrada.split()
            pilha.push(int(valorb))
        if "pop" in entrada:
            print(pilha.pop())
            print(pilha.__len__())            