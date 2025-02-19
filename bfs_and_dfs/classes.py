from queue import Queue


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

    def bfs_min_jumps(self, start, end):
        if start == end:
            return 0

        # CRIAR uma fila vazia
        queue = Queue()
        # CRIAR um conjunto de vértices visitados
        visited = set()
        # ADICIONAR origem na fila e marcar como visitado
        queue.put((start, 0))
        visited.add(start)

        # ENQUANTO a fila NÃO ESTIVER vazia
        while not queue.empty():
            # REMOVER vértice atual da fila
            current_value, jumps = queue.get()

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
                    return jumps + 1
                # SE vizinho NÃO visitado
                if neighbor.value not in visited:
                    # MARCAR como visitado e ADICIONAR na fila
                    visited.add(neighbor.value)
                    queue.put((neighbor.value, jumps + 1))
                neighbor = neighbor.next

        # RETORNAR "Nenhum caminho encontrado"
        return "Nenhum caminho encontrado"
