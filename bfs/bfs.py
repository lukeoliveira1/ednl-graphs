import networkx as nx
import matplotlib.pyplot as plt

from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Graph:
    def __init__(self):
        self.nodes = []
        self.best_track = []

    def display_graph(self):
        for node in self.nodes:
            print(f"{node.value}", end="")
            if node.next:
                print(" --> ", end="")

            current = node.next
            while current:
                if current.next:
                    print(f"{current.value} --> ", end="")
                else:
                    print(current.value, end="")
                current = current.next
            print()

    def print_heads(self):
        for node in self.nodes:
            print(node.value)

    def insert(self, value):
        if any(node.value == value for node in self.nodes):
            return
        self.nodes.append(Node(value))

    def add_edge(self, v1, v2):
        node1 = next((node for node in self.nodes if node.value == v1), None)
        node2 = next((node for node in self.nodes if node.value == v2), None)

        if node1 and node2:
            # INSERIR v2 na lista de adjacência de v1
            last_node = node1
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(v2)

            # INSERIR v1 na lista de adjacência de v2
            last_node = node2
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(v1)

    def bfs_min_jumps(self, start, end):
        if start == end:
            return 0, [start]

        # CRIAR uma fila vazia
        queue = Queue()
        # CRIAR um conjunto de vértices visitados
        visited = set()
        # ADICIONAR origem na fila e marcar como visitado
        queue.put((start, 0, [start]))
        visited.add(start)

        # ENQUANTO a fila NÃO ESTIVER vazia
        while not queue.empty():
            # REMOVER vértice atual da fila
            current_value, jumps, path = queue.get()

            current_node = next(
                (node for node in self.nodes if node.value == current_value), None
            )

            if not current_node:
                continue

            # PARA cada vizinho do vértice atual
            neighbor = current_node.next
            while neighbor:
                # SE vizinho == destino
                if neighbor.value == end:
                    self.best_track = path + [end]
                    return jumps + 1, self.best_track
                # SE vizinho NÃO visitado
                if neighbor.value not in visited:
                    # MARCAR como visitado e ADICIONAR na fila
                    visited.add(neighbor.value)
                    queue.put((neighbor.value, jumps + 1, path + [neighbor.value]))
                neighbor = neighbor.next

        # RETORNAR "Nenhum caminho encontrado"
        return "Nenhum caminho encontrado", []

    def load_from_csv(self, file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].strip().split(",")

            lines = lines[1:]
            for i, line in enumerate(lines):
                self.insert(line[0])

            for line in lines:
                self.add_edge(line[0], line[1])

    def visualize_paths(self, start, end):
        if start == end:
            print("Origem e destino são iguais.")
            return

        G = nx.Graph()
        for node in self.nodes:
            current = node.next
            while current:
                G.add_edge(node.value, current.value)
                current = current.next

        pos = nx.spring_layout(G, seed=42)

        fig, ax = plt.subplots()
        plt.ion()

        queue = Queue()
        visited = set()
        queue.put((start, [start]))
        visited.add(start)

        found_path = None

        while not queue.empty():
            current_value, path = queue.get()

            current_node = next(
                (node for node in self.nodes if node.value == current_value), None
            )

            if not current_node:
                continue

            ax.clear()

            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color="lightgray",
                edge_color="gray",
                ax=ax,
            )

            if len(path) > 1:
                path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
                nx.draw_networkx_edges(
                    G, pos, edgelist=path_edges, edge_color="blue", width=2, ax=ax
                )
                nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red", ax=ax)

            if current_value == end and not found_path:
                found_path = path
                print(f"Caminho encontrado: {found_path}")

            plt.draw()
            plt.pause(1)

            neighbor = current_node.next
            while neighbor:
                if neighbor.value not in visited:
                    visited.add(neighbor.value)
                    queue.put((neighbor.value, path + [neighbor.value]))
                neighbor = neighbor.next

        if found_path:
            ax.clear()

            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color="lightgray",
                edge_color="gray",
                ax=ax,
            )

            path_edges = [
                (found_path[i], found_path[i + 1]) for i in range(len(found_path) - 1)
            ]

            nx.draw_networkx_edges(
                G, pos, edgelist=path_edges, edge_color="green", width=2, ax=ax
            )
            nx.draw_networkx_nodes(
                G, pos, nodelist=found_path, node_color="green", ax=ax
            )

            plt.draw()
            plt.pause(2)

        plt.ioff()
        plt.show()
