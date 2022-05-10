class Grafo:
    def __init__(self, V, E):
        self.V = V
        self.A = E

    def adj(self, v):
        return self.A[v]

    def bfs(self, origem):
        aux = 1
        visitado = [False] * len(self.V)
        antecessor = [-1] * len(self.V)
        fila = []

        visitado[origem-1] = True
        fila.append(origem)
        while fila:
            v = fila.pop()
            for i in g.adj(v):
                if visitado[i-1] not in False:
                    visitado[i-1] = True
                    fila.append(i)
                    antecessor[i-1] = v
                    aux += 1
        
        return aux
    def depthFirst(self, origem):
        lista = [origem]
        visitado = []
        while len(lista) > 0:
            vertice = lista.pop()
            if vertice in visitado:
                continue
            visitado.append(vertice)
            for v in self.A[vertice]:
                if v not in visitado:
                    lista.append(v)
        return len(visitado)

if __name__ == "__main__":
    entrada = input().split()
    user = int(entrada[0]) 
    conecta = int(entrada[1]) 
    V = []
    E = [[] for _ in range(user+1)]

    for i in range(1, user+1):
        V.append(i)

    for i in range(conecta):
        conex1, conex2 = input().split()
        conex1 = int(conex1)
        conex2 = int(conex2)
        E[conex1].append(conex2)
        E[conex2].append(conex1)

    g = Grafo(V, E)
    outuput = ""
    for i in range(1, user+1):
        outuput += str(g.depthFirst(i)) + " "

    print(outuput.strip())