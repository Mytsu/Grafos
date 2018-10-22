# Instituto Federal de Minas Gerais - Campus Formiga
# Estrutura de Dados 2
# Jonathan Arantes

from Vertice import Vertice
from Aresta import Aresta

class Grafo():

    def __init__(self, dir = False):
        self.vertices = []
        self.arestas = []
        self.direcionado = dir

    def addVertice(self, id):
        self.vertices.append(Vertice(id))

    def addAresta(self, orig, dest, peso):
        self.arestas.append(Aresta(orig, dest, peso))
        if not self.direcionado:
            self.arestas.append(Aresta(dest, orig, peso))

    def buscaAresta(self, u, v):
        for i in self.arestas:
            orig = i.getOrigem()
            dest = i.getDestino()
            if orig.getId() == u.getId() and dest.getId() == v.getId():
                return i

    def buscaVertice(self, id):
        for i in self.vertices:
            if id == i.getId():
                return i
    
    def grafoVazio(self):
        if len(self.vertices) == 0:
            return True
        else:
            return False

    def eh_euleriano(self):
        for u in self.vertices:
            if self.grau(u) % 2 is not 0:
                return False
        return True

    def grau(self, u):
        grau = 0
        for w in self.arestas:
            if u == w.getOrigem():
                grau += 1
        return grau
        