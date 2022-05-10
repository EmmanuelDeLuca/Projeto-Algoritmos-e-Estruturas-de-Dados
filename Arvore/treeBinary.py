#Arvore Binaria de busca

#Classe Nó
import re

#DO MODO CODIGO RECURSIVO 
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.data)
#DO MODO ITERATIVO
class No:
    def __init__(self, key, dir, esq) -> None:
        self.item = key
        self.dir = dir
        self.esq = esq

#DO MODO CODIGO RECURSIVO
class BinaryTree:
    def __init__(self, data=None, node=None) -> None:
        if node:
            self.root = node
        elif data:

            node = Node(data)
            self.root = node
        else:
            self.root = None
# DO MODO ITERATIVO
class Tree:
    def __init__(self) -> None:
        self.root = No(None,None,None)
        self.root = None

#DO MODO CODIGO RECURSIVO
#INSERIR
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x=x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
        
# DO MODO ITERATIVO
#INSERIR
    def inserir(self, v):
        novo = No(v, None, None) #Criando novo nó
        if self.root == None:
            self.root = novo
        else: # se não for a raiz
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item:
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                else:
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return

#MODO RECURSIVO
def search(self, value):
    return self._search(value, self.root)
def _search(self, value, node):
    if node is None:
        return node
    if node.data == value:
        return BinaryTree(node)
    if value < node.data:
        return self._search(value, node.left)
    return self._search(value, node.right)
#MODO ITERATIVO
def busca(self, chave):
    if self.root == None:
        return None # se for vazia
    atual = self.root #começa a procura desde raiz
    while atual.item != chave: #enquanto não encontrou
        if chave < atual.item:
            atual = atual.esq #caminha para esquerda
        else:
            atual = atual.dir #caminha para direita
        if atual == None:
            return None #encontrou uma folha -> sai
    return atual #terminou um laço while e chegou aqui e pq encoutr item
#https://gist.github.com/divanibarbosa/a8662693e44ab9ee0d0e8c2d74808929
#https://github.com/python-cafe/data_structures/blob/master/arvores/tree.py