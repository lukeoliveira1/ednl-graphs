class Grafo:
    def __init__(self):
        self.grafos = []

    def adicionar_vertice(self, v):
        if v == None:
            return None
        aresta = [v]
        self.grafos.append(aresta)

    def adicionar_aresta(self, v1, v2):
        if v1 is None or v2 is None:
            return None

        for i in self.grafos:
            # se alguma das cabeças das listas dentro do grafo[]
            if i[0] == v1:
                # adiciona v2 na lista de adjacentes
                i.append(v2)
            # se alguma das cabeças das listas dentro do grafo[]
            if i[0] == v2:
                # adiciona v1 na lista de adjacentes
                i.append(v1)

    def exibir_grafo(self):
        for i in self.grafos:
            print(i)


if __name__ == "__main__":
    g = Grafo()
    g.adicionar_vertice("V1")
    g.adicionar_vertice("V2")
    g.adicionar_vertice("V3")
    g.adicionar_vertice("V4")
    g.adicionar_vertice("V5")

    g.adicionar_aresta("V1", "V2")
    g.adicionar_aresta("V1", "V3")
    g.adicionar_aresta("V1", "V4")

    g.adicionar_aresta("V2", "V3")
    g.adicionar_aresta("V2", "V4")
    g.adicionar_aresta("V2", "V5")

    g.adicionar_aresta("V3", "V5")

    g.adicionar_aresta("V4", "V5")

    g.exibir_grafo()
