# Instituto Federal de Minas Gerais - Campus Formiga
# Estrutura de Dados 2
# Jonathan Arantes

class Grafo(object):

    __vertices = 20
    __direcionado = True

    def __init__(self):
        # criando matriz de adjacencias 20x20
        self.mat = [0] * self.__vertices
        for i in range(self.__vertices):
            self.mat[i] = [0] * self.__vertices

    def inserirAresta(self, v1, v2, val=1):
        # ira sobrepor valor na aresta
        self.mat[v1][v2] = val
        if not self.__direcionado:
            self.mat[v2][v1] = val

    def pesquisaAresta(self, v1, v2):        
        return self.mat[v1][v2]
    
    def removeAresta(self, v1, v2):
        self.mat[v1][v2] = 0
        if not self.__direcionado:
            self.mat[v2][v1] = 0
    
    def imprimeGrafo(self):
        for i in range(self.__vertices):
            for j in range(self.__vertices):
                if self.__direcionado and not self.mat[i][j] == 0:
                    print('[' + str(i) + ',' + str(j) + ']: ' + str(self.mat[i][j]))
                else:
                    if i <= j and not self.mat[i][j] == 0:
                        print('[' + str(i) + ',' + str(j) + ']: ' + str(self.mat[i][j]))


if __name__ == '__main__':
    grafo = Grafo()
    grafo.inserirAresta(2, 3, 12)
    grafo.inserirAresta(3, 3, 20)
    grafo.inserirAresta(1, 2, 5)
    grafo.inserirAresta(4, 3, 1)
    grafo.inserirAresta(2, 2, 5)
    print(grafo.imprimeGrafo())
    grafo.removeAresta(2, 2)
    print(grafo.pesquisaAresta(2, 2))