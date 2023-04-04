class No:
    def __init__(self, data):
        self.data = data
        self.esquerda = None
        self.direita = None

class BinaryTree:
    def __init__(self):
        self.root: No
        self.pre_ordem = None

    def m_arvore(self, esq: str, dir: str, atual_root: No):
    
        if len(esq) != 0:
            atual_root.esquerda = No(self.pre_ordem[0])
            #print(atual_root)
            #atual_root = atual_root.esquerda

            str_temp = esq.split(self.pre_ordem[0])
            self.pre_ordem = self.pre_ordem[1:len(self.pre_ordem)]
            self.m_arvore(str_temp[0], str_temp[1], atual_root.esquerda)
        if len(dir) != 0:
            atual_root.direita = No(self.pre_ordem[0])
            #print(atual_root)
            #atual_root = atual_root.direita

            str_temp = dir.split(self.pre_ordem[0])
            self.pre_ordem = self.pre_ordem[1:len(self.pre_ordem)]
            self.m_arvore(str_temp[0], str_temp[1], atual_root.direita)

        return
            

    def montar_arvore(self, pre_ordem: str, pos_ordem: str ):
        self.pre_ordem = pre_ordem
        str_temp = pos_ordem.split(self.pre_ordem[0])
        self.root = No(self.pre_ordem[0])
        self.pre_ordem = self.pre_ordem[1:len(self.pre_ordem)]

        self.m_arvore(str_temp[0], str_temp[1], self.root)

    def pos_fixa(self, prox_no: No):

        if prox_no != None:
            self.pos_fixa(prox_no.esquerda)
            self.pos_fixa(prox_no.direita)
            print(prox_no.data)


str_out = input()
str_out = str_out.split()
s1 = str_out[0]
s2 = str_out[1]
 
tree = BinaryTree()

tree.montar_arvore(s1, s2)

tree.pos_fixa(tree.root)


