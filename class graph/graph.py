class Graph:
    def __init__(self, N):
        self.matriz = [[0 for i in range(N)] for j in range(N)]
        self.vertices = N

    def addEdge(self, u, v, w=1):
        self.matriz[u-1][v-1] = w

    def getInDegree(self, V):
        contador = 0
        degree = 0
        while contador < self.vertices:
            if self.matriz[contador][V-1] == 1:
                degree = degree + 1
            contador = contador + 1

        return degree

    def getOutDegree(self, V):
        contador = 0
        degree = 0
        while contador < self.vertices:
            if self.matriz[V-1][contador] == 1:
                degree = degree + 1
            contador = contador + 1
        
        return degree

    def getDegree(self, V):
        return (self.getInDegree(V) + self.getOutDegree(V)) 





