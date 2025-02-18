# vértice -> [ (V3) -> V2 -> V4 ]
class Adjacencia:
    def __init__(self, vertice):
        self.vertice = vertice
        self.proxima_adjacencia = (
            None  # ponteiro para a próxima aresta na lista de adjacência
        )

# Vertice V1
# Vertice V2
# Vertice V3
# add_aresta(v1, v2)

# Adjancencia(v2)
# AdjacenciaV2.proxima_adjacencia = None

# VerticeV1.cabeca_lista_de_adjancencias = Adjancencia(v2)

# V1 -> (CABEÇA V2) 
# V2 -> (CABEÇA V1)

# add_aresta(v2, v3)

# Adjancencia(v3)
# AdjacenciaV3.proxima_adjacencia = (CABEÇA V2) AdjanceciaV1
# v2.cabeça = AdjanceciaV3

# V2 -> (CABEÇA V3) -> V1

class Vertice:
    def __init__(self, data):
        self.data = data
        self.cabeca_lista_de_adjancencias = None  # ponteiro para a lista de adjacências (arestas conectadas a este vértice)


class Grafo:
    def __init__(self):
        self.vertices = []

    def adicionar_vertice(self, v: Vertice):
        if v == None:
            return None
        self.vertices.append(v)

    def adicionar_aresta(self, v1: Vertice, v2: Vertice):
        if v1 is None or v2 is None:
            return None

        # v1       v2

        nova_aresta = Adjacencia(v1)  # ----------> v1
        nova_aresta.proxima_adjacencia = (
            v2.cabeca_lista_de_adjancencias
        )  # aponta para a antiga cabeça da lista de adjacência
        v2.cabeca_lista_de_adjancencias = (
            nova_aresta  # atualiza a cabeça da lista de adjacência de v2
        )

        nova_aresta2 = Adjacencia(v2)
        nova_aresta2.proxima_adjacencia = (
            v1.cabeca_lista_de_adjancencias
        )  # aponta para a antiga cabeça da lista de adjacência
        v1.cabeca_lista_de_adjancencias = (
            nova_aresta2  # atualiza a cabeça da lista de adjacência de v1
        )

    def exibir_grafo(self):
        for vertice in self.vertices:
            atual = (
                vertice.cabeca_lista_de_adjancencias
            )  # primeiro elemento da lista de adjacências
            linha = f"{vertice.data} -> "
            while atual:
                linha += f"{atual.vertice.data} -> "
                atual = atual.proxima_adjacencia
            linha += "None"
            print(linha)


if __name__ == "__main__":
    g = Grafo()

    v1 = Vertice("V1")
    v2 = Vertice("V2")
    v3 = Vertice("V3")
    v4 = Vertice("V4")
    v5 = Vertice("V5")

    g.adicionar_vertice(v1)
    g.adicionar_vertice(v2)
    g.adicionar_vertice(v3)
    g.adicionar_vertice(v4)
    g.adicionar_vertice(v5)

    g.adicionar_aresta(v1, v2)
    g.adicionar_aresta(v1, v3)
    g.adicionar_aresta(v1, v4)

    g.adicionar_aresta(v2, v3)
    g.adicionar_aresta(v2, v4)
    g.adicionar_aresta(v2, v5)

    g.adicionar_aresta(v3, v5)

    g.adicionar_aresta(v4, v5)

    g.exibir_grafo()
