# Instituto Federal de Minas Gerais - Campus Formiga
# Estrutura de Dados 2
# Jonathan Arantes

from Vertice import Vertice
from Aresta import Aresta

class Grafo():
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def addVertice(self, id):
        self.vertices.append(Vertice(id))

    def addAresta(self, orig, dest, peso):
        self.arestas.append(Aresta(orig, dest, peso))

    def buscaAresta(self, u, v):
        for i in self.arestas:
            orig = i.getOrigem()
            dest = i.getDestino()
            if orig.getId() == u.getId() and dest.getId() == v.getId():
                return i

    def buscaVertice(self, id):
        