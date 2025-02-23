from .main import AdjacentNodesLists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.max_track = ()


class AdjacentNodesLists(AdjacentNodesLists):

    def __init__(self):
        self.nodes = []
        self.max_cost = 0
        self.best_track = []

    def dfs_search(self, origin, destiny, current_cost, current_track):
        origin.visited = True

        if origin == destiny:
            if current_cost > self.max_cost:
                self.max_cost = current_cost
                self.best_track = current_track

        current_adjacent_node = origin.next
        while current_adjacent_node.next:
            if not current_adjacent_node.visited:
                self.dfs_search()

        

