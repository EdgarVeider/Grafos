class Node:
    def __init__(self, dado):
        self.dado = dado
        self.distancia = None
        self.proximo = None
        self.predecessor = None

class HeaderList:
    def __init__(self, identificador, tipo = "caminho"):
        self.identificador = identificador
        self.tipo = tipo
        self.proximo = None

class Lista:
    def __init__(self):
        self.vertices = []

    def InserirHeader(self, dado):
        header = HeaderList(dado)
        self.vertices.append(header)

    def VerificarHeader(self, dado):
        for x in self.vertices:
            if x.identificador == dado:
                return True
        return False

    def PosicaoHeader(self, dado):
        contador = 0
        for x in self.vertices:
            if (x.identificador == dado):return contador
            else: contador = contador +1
    
    def AcharHeaderTipo(self, tipo):
        for x in self.vertices:
            if (x.tipo == tipo):return x.identificador
        else: -1

    def InserirArestas(self, v1, v2):
        #de v1 para v2
        pos_v1 = self.PosicaoHeader(v1)
        aux_no = self.vertices[pos_v1]
        while aux_no.proximo != None:
            aux_no = aux_no.proximo
        aux_no.proximo = Node(v2)

    def LE_INSERIR(self, v1, v2):
        #verifica se vertice existe e se nao adiciona
        if not(self.VerificarHeader(v1)):
            self.InserirHeader(v1)
        if not(self.VerificarHeader(v2)):
            self.InserirHeader(v2)
        
        #Adicionando as arestas
        self.InserirArestas(v1, v2)
        self.InserirArestas(v2, v1)

    

class graph:
    def __init__(self, Lista: Lista):
        self.lista = Lista

    def BuscaLargura(self):
        print(lista.AcharHeaderTipo("saida"))
        



lista = Lista()
lista.LE_INSERIR("a", "b")
lista.LE_INSERIR("b", "*")
lista.LE_INSERIR("*", "c")

lista.vertices[0].tipo = "entrada"
lista.vertices[3].tipo = "saida"

grafo = graph(lista)
grafo.BuscaLargura()





