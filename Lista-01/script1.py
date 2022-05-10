#Inserir na pilha
#remover da pilha


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        self.maior = 0
        self.menor = 0
        

    def push(self, elem):
        
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size= self._size + 1

        self.maior = elem
        self.menor = elem

        if (elem > self.maior):
            self.maior = node.data
        if (elem < self.menor):
            self.menor = node.data
            
    def pop(self):
    
        if self._size == 0:
            print("empty stack")
        else:
            if(self._size != 0):
                node = self.top
                self.top = self.top.next
                self._size = self._size - 1
                print(node.data)
    
    def getMax(self):
        aux = self.top
        count = 1
        self.maior = 0
        if self._size == 0:
            print("empty stack")
        else:
            while (count <= self._size):

                if (aux.data > self.maior):
                    self.maior = aux.data
                aux = aux.next    
                count += 1
            print(self.maior)
    
    def getMin(self):
        auxiliar = self.top
        count = 1

        if self._size == 0:
            print("empty stack")
        else:
            self.menor = auxiliar.data
            while(count <= self._size):
                if(auxiliar.data <= self.menor):
                    self.menor = auxiliar.data  
                auxiliar = auxiliar.next                
                count += 1
            print(self.menor)
    
    
    

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
            pilha.pop()
            




#Endereçamento fechado
# import unittest
# INITIAL_CAPACITY = 50
# class HashTable:
#     def __init__(self) -> None:
#         self.capacity = INITIAL_CAPACITY
#         self.size = 0
#         self.buckets = [None] * self.capacity
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None

#     def hash(self, key):
#         hashsum = 0
#         for idx, c in enumerate(key):
#             hashsum += (idx + len(key)) ** ord(c)
#             hashsum = hashsum % self.capacity
#         print(hashsum)
#     def insert(self, key, value):
#         self.size += 1
#         index = self.hash(key)
#         node = self.buckets[index]
#         if node is None:
#             self.buckets[index] = Node(key, value)
#             return
#         prev = node
#         while node is not None:
#             prev = node
#             node = node.next
#         prev.next = Node(key, value)

# fun = Node()
# fun.__init__('oi', 4)
# print(fun.insert)
# class HashTable:
#     def __init__(self):
#         self.size = 11
#         self.slots = [None] * self.size
#         self.data = [None] * self.size
    
#     def put(self,key,data):
#         hashvalue = self.hashfunction(key,len(self.slots))
#         if self.slots[hashvalue] == None:
#             self.slots[hashvalue] = key
#             self.data[hashvalue] = data
#         else:
#             if self.slots[hashvalue] == key:
#                 self.data[hashvalue] = data  #replace
#             else:
#                 nextslot = self.rehash(hashvalue,len(self.slots))
#                 while self.slots[nextslot] != None and \
#                       self.slots[nextslot] != key:
#                     nextslot = self.rehash(nextslot,len(self.slots))

#                 if self.slots[nextslot] == None:
#                     self.slots[nextslot]=key
#                     self.data[nextslot]=data
#                 else:
#                     self.data[nextslot] = data #replace

#     def hashfunction(self,key,size):
#         return key%size

#     def rehash(self,oldhash,size):
#         return (oldhash+1)%size

#     def get(self,key):
#         startslot = self.hashfunction(key,len(self.slots))

#         data = None
#         stop = False
#         found = False
#         position = startslot
#         while self.slots[position] != None and  \
#                             not found and not stop:
#             if self.slots[position] == key:
#                 found = True
#                 data = self.data[position]
#             else:
#                 position=self.rehash(position,len(self.slots))
#                 if position == startslot:
#                     stop = True
#         return data

#     def __getitem__(self,key):
#         return self.get(key)

#     def __setitem__(self,key,data):
#         self.put(key,data)
    
# H=HashTable()
# H[54]="cat"
# H[26]="dog"
# H[93]="lion"
# H[17]="tiger"
# H[77]="bird"
# H[31]="cow"
# H[44]="goat"
# H[55]="pig"
# H[20]="chicken"
# H.slots
# H.data
# import numpy as np


# HT = Hash_table(10)
# HT.insert(10)
# HT.insert(90)
# HT.insert(25)
# HT.insert(5)
# HT.insert(35)
# HT.print_hashtable()
# index = HT.search(35)
# if index!= None :
#     print("\nGiven key is present at index",index)
# else :
#     print("\nGiven key is not present in the hash table")