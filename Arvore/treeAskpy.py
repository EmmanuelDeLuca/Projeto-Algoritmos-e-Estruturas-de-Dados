from hashlib import new


class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def insert(root, newValue):
        if root is None:
            root = BinaryTreeNode(newValue)
            return root
        if newValue < root.data:
            root.leftChild = root.insert(root.leftChild, newValue)
        else:
            root.rightChild = root.insert(root.leftChild, newValue)
        return root
        
root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)
a1=root
a2=a1.leftChild
a3=a1.rightChild
a4=a2.leftChild
a5=a2.rightChild
a6=a3.leftChild
a7=a3.rightChild
print("Root Node is:")
print(a1.data)
print("left child of node is:")
print(a1.leftChild.data)
print("right child of node is:")
print(a1.rightChild.data)
print("Node is:")
print(a2.data)
print("left child of node is:")
print(a2.leftChild.data)
print("right child of node is:")
print(a2.rightChild.data)
print("Node is:")
print(a3.data)
print("left child of node is:")
print(a3.leftChild.data)
print("right child of node is:")
print(a3.rightChild.data)
print("Node is:")
print(a4.data)
print("left child of node is:")
print(a4.leftChild)
print("right child of node is:")
print(a4.rightChild)
print("Node is:")
print(a5.data)
print("left child of node is:")
print(a5.leftChild)
print("right child of node is:")
print(a5.rightChild)
print("Node is:")
print(a6.data)
print("left child of node is:")
print(a6.leftChild)
print("right child of node is:")
print(a6.rightChild)
print("Node is:")
print(a7.data)
print("left child of node is:")
print(a7.leftChild)
print("right child of node is:")
print(a7.rightChild)