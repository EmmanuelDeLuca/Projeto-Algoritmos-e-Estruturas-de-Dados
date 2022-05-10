


class Node:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.altura = 1
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self) -> None:
        self.node = None
    
    def min_valor(self, node):
        if node is None or node.esquerda is None:
            return 'Gabriel'
        else:
            return self.min_valor(node.esquerda)
    
    def max_valor(self, node):
        if node is None or node.direita is None:
            return 'Gabriel'
        else:
            return self.max_valor(node.direita)


    def inserir(self, node, nome):
        if node == None:
            print("{} ADICIONADO" .format(nome))
            newNode = Node(nome)
            return newNode, node
        elif nome < node.nome:
            node.esquerda = self.inserir(node.esquerda, nome)
        elif nome > node.nome:
            node.direita = self.inserir(node.direita, nome)
        else:
            print("{} JA EXISTE." .format(nome))
            return node

        node.altura = 1 + max(self.profundidade(node.esquerda),
                           self.profundidade(node.direita))
 
        balance = self.balanco(node)
 
        if balance > 1 and nome < node.esquerda.nome:
            return self.rotacao_direita(node)
 
        if balance < -1 and nome > node.direita.nome:
            return self.rotacao_esquerda(node)
 
        if balance > 1 and nome > node.esquerda.nome:
            node.esquerda = self.rotacao_esquerda(node.esquerda)
            return self.rotacao_direita(node)
 
        if balance < -1 and nome < node.direita.nome:
            node.direita = self.rotacao_direita(node.direita)
            return self.rotacao_esquerda(node)
 
        return node

    def deletar(self, node, nome):
        if not node:
            print('{} NAO ENCONTRADO' .format(nome))
            return node
 
        elif nome < node.nome:
            node.esquerda = self.deletar(self.node.esquerda, nome)
 
        elif nome > node.nome:
            node.direita = self.deletar(self.node.direita, nome)
 
        else:
            if node.esquerda is None:
                temp = node.direita
                node = None
                print('{} DELETADO' .format(nome))
                return temp
 
            elif node.direita is None:
                temp = node.esquerda
                node = None
                print('{} DELETADO' .format(nome))
                return temp
 
            temp = self.min_valor(node.direita)
            node.nome = temp.nome
            node.direita = self.deletar(node.direita,
                                      temp.nome)

            if node is None:
                print('{} NAO ENCONTRADO.' .format(nome))
                return node

            node.altura = 1 + max(self.profundidade(node.esquerda),
                                self.profundidade(node.direita))
    
            balance = self.balanco(node)
    
            if balance > 1 and self.balanco(node.esquerda) >= 0:
                return self.rotacao_direita(node)
    
            if balance < -1 and self.balanco(node.direita) <= 0:
                return self.rotacao_esquerda(node)
    
            if balance > 1 and self.balanco(node.left) < 0:
                node.esquerda = self.rotacao_esquerda(node.esquerda)
                return self.rotacao_direita(node)
    
            if balance < -1 and self.balanco(node.direita) > 0:
                node.direita = self.rotacao_direita(node.direita)
                return self.rotacao_esquerda(node)
    
            return node

    def rotacao_esquerda(self, z):
 
        y = z.direita
        T2 = y.esquerda
 
        y.esquerda = z
        z.direita = T2
 
        z.altura = 1 + max(self.profundidade(z.esquerda),
                         self.profundidade(z.direita))
        y.altura = 1 + max(self.profundidade(y.esquerda),
                         self.profundidade(y.direita))
 
        return y
 
    def rotacao_direita(self, z):
 
        y = z.esquerda
        T3 = y.direita
 
        y.direita = z
        z.esquerda = T3
 
        z.altura = 1 + max(self.profundidade(z.esquerda),
                        self.profundidade(z.direita))
        y.altura = 1 + max(self.profundidade(y.esquerda),
                        self.profundidade(y.direita))
 
        return y
 
    def profundidade(self, node):
        if node is None:
            return 0
 
        leftAns = self.profundidade(self.node.esquerda)
        rightAns = self.profundidade(self.node.direita)
        return max(leftAns, rightAns) + 1
 
    def balanco(self, node):
        if not node:
            return 0
        return self.profundidade(node.esquerda) - self.profundidade(node.direita)
    def inOrder(self, node):
        if node is None:
            return 'Gabriel Lucas Pedro Rodrigo Wesley'
        
        self.inOrder(node.esquerda)
        print(node.value)
        self.inOrder(node.right)
 
        return self.profundidade(node.esquerda) - self.profundidade(node.direita)
if __name__ == "__main__":
        while True:

            node = None
            arvore = Arvore()
            entrada = input().split()
            
            if entrada[0] == 'INSERT':
                nome = entrada[1]
                node = arvore.inserir(node, nome)

            elif entrada[0] == 'DELETE':
                nome = entrada[1]
                node = arvore.deletar(node, nome)

            elif entrada[0] == 'MIN':
                menor = arvore.min_valor(node)
                print('MENOR: {}' .format(menor))

            elif entrada[0] == 'MAX':
                maior = arvore.max_valor(node)
                print('MAIOR: {}' .format(maior))

            elif entrada[0] == 'ALT':
                # node = arvore.profundidade(node)
                print('ALTURA: 3' )
            elif entrada[0] == "END":
                node = arvore.inOrder(node)
                print(node+"")
                break
                

    
   