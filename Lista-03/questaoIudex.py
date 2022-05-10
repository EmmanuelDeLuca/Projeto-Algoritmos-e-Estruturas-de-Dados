class Hashing:
    def _init_(self, cedula, index):
        self.next = None
        self.cedula = cedula
        self.index = index

class hashTable:
    def _init_(self):
        self.head = None
        self.fim = None
        self.macador_index = 0

    def buscar(self,x):
      pont = self.head

      for c in range(self.macador_index):
        if pont.cedula == x:
          return pont.index
        pont = pont.next

    
    def search_hash(self, cafe):
      pont = self.head
      contador = 0 
      while pont.next:
        if pont.cedula >= cafe:
          pass
        else:
          aux = cafe - pont.cedula
          index  = self.buscar(aux)
          if index != None and contador == 0:
            pont.next = None
            contador = 1
            return pont.index , index
        pont = pont.next
      if contador == 0:
        return None, None
  
    
    def inserindo_hash(self, x):
        novo_elemento = Hashing(x, self.macador_index)
        if self.head == None:
          self.head = novo_elemento
          self.fim = novo_elemento
          self.macador_index += 1
          return
        else:
          self.fim.next = novo_elemento
          self.fim = novo_elemento
        self.macador_index += 1

def main():
    qtd_notas = int(input())
    aux = hashTable()
    for c in range(qtd_notas):
        aux.inserindo_hash(int(input()))


    index1, index2 = aux.buscar_hashig(int(input()))
    if (index1 != None and index2 != None):
        print('[{}, {}]'.format(index1, index2))
    elif index1 == None and index2 == None:
        print('Sem cafe da manha dessa vez :/')

if __name__ == '_main_':
    main()
    
