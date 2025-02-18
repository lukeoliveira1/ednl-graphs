class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class AdjacentNodesLists:
    def __init__(self):
        self.nodes = []

    def print_adjacency_list(self):
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
            # Inserir v2 na lista de adjacência de v1
            last_node = node1
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(v2)

            # Inserir v1 na lista de adjacência de v2
            last_node = node2
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(v1)


if __name__ == "__main__":
    adj = AdjacentNodesLists()
    adj.insert(1)
    adj.insert(2)
    adj.insert(3)
    adj.insert(4)
    adj.insert(5)

    adj.add_edge(1, 2)
    adj.add_edge(1, 3)
    adj.add_edge(1, 4)
    adj.add_edge(2, 4)
    adj.add_edge(5, 4)
    adj.add_edge(5, 2)

    adj.print_adjacency_list()
