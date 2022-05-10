from dataclasses import dataclass
from logging import root
from operator import le
from re import X
from turtle import right
ROOT = "root"
class Node:
    
    
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None) -> None:
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            
            self.simetric_traversal(node.left)
        
        if node.right:
            self.simetric_traversal(node.right)
        print(node)
            

    def postorder_travesal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_travesal(node.left)
        if node.right:
            self.postorder_travesal(node.right)
        print(node)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

class BinarySearchTree(BinaryTree):

    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = X
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=0):
        if node == 0:
            node = self.root
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)
    #MENOR E O MAIOR DA ARVORE
    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
            while node.right:
                node = node.right
        return node.data
    #REMOÇÃO
    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            #filho a direita e a esquerda
            else:
                sub = self.min(node.right)
                node.data = sub
                node.right = self.remove(sub, node.right)
        return node


        



if __name__ =="__main__":

    tree = BinaryTree()
    
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    
    
    tree.simetric_traversal()
    print(end='')
    print(f"Altura {tree.height(n5 )}")