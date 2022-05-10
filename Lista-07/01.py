class Graph:
	def __init__(self, vertices, qtd):
    self.quantidade = qtd
		self.V = vertices
		self.graph = []
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])
	def printArr(self, dist, dist_1):
		for i in range(self.quantidade):
			print('Vertice: %d', %i ,'Antecessor: %d',%dist_1[i], 'Distancia: %d', %dist[i])
	def BellmanFord(self, src):
    dist_1 = [-1] * self.V
		dist = [float("Inf")] * self.V
		dist[src] = 0
		for _ in range(self.V - 1):
			for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						dist[v] = dist[u] + w
            dist_1[v] = u
		for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						print("frase dele")
						return
		self.printArr(dist, dist_1)
if __name__ == "__main__":
    entrada = int(input())
    for i in range(entrada):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        g = Graph(v, u)
        for i in range(v):
            lines = input().split()
            a = int(lines[0])
            b = int(lines[1])
            c = int(lines[2])
            g.addEdge(a, b, c)
        m = int(input())
        g.BellmanFord(m)


    print(g.graph)