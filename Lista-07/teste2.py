class Node:
    def __init__(self, nome, valor):
        self.nome = nome 
        self.valor = valor
        self.direita = None
        self.esquerda = None
        self.pai = None

class Tree:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, nome, valor ):
        z = Node(nome, valor)
        y = None
        x = self.raiz
        if self. raiz == None:
            self.raiz = z
        else:
            while x != None:
                y = x
                if z.valor > x.valor:
                    x = x.direita
                elif z.valor < x.valor:
                    x = x.esquerda
                else:
                    return 0
        
        z.pai = y
        if y == None:
            self.raiz = z
        elif z.valor < y.valor:
            y.esquerda = z
        else:
            y.direita = z

    def buscar(self, y):
        if self.raiz == None:
            return None
        Q = self.raiz
        while  y != Q.valor:
            if y == Q.nome:
                return Q.valor
            if y < Q.valor:
                Q = Q.esquerda
            else:
                Q = Q.direita
        return Q
    def get_min(self, x):
        
        while x.esquerda is not None:
            x = x.esquerda
        return x
    def get_max(self, x):

        while x.direita is not None:
            x = x.direita
        return x
        
    def sucessor(self, x):
        if x.direita is not None:
            return self.get_min(x.direita)
        else:
            y = x.pai
            while y is not None:
                if x != y.direita:
                    break
                x = y
                y = y.pai

            return y
    
    def antecessor(self, x):

        if x.esquerda != None:
            return self.get_max(x.esquerda)
        else:
            y = x.pai
            while y is not None :
                if x != y.esquerda:
                    break
                x = y
                y = y.pai

            return y
if __name__ == "__main__":
    qtd = int(input())
    arvore = Tree()
    for i in range(qtd):
        entrada = input().split()
        if 'ADD' in entrada:
            inserir_new = arvore.inserir(entrada[1], int(entrada[2]))
            if inserir_new != 0:
                print(entrada[1], "inserido com sucesso!")
            else:
                print(entrada[1], "ja esta no sistema.")
        else:
            x = arvore.buscar(int(entrada[1]))
            antecessor = arvore.antecessor(x)
            sucessor = arvore.sucessor(x)
            if antecessor is None and sucessor is None: 
                print("Apenas",x.nome,"existe no sistema...")
            elif sucessor is None:
                print(x.nome,"e o maior! e logo atras vem", antecessor.nome)
            elif antecessor is None:
                print(x.nome,"e o menor! e logo apos vem", sucessor.nome)
            else:
                print(x.nome,"vem apos",antecessor.nome,"e antes de",sucessor.nome)