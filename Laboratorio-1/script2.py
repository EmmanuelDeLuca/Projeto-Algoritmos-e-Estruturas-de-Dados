from ctypes import pointer


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def push(self, elem):
        self.head  = Node(elem)



lista = LinkedList()
lista.push(5)
lista.push(6)
print(lista)