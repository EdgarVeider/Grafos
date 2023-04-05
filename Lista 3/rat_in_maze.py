class Node:
    def __init__(self, dado):
        self.dado = dado
        self.distancia = None
        self.proximo = None

class HeaderList:
    def __init__(self, identificador, tipo = "caminho"):
        self.identificador = identificador
        self.tipo = tipo
        self.distancia = 0
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
        self.alcancados = []
        self.computados = []

    def VerificarComputado(self, v1):
        for x in self.computados:
            if v1 == x: return True
        return False

    def VerificarAlcancados(self, v1):
        for x in self.alcancados:
            if v1 == x: return True
        return False
        
    def AdicionarListaVisitados(self, header: HeaderList):
        if not self.VerificarAlcancados(header.identificador):
            self.alcancados.append(header.identificador)
        #adiciona o header que esta sendo lido como computado
        self.computados.append(header.identificador)
        #print(header.identificador+"\n")

        #adiciona todos os nos que nao foram computados ainda na fila de alcancados
        aux_no = header.proximo
        while aux_no != None:
            if not self.VerificarComputado(aux_no.dado):
                self.alcancados.append(aux_no.dado)

                pos_Noalcancado = self.lista.PosicaoHeader(aux_no.dado)
                self.lista.vertices[pos_Noalcancado].distancia = (header.distancia+1)
                #print(self.lista.vertices[pos_Noalcancado].distancia)

            aux_no = aux_no.proximo
        
        self.alcancados.pop(0)


    def DistanciaEntradaSaida(self):
        entrada = lista.AcharHeaderTipo("entrada")

        #print("iteracao 1")
        entrada_pos = lista.PosicaoHeader(entrada)
        self.AdicionarListaVisitados(lista.vertices[entrada_pos])

        contador = 2
        while len(self.alcancados) > 0:
            #print(f"iteracao {contador}")
            entrada_pos = lista.PosicaoHeader(self.alcancados[0])
            self.AdicionarListaVisitados(lista.vertices[entrada_pos])
            contador = contador +1

        distancia1 = lista.vertices[lista.PosicaoHeader("*")].distancia

        #limpando os arrays
        self.alcancados.clear()
        self.computados.clear()

        #limpando as distancias
        for x in self.lista.vertices:
            x.distancia = 0

        obejetivo_pos = self.lista.PosicaoHeader("*")
        self.AdicionarListaVisitados(lista.vertices[obejetivo_pos])
        
        contador = 2
        while len(self.alcancados) > 0:
            #print(f"iteracao {contador}")
            entrada_pos = lista.PosicaoHeader(self.alcancados[0])
            self.AdicionarListaVisitados(lista.vertices[entrada_pos])
            contador = contador +1

        distancia2 = lista.vertices[lista.PosicaoHeader("d")].distancia

        print(distancia1 + distancia2)




lista = Lista()
lista.LE_INSERIR("a", "b")
lista.LE_INSERIR("b", "*")
lista.LE_INSERIR("*", "c")
lista.LE_INSERIR("a", "d")

lista.vertices[0].tipo = "entrada"
lista.vertices[4].tipo = "saida"

grafo = graph(lista)
grafo.DistanciaEntradaSaida()





