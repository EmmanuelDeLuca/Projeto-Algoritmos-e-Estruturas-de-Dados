

class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. de vertices
		self.graph = [] 
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		else:
			parent[yroot] = xroot
			rank[xroot] += 1

    
	def KruskalMST(self):

		result = [] # This will store the resultant MST

		i = 0
		e = 0

		self.graph = build_max_heap(self.graph)

		parent = []
		rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		while e < self.V - 1:

			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)


			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
		minimumCost = 0
		for u, v, weight in result:
			minimumCost += weight
		print(minimumCost)




    

if __name__ == "__main__":
    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])
    g = Graph(m)

    for i in range(n):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        w = int(line[2])
        g.addEdge(u, v, w)

    total = [[100] for i in range(g.V)]
    total = g.KruskalMST()
def troca_elemento( vetor, i, aux):
    vetor[i], vetor[aux] = vetor[aux], vetor[i]

def left( i):
    return (2 * i) + 1

def right( i):
    return (2 * i) + 2

def max_heapify(veeetor, i):
    tamanho_do_heap = len(veeetor) - 1
    l = left(i)
    r = right(i)
    if l <= tamanho_do_heap and veeetor[l] < veeetor[i]:
        maior = l
    else:
        maior = i
    if r <= tamanho_do_heap and veeetor[r] < veeetor[maior]:
        maior = r
    if maior != i:
        troca_elemento(veeetor, i, maior)
        max_heapify(veeetor, maior)

def build_max_heap(veeetor):
    tamanho_do_heap = len(veeetor)
    for i in range(tamanho_do_heap,tamanho_do_heap//2, -1):
        max_heapify(veeetor, i)