from base import Graph as GraphBase
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value, cost=None):
        self.visited = False
        self.value = value
        self.next = None
        self.cost = cost


class Graph(GraphBase):

    def __init__(self):
        self.nodes = []
        self.max_cost = 0
        self.best_track = []
        self.all_paths = []
        
    def insert(self, value):
        if any(node.value == value for node in self.nodes):
            return False
        self.nodes.append(Node(value))

        return True

    def dfs_search(self, origin, destiny, current_cost, current_track):
        origin = self.get_node(origin.value)
        if not origin:
            return

        if origin == destiny:
            self.all_paths.append(current_track.copy())
            if current_cost > self.max_cost:
                self.max_cost = current_cost
                self.best_track = current_track

        current_adjacent_node = origin.next
        while current_adjacent_node:
            if not current_adjacent_node.visited:
                self.dfs_search(current_adjacent_node, destiny, current_cost + current_adjacent_node.cost, current_track + [current_adjacent_node])
            
            current_adjacent_node = current_adjacent_node.next

        origin.visited = False

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

        return
    
    def add_edge(self, v1, v2, cost):
        node1 = None
        for n in self.nodes:
            if n.value == v1.value:
                node1 = n
                break

        if node1:
            last_node = node1
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(v2, cost)

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
                    if self.insert(line[0]):
                        for j in range(i, len(lines)):
                            if lines[j][0] != line[0]:
                                break
                            else:
                                self.add_edge(self.nodes[len(self.nodes)-1], lines[j][1], cost=int(lines[j][2]))

    def visualize_paths(self):
        if not self.all_paths:
            print("Nenhum caminho encontrado.")
            return
        
        G = nx.DiGraph()
        for node in self.nodes:
            current = node.next
            while current:
                G.add_edge(node.value, current.value, weight=current.cost)
                current = current.next
        
        pos = nx.spring_layout(G, seed=42) 
        
        fig, ax = plt.subplots()
        plt.ion()
        
        for path in self.all_paths:
            ax.clear()
            
            nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', ax=ax)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
            
            path_edges = [(edge.value, next_edge.value) for edge, next_edge in zip(path, path[1:])]
            for edge in path_edges:
                nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='blue', width=2, ax=ax)
                nx.draw_networkx_nodes(G, pos, nodelist=[edge[0], edge[1]], node_color='red', ax=ax)
                plt.pause(2)
            
            plt.pause(1)
        
        plt.ioff()
        plt.show()

