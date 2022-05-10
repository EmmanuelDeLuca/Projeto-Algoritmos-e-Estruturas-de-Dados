class Node:
    #Construtor
    def __init__(self, init_data, prev, next):
        self.data = init_data
        self.prev = prev
        self.next = next
    #Obten o dado armazenado
    def get_data(self):
        return self.data
    #Atualiza dado armazenado

    def set_data(self, new_data):
        self.data = new_data
    
class DoubleList:
    def __init__(self) -> None:
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        # trailer é no final
        self.header.next = self.trailer
        # header é no início
        self.trailer.prev = self.header
        self.size = 0
    # Verifica se lista está vazia
    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    # Insere novo nó entre dois nós existentes
    def insert_between(self, item, predecessor, successor):
        newest = Node(item, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest
    # Remove um nó intermediário da lista
 # Header e trailer nunca podem ser removidos!
    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        # Armazena o elemento removido
        element = node.data
        node.prev = node.next = node.element = None
        return element
    # Insere elemento no início
    def insert_first(self, data):
 # nó deve entrar entre header e header.next
        self.insert_between(data, self.header, self.header.next)
 # Insere elemento no final
    def insert_last(self, data):
 # nó deve entrar entre trailer.prev e trailer
        self.insert_between(data, self.trailer.prev, self.trailer)
 # Remove elemento no início
    def delete_first(self):
        if self.is_empty():
            raise Empty('Lista está vazia!')
        return self.delete_node(self.header.next)
 # Remove elemento no final
    def delete_last(self):
        if self.is_empty():
            raise Empty('Lista está vazia!')
        return self.delete_node(self.trailer.prev)
    def print_list(self):
 # Aponta referência para cabeça
        temp = self.header.next
        X = []
 # Percorre lista adicionando elementos em X
        while temp.next != None:
            X.append(temp.data)
            temp = temp.next
        return X


    
        