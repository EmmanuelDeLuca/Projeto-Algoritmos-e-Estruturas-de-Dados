





class Node:
    def __init__(self):  
        self.data = 0
        self.next = None



def sortedIntersect(a, b):
    dummy = Node()
    tail = dummy
    dummy.next = None

    while (a != None and b != None):
        if (a.data == b.data):
            tail.next = push((tail.next), a.data)
            tail = tail.next
            a = a.next
            b = b.next
        elif(a.data < b.data):
            a = a.next
        else:
            b = b.next  
    
    print(dummy.next)


def push(head_ref, new_data):

    new_node = Node()
    new_node.data = new_data
    new_node.next = (head_ref)
    (head_ref) = new_node 
        
    return head_ref
    

def printList(node):
    while (node != None):
        print(node.data)
        node = node.next
    

if __name__=='__main__':
    result = None
    a = input().split()
    for i in a:
        i = (int(i))
    b = input().split()
    for j in b:
        j = (int(j))

    push(i , j)
    printList("Valores: ", result)

    


