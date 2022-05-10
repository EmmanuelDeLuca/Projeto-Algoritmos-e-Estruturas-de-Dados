class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = [] # default dictionary
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

		self.graph = sorted(self.graph,key=lambda item: item[2])

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

