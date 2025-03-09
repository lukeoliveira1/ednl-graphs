from base import Graph as GraphBase
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value, cost=None):
        self.value = value
        self.next = None
        self.cost = cost
        self.visited = False
        self.estimation_value = float("inf")
        self.previous = None


class Dijkstra(GraphBase):

    def __init__(self):
        self.nodes = []
        self.best_track = []
        self.all_tracks = []
        self.best_cost = float("inf")

    def insert(self, value):
        if any(node.value == value for node in self.nodes):
            return False
        self.nodes.append(Node(value))

        return True
    
    def add_edge(self, v1, v2, cost):
        node1 = next((node for node in self.nodes if node.value == v1), None)
        node2 = next((node for node in self.nodes if node.value == v2), None)

        if not node2 and node1:
            self.insert(v2)
            node2 = next((node for node in self.nodes if node.value == v2), None)

        if node1 and node2:
            last_node = node1
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(v2, cost)

            last_node = node2
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(v1, cost)

    def cost_of(self, origin, current):
        current = self.get_node(current)
        origin = self.get_node(origin)

        while current:
            if current.value == origin.value:
                return current.cost
            current = current.next

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

        return

    def dijkstra(self, origin, v2):
        #Encontra node de origem e define sua estimativa como 0
        lesser_node = None
        for node in self.nodes:
            if node.value == origin:
                node.estimation_value = 0
                lesser_node = node

        #Não para enquanto todos os nós forem visitados
        while not all(node.visited for node in self.nodes):

            #Encontra nó com menor estimativa
            for node in self.nodes:
                if node.estimation_value < lesser_node.estimation_value and node.visited == False:
                    lesser_node = node

            lesser_node.visited = True
            # print("Visitando node", lesser_node.value)
            #Percorre os vizinhos na lista de adjacência
            neighbor = lesser_node.next
            while neighbor:
                flag = False
                for node in self.nodes:
                    if node.value == neighbor.value:
                        flag = not node.visited

                if flag:
                    neighbor.previous = lesser_node

                    #Percorre os anteriores para calcular a estimativa
                    previous = neighbor.previous
                    estimation = 0
                    while previous:
                        # print(f"Passando por {previous.value} e pegando custo para {neighbor.value}")
                        estimation += previous.estimation_value + neighbor.cost

                        previous = previous.previous
                    
                    # print(f"Estimativa de {lesser_node.value} para {neighbor.value}: {estimation}" )

                    node = self.get_node(neighbor.value)
                    if estimation < node.estimation_value:
                        # print(f"Atualizando de {node.value}:{node.estimation_value} para {estimation}")
                        node.estimation_value = estimation

                
                neighbor = neighbor.next

            for node in self.nodes:
                if not node.visited:
                    lesser_node = node

        for node in self.nodes:
            if node.value == v2:
                return f"A menor distância do vértice {origin} para {node.value} é {node.estimation_value}"

    def display_graph(self):
        for node in self.nodes:
            print(f"{node.value}", end="")
            if node.next:
                print(f" --{node.next.cost}--> ", end="")

            current = node.next
            while current:
                if current.next:
                    print(f"{current.value} --{current.next.cost}--> ", end="")
                else:
                    print(current.value, end="")
                current = current.next
            print()

    def load_from_csv(self, file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].strip().split(",")

            lines = lines[1:]
            for i, line in enumerate(lines):
                self.insert(line[0])

            for line in lines:
                self.add_edge(line[0], line[1], int(line[2]))

    def visualize_tracks(self):
        if not self.all_tracks:
            print("Nenhum caminho encontrado.")
            return

        G = nx.DiGraph()
        for node in self.nodes:
            current = node.next
            while current:
                G.add_edge(node.value, current.value, weight=current.cost)
                current = current.next

        pos = nx.spring_layout(G, seed=64)

        fig, ax = plt.subplots()
        plt.ion()

        for path in self.all_tracks:
            ax.clear()

            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color="lightgray",
                edge_color="gray",
                ax=ax,
            )
            labels = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

            path_edges = [
                (edge.value, next_edge.value) for edge, next_edge in zip(path, path[1:])
            ]
            for edge in path_edges:
                nx.draw_networkx_edges(
                    G, pos, edgelist=[edge], edge_color="blue", width=2, ax=ax
                )
                nx.draw_networkx_nodes(
                    G, pos, nodelist=[edge[0], edge[1]], node_color="red", ax=ax
                )
                plt.pause(1)

            plt.pause(1)

        ax.clear()

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightgray",
            edge_color="gray",
            ax=ax,
        )
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

        best_path_edges = [
            (edge.value, next_edge.value)
            for edge, next_edge in zip(self.best_track, self.best_track[1:])
        ]
        for edge in best_path_edges:
            nx.draw_networkx_edges(
                G, pos, edgelist=[edge], edge_color="green", width=2, ax=ax
            )
            nx.draw_networkx_nodes(
                G, pos, nodelist=[edge[0], edge[1]], node_color="green", ax=ax
            )

            plt.pause(1)

        plt.ioff()
        plt.show()
