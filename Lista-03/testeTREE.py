import re


class node:
    # Inicializando a instancia da classe do nó com valores padrao
    def __init__(self, num) -> None:
        self.value = num
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    # retorna a altura de um determinado nó
    def height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.height

    def balance(self, Node):
        #usar o FB para calcular se tree avl é balanceada ou não
        # FB = H.esquerda - H.direita < 2
        if Node is None:
            return 0
        else:
            return self.height(Node.left) - self.height(Node.right)

    def MinimumValueNode(self, Node):
        if Node is None or Node.left is None:
            return Node
        else:
            return self.MinimumValueNode(Node.left)
    def maxValueNode(self, Node):
        if Node is None or Node.right is None:
            return Node
        # while Node.right != None:
        #     Node = Node.right
        else:
            return self.maxValueNode(Node.right)
    
    def rotateR(self, Node):
        #Rotação para direita
        a = Node.left
        b = a.right
        a.right = Node
        Node.left = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a
    
    def rotateL(self, Node):
        #Rotação para esquerda
        a = Node.right
        b = a.left
        a.left = Node
        Node.right = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a
    
    def insert(self, val, root):
        if root is None:
            return node(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        elif val > root.value:
            root.right = self.insert(val, root.right)
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root
    
    def delete(self, val, Node):
        if Node is None:
            return Node
        elif val < Node.value:
            Node.left = self.delete(val, Node.left)
        elif val > Node.value:
            Node.right = self.delete(val, Node.right)
        
        else:
            if Node.left is None:
                lt = Node.right
                Node = None
                return lt
            elif Node.right is None:
                lt = Node.left
                Node = None
                return lt
            rgt = self.MinimumValueNode(Node.right)
            Node.value = rgt.value
            Node.right = self.delete(rgt.value, Node.right)

        if Node is None:
            return Node
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))

        balance = self.balance(Node)
        if balance > 1 and self.balance(Node.left) >= 0:
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) <= 0:
            return self.rotateL(Node)
        if balance > 1 and self.balance(Node.left) < 0:
            Node.left = self.rotateL(Node.left)
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) > 0:
            Node.right = self.rotateR(Node.right)
            return self.rotateL(Node)
        return Node
    def getHeight(self,root):
        if not root:
            return 0
        print(root.height)
        
    
    def inOrder(self, root):
        if root is None:
            return
        
        self.inOrder(root.left)
        print(root.value)
        self.inOrder(root.right)

Tree = AVL()
rt = None
rt = Tree.insert(3, rt)
rt = Tree.insert(5, rt)
rt = Tree.insert(7, rt)
rt = Tree.insert(8, rt)
# rt = Tree.MinimumValueNode(rt)
# rt = Tree.maxValueNode(rt)
rt = (Tree.getHeight(rt))
print("INORDER")
# Tree.inOrder(rt)