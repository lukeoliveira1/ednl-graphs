from base import Graph as GraphBase

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
            if current_cost > self.max_cost:
                self.max_cost = current_cost
                self.best_track = current_track

        current_adjacent_node = origin.next
        while current_adjacent_node:
            if not current_adjacent_node.visited:
                print(f"Visiting {current_adjacent_node.value}")
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
