class No:
    def __init__(self, data):
        self.data = data
        self.esquerda = None
        self.direita = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def montar_arvore(self, entrada = input()):
        entrada = entrada.strip()
        x = entrada.split()
        pre_ordem = x[0]
        em_ordem = x[1]

        
