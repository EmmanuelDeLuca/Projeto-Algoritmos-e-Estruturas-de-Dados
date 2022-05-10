

#separate chaining in python
class Node() :
    
    def __init__(self,value) :
        self.value = value
        self.next = None

class Linked_List() :
    
    def __init__(self) :
        self.head = None
        
    def insert(self,value) :
        if not self.head :
            self.head = Node(value)
        else :
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = Node(value)
            
    def search(self,value) :
        temp = self.head
        while temp :
            if temp.value == value :
                return True
            temp = temp.next
        return False
    
    def print_LL(self) :
        temp = self.head
        if not temp :
            print(None)
        while temp :
            if temp.next :
                print(temp.value,"--->",end="  ")
            else :
                print(temp.value)
            temp = temp.next
            
            
class Hash_table() :
    def __init__(self) :
        pass
        
        
    def hash(self,key) :
        # Hash function is h(x) = x%10
        return key% self.size
    def alt(self, size):
        self.size = size
        self.hashtable =([None]*self.size)
        for x in range(self.size) :
            self.hashtable[x] = Linked_List()
    
    def insert_key(self,key) :
        index = self.hash(key)
        self.hashtable[index].insert(key)
        
        
    def search_key(self,key) :
        index = self.hash(key)
        boolean = self.hashtable[index].search(key)
        return boolean
    
    def print_HT(self) :
        print("Hash table is :- \n")
        print("Index \t\tValues\n")
        for x in range(self.size) :
            print(x,end="\t\t")
            self.hashtable[x].print_LL()
    


if __name__ == "__main__":
    HT = Hash_table()
    n = int(input())

    for i in range(n):
        HT.alt(n)
        entrada = input()
        valorA = entrada.split()
        HT.insert_key(int(entrada))


        
    if HT.search_key(17) :
        print("Given key is present\n")
    else :
        print("Given key is not present\n")
    HT.print_HT()