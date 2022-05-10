#criando nó
# class Node:

#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self) -> None:
#         self.front = self.rear = None
    
#     def isEmpty(self):
#         return self.front == None

#     def enQueue(self, item):
#         temp = Node(item)
#         if self.rear == None:
#             self.front = self.rear = temp
#             print("O programa foi add", item)
#         self.rear.next = temp
#         self.rear = temp
#         print(item)
        
#     def DeQueue(self):
#         if self.isEmpty():
#             return
#         temp = self.front
#         self.front = temp.next

#         if(self.front == None):
#             self.rear = None
# if __name__ == '__main__':
#     q = Queue()
#     q.enQueue(10)
    # print("Primeiro da fila: " +str(q.front.data))




# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

# class Queue:
    
#     def __init__(self) -> None:
#         self._size = 0
#         self.first = None
#         self.last = None

#     def push(self, elem, num):
#         #Insere um elemento na filha
#         node = Node(elem)

#         if self.last is None:
#             self.last = node
#         else:
#             self.last.next = node
#             self.last = node
#         if self.first is None:
#             self.first = node
#         self._size = self._size + 1

#         print("O programa ",elem, " foi agendado com sucesso!")
#     def pop(self):
#         if self._size > 0:
#             elem = self.first.data
#             self.first = self.first.next
#             self._size = self._size - 1
#             return elem
#         else:
#             print("A fila esta vazia")
    
#     def peek(self):
#         if self._size > 0:
#             elem = self.first.data
#             return elem
#         else:
#             print("A fila esta vazia")

#     def len(self):
#         return self._size

#     def __repr__(self) -> str:
#         if self._size > 0:
#             r = ""
#             pointer = self.first
#             while(pointer):
#                 r = r + str(pointer.data) + " \n"
#                 pointer = pointer.next
#             return r
#         print("A fila esta vazia")
#     def __str__(self) -> str:
#         return self.__repr__()

# if __name__ == "__main__":
#     fila = Queue()

#     n = int(input())
#     for i in range(n):
#         entrada = input()
#         if "ADD" in entrada:
#             valorA, valorB, valorC = entrada.split()
#             fila.push(int(valorB), int(valorC))
#         if "size" in entrada:
#            print( fila.peek())





class Node:
    def __init__(self, data, data2) -> None:
        self.data2 = data2
        self.data = data
        self.next = None

class Queue:
    
    def __init__(self) -> None:
        self._size = 0
        self.first = None
        self.last = None

    def push(self, elem, elem2):
        #Insere um elemento na filha
        node = Node(elem, elem2)

        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node

        self._size = self._size + 1

        print("O programa",elem,"foi agendado com sucesso!")

    def display(self, num):
        p = self.first
        while p != None:
            temp = num - p.data2
            # print(temp)
            s = temp - p.data2
            print(s)
            if( temp > 0):
                print("O programa",p.data,"executou por",temp, "segundos.")
                print("O programa",p.data,"terminou.")
                p = p.next
            
    def peek(self):
        if self._size > 0:
            
            elem = self.first.data
            print(elem)
        else:
            print("A fila esta vazia")

    def len(self):
        return self._size

if __name__ == "__main__":
    fila = Queue()

    n = int(input())
    for i in range(n):
        entrada = input().upper()
        if "ADD" in entrada:
            valorA, valorB, valorC = entrada.split()
            fila.push(int(valorB), int(valorC))
        if "EXE" in entrada:
            num = entrada.split()
            fila.display(int(num[1]))